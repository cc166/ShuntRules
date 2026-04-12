import requests
from pathlib import Path

TARGETS = {
    'LAN.yaml': 'https://kelee.one/Tool/Clash/Rule/LAN_SPLITTER.yaml',
    'Direct.yaml': 'https://kelee.one/Tool/Clash/Rule/Direct.yaml',
    'Proxy.yaml': 'https://kelee.one/Tool/Clash/Rule/Proxy.yaml',
    'AI.yaml': 'https://kelee.one/Tool/Clash/Rule/AI.yaml',
    'TikTok.yaml': 'https://kelee.one/Tool/Clash/Rule/TikTok.yaml',
    'SpeedtestInternational.yaml': 'https://kelee.one/Tool/Clash/Rule/SpeedtestInternational.yaml',
    'Game.yaml': 'https://kelee.one/Tool/Clash/Rule/Game.yaml',
    'Netflix.yaml': 'https://rule.kelee.one/Clash/Netflix.yaml',
    'ESET_China.yaml': 'https://kelee.one/Tool/Clash/Rule/ESET_China.yaml',
}
MIRRORS = ['https://git.repcz.link/kelee.one/Tool/Clash/Rule/','https://git.repcz.link/rule.kelee.one/Clash/']
OUT = Path('mirror/ClashCore')
OUT.mkdir(parents=True, exist_ok=True)
report = ['# Clash 核心成品规则镜像结果', '']
headers = {'User-Agent': 'Mozilla/5.0'}

def fetch_with_fallback(name, url):
    candidates = [url]
    if 'https://kelee.one/Tool/Clash/Rule/' in url:
        candidates.append(url.replace('https://kelee.one/Tool/Clash/Rule/','https://git.repcz.link/kelee.one/Tool/Clash/Rule/'))
    if 'https://rule.kelee.one/Clash/' in url:
        candidates.append(url.replace('https://rule.kelee.one/Clash/','https://git.repcz.link/rule.kelee.one/Clash/'))
    last_err = None
    for cand in candidates:
        try:
            r = requests.get(cand, headers=headers, timeout=60)
            r.raise_for_status()
            text = r.text.replace('\r\n', '\n')
            if 'Attention Required' in text[:800] and 'Cloudflare' in text[:800]:
                raise RuntimeError(f'blocked by cloudflare: {cand}')
            if not text.strip():
                raise RuntimeError(f'empty response: {cand}')
            return cand, text
        except Exception as e:
            last_err = e
    raise last_err

for name, url in TARGETS.items():
    used, text = fetch_with_fallback(name, url)
    OUT.joinpath(name).write_text(text, encoding='utf-8')
    report.append(f'- {name}: {used}')

Path('docs/CLASH-CORE-MIRROR.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
