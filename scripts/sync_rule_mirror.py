import json
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
import requests

UPSTREAM_README = 'https://raw.githubusercontent.com/luestr/ShuntRules/main/README.md'
UA = {'User-Agent': 'Mozilla/5.0'}
OUT = Path('mirror')


def fetch(url):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    text = r.text.replace('\r\n', '\n')
    if 'Attention Required' in text[:500] and 'Cloudflare' in text[:500]:
        raise RuntimeError(f'blocked: {url}')
    return text


def extract_loon_raw(url: str) -> str:
    if 'openloon/import' in url and 'rules=' in url:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if 'rules' in qs and qs['rules']:
            return unquote(qs['rules'][0])
    return url


def filename_from_url(url: str) -> str:
    return urlparse(url).path.rsplit('/', 1)[-1]

readme = fetch(UPSTREAM_README)
pat = re.compile(r'\|\s*\d+\s*\|\s*\[\[Loon\]\s+([^\]]+)\]\(([^)]+)\)\s*\|\s*\d+\s*\|\s*\[\[Clash\]\s+([^\]]+)\]\(([^)]+)\)\s*\|')
rows = []
for m in pat.finditer(readme):
    loon_name = m.group(1).strip()
    loon_url = extract_loon_raw(m.group(2).strip())
    clash_name = m.group(3).strip()
    clash_url = m.group(4).strip()
    rows.append({
        'name': loon_name,
        'loon_url': loon_url,
        'clash_url': clash_url,
        'loon_file': filename_from_url(loon_url),
        'clash_file': filename_from_url(clash_url),
    })

(OUT/'Loon').mkdir(parents=True, exist_ok=True)
(OUT/'Clash').mkdir(parents=True, exist_ok=True)
manifest = []
errors = []
for row in rows:
    entry = dict(row)
    try:
        loon_text = fetch(row['loon_url'])
        (OUT/'Loon'/row['loon_file']).write_text(loon_text, encoding='utf-8')
        entry['loon_ok'] = True
    except Exception as e:
        entry['loon_ok'] = False
        entry['loon_error'] = str(e)
    try:
        clash_text = fetch(row['clash_url'])
        (OUT/'Clash'/row['clash_file']).write_text(clash_text, encoding='utf-8')
        entry['clash_ok'] = True
    except Exception as e:
        entry['clash_ok'] = False
        entry['clash_error'] = str(e)
    if not entry.get('loon_ok') or not entry.get('clash_ok'):
        errors.append(entry)
    manifest.append(entry)

(OUT/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
summary = [
    '# Mirror Rules',
    '',
    '本目录由 workflow 自动从上游 README 解析并同步规则文件。',
    '',
    f'- 总规则数：{len(manifest)}',
    f'- 完整成功：{sum(1 for x in manifest if x.get("loon_ok") and x.get("clash_ok"))}',
    f'- 部分失败：{sum(1 for x in manifest if not (x.get("loon_ok") and x.get("clash_ok")))}',
    '',
    '## 目录',
    '- `mirror/Loon/`',
    '- `mirror/Clash/`',
    '- `mirror/manifest.json`',
]
(OUT/'README.md').write_text('\n'.join(summary) + '\n', encoding='utf-8')
if errors:
    (OUT/'errors.json').write_text(json.dumps(errors, ensure_ascii=False, indent=2), encoding='utf-8')
