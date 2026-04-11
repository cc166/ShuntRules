import requests
from pathlib import Path

BASE = 'https://raw.githubusercontent.com/yuumimi/rules/release'
UA = {'User-Agent': 'Mozilla/5.0'}

SOURCES = {
    'Telegram': ['telegram', 'discord', 'whatsapp', 'signal', 'line'],
    'SocialMedia': ['twitter', 'instagram', 'facebook', 'reddit'],
    'GitHub': ['github'],
    'YouTube': ['youtube'],
    'Netflix': ['netflix'],
    'ForeignMedia': ['disney', 'spotify', 'bahamut', 'category-entertainment@!cn'],
    'Google': ['google'],
    'Apple': ['apple'],
    'Microsoft': ['microsoft'],
    'Steam': ['steam'],
    'Speedtest': ['speedtest'],
    'TikTok': ['tiktok'],
}

root = Path('.')
(root/'mirror'/'yuumimi'/'clash').mkdir(parents=True, exist_ok=True)
(root/'mirror'/'yuumimi'/'loon').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Clash').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Loon').mkdir(parents=True, exist_ok=True)


def fetch(url):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    return r.text.replace('\r\n', '\n')


def parse_rule_lines(text):
    rows=[]
    for line in text.splitlines():
        s=line.strip()
        if not s or s.startswith('#') or s.startswith('//') or s.startswith(';'):
            continue
        rows.append(s)
    return rows


def uniq(seq):
    out=[]; seen=set()
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

summary = ['# yuumimi 分类同步结果', '']
for category, names in SOURCES.items():
    clash_all=[]; loon_all=[]; subreport=[]
    for name in names:
        cu=f'{BASE}/clash/{name}.txt'
        lu=f'{BASE}/loon/{name}.txt'
        ctext=fetch(cu)
        ltext=fetch(lu)
        Path(f'mirror/yuumimi/clash/{name}.txt').write_text(ctext, encoding='utf-8')
        Path(f'mirror/yuumimi/loon/{name}.txt').write_text(ltext, encoding='utf-8')
        citems=parse_rule_lines(ctext)
        litems=parse_rule_lines(ltext)
        clash_all.extend(citems)
        loon_all.extend(litems)
        subreport.append((name, len(citems), len(litems)))
    clash_all=uniq(clash_all)
    loon_all=uniq(loon_all)
    Path(f'custom/Clash/{category}.yaml').write_text('payload:\n' + '\n'.join(f'  - {x}' for x in clash_all) + '\n', encoding='utf-8')
    Path(f'custom/Loon/{category}.lsr').write_text('\n'.join(loon_all) + '\n', encoding='utf-8')
    summary.append(f'## {category}')
    for name, ccount, lcount in subreport:
        summary.append(f'- {name}: clash={ccount}, loon={lcount}')
    summary.append(f'- merged clash total: {len(clash_all)}')
    summary.append(f'- merged loon total: {len(loon_all)}')
    summary.append('')

Path('docs/YUUMIMI-SYNC-REPORT.md').write_text('\n'.join(summary), encoding='utf-8')
