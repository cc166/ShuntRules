import requests
from pathlib import Path

TARGETS = {
    'Telegram.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Telegram.yaml',
    'GitHub.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/GitHub.yaml',
    'YouTube.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/YouTube.yaml',
    'Google.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Google.yaml',
    'Apple.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Apple.yaml',
    'Microsoft.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Microsoft.yaml',
    'Steam.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Steam.yaml',
    'Twitter.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Twitter.yaml',
    'Facebook.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Facebook.yaml',
    'Instagram.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Instagram.yaml',
    'Reddit.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Reddit.yaml',
    'Discord.yaml': 'https://git.repcz.link/rule.kelee.one/Clash/Discord.yaml',
}
OUT = Path('mirror/ClashPlus')
OUT.mkdir(parents=True, exist_ok=True)
headers = {'User-Agent':'Mozilla/5.0'}
report=['# Clash 扩展成品规则镜像结果（优先级重整）','']
for name, url in TARGETS.items():
    r=requests.get(url, headers=headers, timeout=60)
    r.raise_for_status()
    text=r.text.replace('\r\n','\n')
    OUT.joinpath(name).write_text(text, encoding='utf-8')
    report.append(f'- {name}: {url}')
Path('docs/CLASH-PLUS-MIRROR.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
