import requests
from pathlib import Path

TARGETS = {
    'Reddit.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Reddit.yaml',
    'Emby.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Emby.yaml',
    'AppleTV.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/AppleTV.yaml',
    'HBO.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/HBO.yaml',
    'PrimeVideo.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/PrimeVideo.yaml',
    'Discord.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Discord.yaml',
}
OUT = Path('mirror/ClashPlus')
OUT.mkdir(parents=True, exist_ok=True)
headers = {'User-Agent':'Mozilla/5.0'}
report=['# Clash 扩展成品规则镜像结果','']
for name, url in TARGETS.items():
    r=requests.get(url, headers=headers, timeout=60)
    r.raise_for_status()
    text=r.text.replace('\r\n','\n')
    OUT.joinpath(name).write_text(text, encoding='utf-8')
    report.append(f'- {name}: {url}')
Path('docs/CLASH-PLUS-MIRROR.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
