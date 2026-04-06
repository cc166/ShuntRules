from pathlib import Path

collections = {
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

root = Path('.')
(root/'custom'/'Loon').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Clash').mkdir(parents=True, exist_ok=True)

for name, data in collections.items():
    (root/'custom'/'Loon'/f'{name}.lsr').write_text('\\n'.join(data['loon'])+'\\n', encoding='utf-8')
    (root/'custom'/'Clash'/f'{name}.yaml').write_text('payload:\\n' + '\\n'.join(f'  - {x}' for x in data['clash']) + '\\n', encoding='utf-8')
