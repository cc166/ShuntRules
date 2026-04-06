from pathlib import Path

collections = {
    'AI': {
        'loon': [
            'DOMAIN-SUFFIX,openai.com','DOMAIN-SUFFIX,chatgpt.com','DOMAIN-SUFFIX,claude.ai','DOMAIN-SUFFIX,anthropic.com',
            'DOMAIN-SUFFIX,copilot.microsoft.com','DOMAIN-SUFFIX,githubcopilot.com','DOMAIN-SUFFIX,gemini.google.com',
            'DOMAIN-SUFFIX,makersuite.google.com','DOMAIN-SUFFIX,vercel.com','DOMAIN-SUFFIX,nvidia.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,openai.com','DOMAIN-SUFFIX,chatgpt.com','DOMAIN-SUFFIX,claude.ai','DOMAIN-SUFFIX,anthropic.com',
            'DOMAIN-SUFFIX,copilot.microsoft.com','DOMAIN-SUFFIX,githubcopilot.com','DOMAIN-SUFFIX,gemini.google.com',
            'DOMAIN-SUFFIX,makersuite.google.com','DOMAIN-SUFFIX,vercel.com','DOMAIN-SUFFIX,nvidia.com',
        ],
    },
    'Communication': {
        'loon': [
            'DOMAIN-SUFFIX,telegram.org','DOMAIN-SUFFIX,t.me','DOMAIN-SUFFIX,discord.com','DOMAIN-SUFFIX,discord.gg',
            'DOMAIN-SUFFIX,twitter.com','DOMAIN-SUFFIX,x.com','DOMAIN-SUFFIX,reddit.com','DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com','DOMAIN-SUFFIX,line.me',
        ],
        'clash': [
            'DOMAIN-SUFFIX,telegram.org','DOMAIN-SUFFIX,t.me','DOMAIN-SUFFIX,discord.com','DOMAIN-SUFFIX,discord.gg',
            'DOMAIN-SUFFIX,twitter.com','DOMAIN-SUFFIX,x.com','DOMAIN-SUFFIX,reddit.com','DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com','DOMAIN-SUFFIX,line.me',
        ],
    },
    'Development': {
        'loon': [
            'DOMAIN-SUFFIX,github.com','DOMAIN-SUFFIX,githubusercontent.com','DOMAIN-SUFFIX,githubassets.com','DOMAIN-SUFFIX,cloudflare.com',
            'DOMAIN-SUFFIX,docker.com','DOMAIN-SUFFIX,docker.io','DOMAIN-SUFFIX,jetbrains.com','DOMAIN-SUFFIX,openai.com',
            'DOMAIN-SUFFIX,claude.ai','DOMAIN-SUFFIX,anthropic.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,github.com','DOMAIN-SUFFIX,githubusercontent.com','DOMAIN-SUFFIX,githubassets.com','DOMAIN-SUFFIX,cloudflare.com',
            'DOMAIN-SUFFIX,docker.com','DOMAIN-SUFFIX,docker.io','DOMAIN-SUFFIX,jetbrains.com','DOMAIN-SUFFIX,openai.com',
            'DOMAIN-SUFFIX,claude.ai','DOMAIN-SUFFIX,anthropic.com',
        ],
    },
    'Media': {
        'loon': [
            'DOMAIN-SUFFIX,youtube.com','DOMAIN-SUFFIX,ytimg.com','DOMAIN-SUFFIX,googlevideo.com','DOMAIN-SUFFIX,netflix.com',
            'DOMAIN-SUFFIX,nflxvideo.net','DOMAIN-SUFFIX,spotify.com','DOMAIN-SUFFIX,scdn.co','DOMAIN-SUFFIX,tiktok.com',
            'DOMAIN-SUFFIX,tiktokv.com','DOMAIN-SUFFIX,disneyplus.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,youtube.com','DOMAIN-SUFFIX,ytimg.com','DOMAIN-SUFFIX,googlevideo.com','DOMAIN-SUFFIX,netflix.com',
            'DOMAIN-SUFFIX,nflxvideo.net','DOMAIN-SUFFIX,spotify.com','DOMAIN-SUFFIX,scdn.co','DOMAIN-SUFFIX,tiktok.com',
            'DOMAIN-SUFFIX,tiktokv.com','DOMAIN-SUFFIX,disneyplus.com',
        ],
    },
    'DomesticBasic': {
        'loon': [
            'DOMAIN-SUFFIX,baidu.com','DOMAIN-SUFFIX,qq.com','DOMAIN-SUFFIX,weixin.qq.com','DOMAIN-SUFFIX,taobao.com',
            'DOMAIN-SUFFIX,tmall.com','DOMAIN-SUFFIX,jd.com','DOMAIN-SUFFIX,bilibili.com','DOMAIN-SUFFIX,alicdn.com',
            'DOMAIN-SUFFIX,alipay.com','DOMAIN-SUFFIX,12306.cn',
        ],
        'clash': [
            'DOMAIN-SUFFIX,baidu.com','DOMAIN-SUFFIX,qq.com','DOMAIN-SUFFIX,weixin.qq.com','DOMAIN-SUFFIX,taobao.com',
            'DOMAIN-SUFFIX,tmall.com','DOMAIN-SUFFIX,jd.com','DOMAIN-SUFFIX,bilibili.com','DOMAIN-SUFFIX,alicdn.com',
            'DOMAIN-SUFFIX,alipay.com','DOMAIN-SUFFIX,12306.cn',
        ],
    },
    'Platform': {
        'loon': [
            'DOMAIN-SUFFIX,apple.com','DOMAIN-SUFFIX,icloud.com','DOMAIN-SUFFIX,me.com','DOMAIN-SUFFIX,apple-dns.net',
            'DOMAIN-SUFFIX,google.com','DOMAIN-SUFFIX,gstatic.com','DOMAIN-SUFFIX,googleapis.com','DOMAIN-SUFFIX,googlevideo.com',
            'DOMAIN-SUFFIX,microsoft.com','DOMAIN-SUFFIX,live.com','DOMAIN-SUFFIX,office.com','DOMAIN-SUFFIX,windows.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,apple.com','DOMAIN-SUFFIX,icloud.com','DOMAIN-SUFFIX,me.com','DOMAIN-SUFFIX,apple-dns.net',
            'DOMAIN-SUFFIX,google.com','DOMAIN-SUFFIX,gstatic.com','DOMAIN-SUFFIX,googleapis.com','DOMAIN-SUFFIX,googlevideo.com',
            'DOMAIN-SUFFIX,microsoft.com','DOMAIN-SUFFIX,live.com','DOMAIN-SUFFIX,office.com','DOMAIN-SUFFIX,windows.com',
        ],
    },
}

root = Path('.')
(root/'custom'/'Loon').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Clash').mkdir(parents=True, exist_ok=True)

for name, data in collections.items():
    (root/'custom'/'Loon'/f'{name}.lsr').write_text('\n'.join(data['loon'])+'\n', encoding='utf-8')
    (root/'custom'/'Clash'/f'{name}.yaml').write_text('payload:\n' + '\n'.join(f'  - {x}' for x in data['clash']) + '\n', encoding='utf-8')
