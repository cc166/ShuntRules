import requests
from pathlib import Path

BASE = 'https://rule.kelee.one'
UA = {'User-Agent': 'Mozilla/5.0'}
CATEGORIES = {
    'AI': ['OpenAI','Claude','Copilot','Gemini','Anthropic','GitHub','Vercel','Nvidia','Jetbrains','BardAI','aiXcoder'],
    'Communication': ['Telegram','Discord','Twitter','Reddit','Facebook','Instagram','Line','Mail'],
}

root = Path('.')
(root/'custom'/'Loon').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Clash').mkdir(parents=True, exist_ok=True)


def fetch(url):
    r = requests.get(url, headers=UA, timeout=60)
    r.raise_for_status()
    text = r.text.replace('
', '
')
    head = text[:600].lower()
    if 'attention required' in head or 'you have been blocked' in head:
        raise RuntimeError(f'blocked: {url}')
    return text


def uniq(seq):
    out=[]; seen=set()
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out


def parse_lsr(text):
    rows=[]
    for line in text.splitlines():
        s=line.strip()
        if not s or s.startswith('#') or s.startswith(';') or s.startswith('//'):
            continue
        rows.append(s)
    return uniq(rows)


def parse_yaml_payload(text):
    rows=[]
    in_payload=False
    for line in text.splitlines():
        if line.strip() == 'payload:':
            in_payload=True
            continue
        if not in_payload:
            continue
        s=line.strip()
        if s.startswith('- '):
            rows.append(s[2:].strip())
    return uniq(rows)

fallback = {
    'AI': {
        'loon': [
            'DOMAIN-SUFFIX,openai.com',
            'DOMAIN-SUFFIX,chatgpt.com',
            'DOMAIN-SUFFIX,claude.ai',
            'DOMAIN-SUFFIX,anthropic.com',
            'DOMAIN-SUFFIX,copilot.microsoft.com',
            'DOMAIN-SUFFIX,githubcopilot.com',
            'DOMAIN-SUFFIX,gemini.google.com',
            'DOMAIN-SUFFIX,makersuite.google.com',
            'DOMAIN-SUFFIX,vercel.com',
            'DOMAIN-SUFFIX,nvidia.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,openai.com',
            'DOMAIN-SUFFIX,chatgpt.com',
            'DOMAIN-SUFFIX,claude.ai',
            'DOMAIN-SUFFIX,anthropic.com',
            'DOMAIN-SUFFIX,copilot.microsoft.com',
            'DOMAIN-SUFFIX,githubcopilot.com',
            'DOMAIN-SUFFIX,gemini.google.com',
            'DOMAIN-SUFFIX,makersuite.google.com',
            'DOMAIN-SUFFIX,vercel.com',
            'DOMAIN-SUFFIX,nvidia.com',
        ],
    },
    'Communication': {
        'loon': [
            'DOMAIN-SUFFIX,telegram.org',
            'DOMAIN-SUFFIX,t.me',
            'DOMAIN-SUFFIX,discord.com',
            'DOMAIN-SUFFIX,discord.gg',
            'DOMAIN-SUFFIX,twitter.com',
            'DOMAIN-SUFFIX,x.com',
            'DOMAIN-SUFFIX,reddit.com',
            'DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com',
            'DOMAIN-SUFFIX,line.me',
        ],
        'clash': [
            'DOMAIN-SUFFIX,telegram.org',
            'DOMAIN-SUFFIX,t.me',
            'DOMAIN-SUFFIX,discord.com',
            'DOMAIN-SUFFIX,discord.gg',
            'DOMAIN-SUFFIX,twitter.com',
            'DOMAIN-SUFFIX,x.com',
            'DOMAIN-SUFFIX,reddit.com',
            'DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com',
            'DOMAIN-SUFFIX,line.me',
        ],
    },
}

for cat, names in CATEGORIES.items():
    loon_items=[]; clash_items=[]
    for name in names:
        loon_url=f'{BASE}/Loon/{name}.lsr'
        clash_url=f'{BASE}/Clash/{name}.yaml'
        try:
            loon_items.extend(parse_lsr(fetch(loon_url)))
        except Exception as e:
            print('skip loon', name, e)
        try:
            clash_items.extend(parse_yaml_payload(fetch(clash_url)))
        except Exception as e:
            print('skip clash', name, e)
    loon_items=uniq(loon_items)
    clash_items=uniq(clash_items)
    if not loon_items:
        loon_items=fallback[cat]['loon']
    if not clash_items:
        clash_items=fallback[cat]['clash']
    (root/'custom'/'Loon'/f'{cat}.lsr').write_text('
'.join(loon_items)+'
', encoding='utf-8')
    (root/'custom'/'Clash'/f'{cat}.yaml').write_text('payload:
' + '
'.join(f'  - {x}' for x in clash_items) + '
', encoding='utf-8')
