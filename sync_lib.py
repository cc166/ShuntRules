#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent
CACHE_DIR = Path(os.environ.get('SHUNTRULES_REPORT_CACHE', str(Path.home() / '.cache' / 'shuntrules-sync')))
SOURCE_CACHE_DIR = Path(os.environ.get('SHUNTRULES_SOURCE_CACHE', str(Path.home() / '.cache' / 'shuntrules-sources')))
BAD_MARKERS = ('<!doctype html', '<html', 'just a moment', 'cf-chl', 'forbidden', 'access denied')


@dataclass(frozen=True)
class Category:
    name: str
    source_dir: Path
    output_dir: Path
    suffixes: tuple[str, ...]


def snippet(text: str, limit: int = 220) -> str:
    return ' '.join(text[:limit].split())


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd or ROOT, text=True, capture_output=True, check=True)


def normalize_text(text: str) -> str:
    return text.replace('\r\n', '\n').replace('\r', '\n')


def rule_lines(text: str) -> int:
    count = 0
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(('#', '//', ';')):
            continue
        count += 1
    return count


def validate_text(text: str) -> tuple[bool, dict]:
    text = normalize_text(text)
    lower = text[:1000].lower()
    stats = {
        'bytes': len(text.encode('utf-8')),
        'lines': len(text.splitlines()),
        'rule_lines': rule_lines(text),
        'sha256_16': sha256(text.encode('utf-8')).hexdigest()[:16],
    }
    if any(marker in lower for marker in BAD_MARKERS):
        stats['reason'] = 'blocked-or-html-response'
        return False, stats
    if stats['rule_lines'] <= 0:
        stats['reason'] = 'no-rule-lines'
        return False, stats
    stats['reason'] = 'ok'
    return True, stats


def read_rule(path: Path) -> tuple[bool, dict, str]:
    try:
        text = path.read_text(encoding='utf-8', errors='replace')
    except Exception as exc:
        return False, {'reason': f'unreadable: {exc.__class__.__name__}'}, ''
    ok, stats = validate_text(text)
    return ok, stats, normalize_text(text)


def category_files(base: Path, category: Category) -> list[Path]:
    directory = base / category.output_dir
    if not directory.is_dir():
        return []
    return sorted(
        [p for p in directory.iterdir() if p.is_file() and p.name.endswith(category.suffixes)],
        key=lambda p: p.name.lower(),
    )


def source_files(source_root: Path, category: Category) -> list[Path]:
    directory = source_root / category.source_dir
    if not directory.is_dir():
        raise RuntimeError(f'missing source directory: {category.source_dir}')
    return sorted(
        [p for p in directory.iterdir() if p.is_file() and p.name.endswith(category.suffixes)],
        key=lambda p: p.name.lower(),
    )


def validate_existing(categories: Iterable[Category]) -> dict:
    report = {'meta': {'mode': 'check-existing'}, 'categories': {}, 'failed_paths': []}
    for category in categories:
        checks = {}
        files = category_files(ROOT, category)
        if not files:
            report['failed_paths'].append(str(category.output_dir))
        for path in files:
            ok, stats, _ = read_rule(path)
            rel = path.relative_to(ROOT).as_posix()
            checks[path.name] = stats | {'path': rel, 'valid': ok}
            if not ok:
                report['failed_paths'].append(rel)
        report['categories'][category.name] = {
            'count': len(files),
            'ok': sum(1 for item in checks.values() if item['valid']),
            'failed': sum(1 for item in checks.values() if not item['valid']),
            'checks': checks,
        }
    return report


def existing_valid(existing: dict) -> bool:
    return not existing.get('failed_paths')


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_cache(name: str, data: dict) -> None:
    write_json(CACHE_DIR / f'{name}.json', data)


def print_summary(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False))


def fallback(source_name: str, cache_name: str, existing: dict, error: str) -> int:
    ok = existing_valid(existing)
    report = {
        'meta': {
            'source': source_name,
            'status': 'kept-last-known-good' if ok else 'blocked',
            'note': 'latest source sync failed; existing published files were used only if local validation passed',
            'error': snippet(error, 500),
        },
        'existing': existing,
    }
    write_cache(cache_name, report)
    print_summary({'status': report['meta']['status'], 'existing_valid': ok, 'failed_existing': len(existing.get('failed_paths', []))})
    return 0 if ok else 1


def build_stage(source_root: Path, categories: Iterable[Category], stage_root: Path) -> dict:
    report = {'categories': {}}
    for category in categories:
        existing_names = {p.name for p in category_files(ROOT, category)}
        files = source_files(source_root, category)
        source_names = {p.name for p in files}
        missing = sorted(existing_names - source_names)
        if missing:
            raise RuntimeError(f'{category.name}: source missing existing files: {", ".join(missing[:20])}')
        if not files:
            raise RuntimeError(f'{category.name}: source has no matching files')

        out_dir = stage_root / category.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        checks = {}
        for src in files:
            ok, stats, text = read_rule(src)
            if not ok:
                raise RuntimeError(f'{category.name}/{src.name}: invalid source file: {stats.get("reason")}')
            (out_dir / src.name).write_text(text, encoding='utf-8')
            checks[src.name] = stats | {'path': (category.output_dir / src.name).as_posix(), 'valid': True}
        report['categories'][category.name] = {
            'ok': [p.name for p in files],
            'failed': [],
            'checks': checks,
        }
    return report


def publish_stage(stage_root: Path, categories: Iterable[Category]) -> None:
    for category in categories:
        dst_dir = ROOT / category.output_dir
        src_dir = stage_root / category.output_dir
        dst_dir.mkdir(parents=True, exist_ok=True)
        for old in category_files(ROOT, category):
            old.unlink()
        for src in sorted(src_dir.iterdir(), key=lambda p: p.name.lower()):
            if src.is_file():
                shutil.copy2(src, dst_dir / src.name)


def clone_source(repo_url: str, source_root: Path) -> None:
    if os.environ.get('SHUNTRULES_FORCE_FETCH_FAIL') == '1':
        raise RuntimeError('forced source fetch failure for fallback validation')
    source_root.parent.mkdir(parents=True, exist_ok=True)
    if (source_root / '.git').is_dir():
        run(['git', 'fetch', '--depth', '1', 'origin', 'HEAD'], cwd=source_root)
        run(['git', 'reset', '--hard', 'FETCH_HEAD'], cwd=source_root)
        run(['git', 'clean', '-fd'], cwd=source_root)
    else:
        if source_root.exists():
            shutil.rmtree(source_root)
        run(['git', 'clone', '--depth', '1', repo_url, str(source_root)], cwd=ROOT)


def sync_from_git(source_name: str, repo_url: str, categories: tuple[Category, ...], report_file: Path, cache_name: str) -> int:
    parser = argparse.ArgumentParser(description=f'Sync {source_name} rule files.')
    parser.add_argument('--check-existing', action='store_true', help='validate currently published files without network access')
    args = parser.parse_args()

    existing = validate_existing(categories)
    if args.check_existing:
        summary = {
            'mode': 'check-existing',
            'source': source_name,
            'valid': existing_valid(existing),
            'failed': len(existing.get('failed_paths', [])),
            'categories': {name: {'ok': item['ok'], 'count': item['count']} for name, item in existing['categories'].items()},
        }
        print_summary(summary)
        return 0 if existing_valid(existing) else 1

    try:
        source_root = SOURCE_CACHE_DIR / cache_name / 'source'
        stage_root = SOURCE_CACHE_DIR / cache_name / 'stage'
        if stage_root.exists():
            shutil.rmtree(stage_root)
        clone_source(repo_url, source_root)
        stage_report = build_stage(source_root, categories, stage_root)
        publish_stage(stage_root, categories)
    except Exception as exc:
        return fallback(source_name, cache_name, existing, str(exc))

    report = {
        'meta': {
            'source': source_name,
            'url': repo_url,
            'status': 'synced-verified',
            'note': 'files are published only after source validation and existing-file baseline checks pass',
        },
        'categories': {
            name: {
                'ok_count': len(section.get('ok', [])),
                'failed_count': len(section.get('failed', [])),
            }
            for name, section in stage_report.get('categories', {}).items()
        },
    }
    write_json(report_file, report)
    write_cache(cache_name, {'meta': report['meta'], **stage_report})
    summary = {
        'status': 'synced-verified',
        'source': source_name,
        'categories': {name: {'ok': len(item['ok']), 'failed': len(item['failed'])} for name, item in stage_report['categories'].items()},
    }
    print_summary(summary)
    return 0
