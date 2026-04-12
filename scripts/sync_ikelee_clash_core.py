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

OUT = Path('mirror/ClashCore')
OUT.mkdir(parents=True, exist_ok=True)
report = ['# Clash 核心成品规则镜像结果', '']
headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in TARGETS.items():
    r = requests.get(url, headers=headers, timeout=60)
    r.raise_for_status()
    text = r.text.replace('\r\n', '\n')
    if 'Attention Required' in text[:800] and 'Cloudflare' in text[:800]:
        raise RuntimeError(f'blocked by cloudflare: {url}')
    OUT.joinpath(name).write_text(text, encoding='utf-8')
    report.append(f'- {name}: {url}')

Path('docs/CLASH-CORE-MIRROR.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
