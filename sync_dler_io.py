#!/usr/bin/env python3
"""
Sync dler-io/Rules Surge Provider rules to ShuntRules
"""
from pathlib import Path
import subprocess
import json
import time

REPO_URL = "https://github.com/dler-io/Rules.git"
TEMP_DIR = Path("/tmp/dler-io-Rules")
OUT_BASE = Path("surge")
OUT_PROVIDER = OUT_BASE / "provider"
OUT_MEDIA = OUT_BASE / "media"

report = {
    'meta': {
        'source': 'dler-io/Rules',
        'url': REPO_URL,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
    },
    'provider': {'ok': [], 'failed': []},
    'media': {'ok': [], 'failed': []}
}

def run(cmd):
    """Run shell command and return stdout"""
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}\n{r.stderr}")
    return r.stdout.strip()

def clone_or_pull():
    """Clone or pull dler-io/Rules"""
    if TEMP_DIR.exists():
        print(f"Pulling latest from {REPO_URL}...")
        run(f"cd {TEMP_DIR} && git pull")
    else:
        print(f"Cloning {REPO_URL}...")
        run(f"git clone --depth 1 {REPO_URL} {TEMP_DIR}")

def sync_provider():
    """Sync Surge Provider rules (22 items)"""
    src = TEMP_DIR / "Surge" / "Surge 3" / "Provider"
    OUT_PROVIDER.mkdir(parents=True, exist_ok=True)
    
    for item in src.iterdir():
        if item.is_file() and item.suffix == ".list":
            try:
                dest = OUT_PROVIDER / item.name
                dest.write_text(item.read_text(encoding='utf-8'), encoding='utf-8')
                report['provider']['ok'].append(item.name)
                print(f"✓ {item.name}")
            except Exception as e:
                report['provider']['failed'].append({'name': item.name, 'error': str(e)})
                print(f"✗ {item.name}: {e}")

def sync_media():
    """Sync Surge Provider Media rules (44 items)"""
    src = TEMP_DIR / "Surge" / "Surge 3" / "Provider" / "Media"
    OUT_MEDIA.mkdir(parents=True, exist_ok=True)
    
    for item in src.iterdir():
        if item.is_file() and item.suffix == ".list":
            try:
                dest = OUT_MEDIA / item.name
                dest.write_text(item.read_text(encoding='utf-8'), encoding='utf-8')
                report['media']['ok'].append(item.name)
                print(f"✓ Media/{item.name}")
            except Exception as e:
                report['media']['failed'].append({'name': item.name, 'error': str(e)})
                print(f"✗ Media/{item.name}: {e}")

def save_report():
    """Save sync report"""
    report_file = Path("_sync_report_dler_io.json")
    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"\n📊 Report saved to {report_file}")
    print(f"Provider: {len(report['provider']['ok'])} ok, {len(report['provider']['failed'])} failed")
    print(f"Media: {len(report['media']['ok'])} ok, {len(report['media']['failed'])} failed")

if __name__ == "__main__":
    print("=== Syncing dler-io/Rules ===")
    clone_or_pull()
    sync_provider()
    sync_media()
    save_report()
