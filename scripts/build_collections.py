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
            'DOMAIN-SUFFIX,line.me','DOMAIN-SUFFIX,whatsapp.com','DOMAIN-SUFFIX,signal.org',
        ],
        'clash': [
            'DOMAIN-SUFFIX,telegram.org','DOMAIN-SUFFIX,t.me','DOMAIN-SUFFIX,discord.com','DOMAIN-SUFFIX,discord.gg',
            'DOMAIN-SUFFIX,line.me','DOMAIN-SUFFIX,whatsapp.com','DOMAIN-SUFFIX,signal.org',
        ],
    },
    'SocialMedia': {
        'loon': [
            'DOMAIN-SUFFIX,twitter.com','DOMAIN-SUFFIX,x.com','DOMAIN-SUFFIX,reddit.com','DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com','DOMAIN-SUFFIX,threads.net',
        ],
        'clash': [
            'DOMAIN-SUFFIX,twitter.com','DOMAIN-SUFFIX,x.com','DOMAIN-SUFFIX,reddit.com','DOMAIN-SUFFIX,facebook.com',
            'DOMAIN-SUFFIX,instagram.com','DOMAIN-SUFFIX,threads.net',
        ],
    },
    'GitHub': {
        'loon': [
            'DOMAIN-SUFFIX,github.com','DOMAIN-SUFFIX,githubusercontent.com','DOMAIN-SUFFIX,githubassets.com',
            'DOMAIN-SUFFIX,github.io','DOMAIN-SUFFIX,github.dev','DOMAIN-SUFFIX,githubcopilot.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,github.com','DOMAIN-SUFFIX,githubusercontent.com','DOMAIN-SUFFIX,githubassets.com',
            'DOMAIN-SUFFIX,github.io','DOMAIN-SUFFIX,github.dev','DOMAIN-SUFFIX,githubcopilot.com',
        ],
    },
    'TikTok': {
        'loon': [
            'DOMAIN-SUFFIX,tiktok.com','DOMAIN-SUFFIX,tiktokv.com','DOMAIN-SUFFIX,tiktokcdn.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,tiktok.com','DOMAIN-SUFFIX,tiktokv.com','DOMAIN-SUFFIX,tiktokcdn.com',
        ],
    },
    'YouTube': {
        'loon': [
            'DOMAIN-SUFFIX,youtube.com','DOMAIN-SUFFIX,youtu.be','DOMAIN-SUFFIX,ytimg.com','DOMAIN-SUFFIX,googlevideo.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,youtube.com','DOMAIN-SUFFIX,youtu.be','DOMAIN-SUFFIX,ytimg.com','DOMAIN-SUFFIX,googlevideo.com',
        ],
    },
    'Netflix': {
        'loon': [
            'DOMAIN-SUFFIX,netflix.com','DOMAIN-SUFFIX,nflxvideo.net','DOMAIN-SUFFIX,nflximg.net','DOMAIN-SUFFIX,nflxso.net',
        ],
        'clash': [
            'DOMAIN-SUFFIX,netflix.com','DOMAIN-SUFFIX,nflxvideo.net','DOMAIN-SUFFIX,nflximg.net','DOMAIN-SUFFIX,nflxso.net',
        ],
    },
    'ForeignMedia': {
        'loon': [
            'DOMAIN-SUFFIX,disneyplus.com','DOMAIN-SUFFIX,disney.com','DOMAIN-SUFFIX,hbo.com','DOMAIN-SUFFIX,hbomax.com',
            'DOMAIN-SUFFIX,max.com','DOMAIN-SUFFIX,primevideo.com','DOMAIN-SUFFIX,amazonvideo.com','DOMAIN-SUFFIX,spotify.com',
            'DOMAIN-SUFFIX,scdn.co','DOMAIN-SUFFIX,emby.media','DOMAIN-SUFFIX,bahamut.com.tw','DOMAIN-SUFFIX,gamer.com.tw',
        ],
        'clash': [
            'DOMAIN-SUFFIX,disneyplus.com','DOMAIN-SUFFIX,disney.com','DOMAIN-SUFFIX,hbo.com','DOMAIN-SUFFIX,hbomax.com',
            'DOMAIN-SUFFIX,max.com','DOMAIN-SUFFIX,primevideo.com','DOMAIN-SUFFIX,amazonvideo.com','DOMAIN-SUFFIX,spotify.com',
            'DOMAIN-SUFFIX,scdn.co','DOMAIN-SUFFIX,emby.media','DOMAIN-SUFFIX,bahamut.com.tw','DOMAIN-SUFFIX,gamer.com.tw',
        ],
    },
    'ForeignEcommerce': {
        'loon': [
            'DOMAIN-SUFFIX,amazon.com','DOMAIN-SUFFIX,ebay.com','DOMAIN-SUFFIX,walmart.com','DOMAIN-SUFFIX,bestbuy.com','DOMAIN-SUFFIX,aliexpress.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,amazon.com','DOMAIN-SUFFIX,ebay.com','DOMAIN-SUFFIX,walmart.com','DOMAIN-SUFFIX,bestbuy.com','DOMAIN-SUFFIX,aliexpress.com',
        ],
    },
    'GoogleFCM': {
        'loon': [
            'DOMAIN-SUFFIX,mtalk.google.com','DOMAIN-SUFFIX,firebaseinstallations.googleapis.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,mtalk.google.com','DOMAIN-SUFFIX,firebaseinstallations.googleapis.com',
        ],
    },
    'Google': {
        'loon': [
            'DOMAIN-SUFFIX,google.com','DOMAIN-SUFFIX,gstatic.com','DOMAIN-SUFFIX,googleapis.com','DOMAIN-SUFFIX,googleusercontent.com','DOMAIN-SUFFIX,ggpht.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,google.com','DOMAIN-SUFFIX,gstatic.com','DOMAIN-SUFFIX,googleapis.com','DOMAIN-SUFFIX,googleusercontent.com','DOMAIN-SUFFIX,ggpht.com',
        ],
    },
    'Apple': {
        'loon': [
            'DOMAIN-SUFFIX,apple.com','DOMAIN-SUFFIX,icloud.com','DOMAIN-SUFFIX,me.com','DOMAIN-SUFFIX,apple-dns.net','DOMAIN-SUFFIX,mzstatic.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,apple.com','DOMAIN-SUFFIX,icloud.com','DOMAIN-SUFFIX,me.com','DOMAIN-SUFFIX,apple-dns.net','DOMAIN-SUFFIX,mzstatic.com',
        ],
    },
    'Microsoft': {
        'loon': [
            'DOMAIN-SUFFIX,microsoft.com','DOMAIN-SUFFIX,live.com','DOMAIN-SUFFIX,office.com','DOMAIN-SUFFIX,office365.com','DOMAIN-SUFFIX,windows.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,microsoft.com','DOMAIN-SUFFIX,live.com','DOMAIN-SUFFIX,office.com','DOMAIN-SUFFIX,office365.com','DOMAIN-SUFFIX,windows.com',
        ],
    },
    'Game': {
        'loon': [
            'DOMAIN-SUFFIX,epicgames.com','DOMAIN-SUFFIX,riotgames.com','DOMAIN-SUFFIX,playstation.com','DOMAIN-SUFFIX,xbox.com','DOMAIN-SUFFIX,nintendo.net','DOMAIN-SUFFIX,battle.net',
        ],
        'clash': [
            'DOMAIN-SUFFIX,epicgames.com','DOMAIN-SUFFIX,riotgames.com','DOMAIN-SUFFIX,playstation.com','DOMAIN-SUFFIX,xbox.com','DOMAIN-SUFFIX,nintendo.net','DOMAIN-SUFFIX,battle.net',
        ],
    },
    'Steam': {
        'loon': [
            'DOMAIN-SUFFIX,steampowered.com','DOMAIN-SUFFIX,steamcommunity.com','DOMAIN-SUFFIX,steamstatic.com','DOMAIN-SUFFIX,steamcontent.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,steampowered.com','DOMAIN-SUFFIX,steamcommunity.com','DOMAIN-SUFFIX,steamstatic.com','DOMAIN-SUFFIX,steamcontent.com',
        ],
    },
    'Speedtest': {
        'loon': [
            'DOMAIN-SUFFIX,speedtest.net','DOMAIN-SUFFIX,ookla.com',
        ],
        'clash': [
            'DOMAIN-SUFFIX,speedtest.net','DOMAIN-SUFFIX,ookla.com',
        ],
    },
}

root = Path('.')
(root/'custom'/'Loon').mkdir(parents=True, exist_ok=True)
(root/'custom'/'Clash').mkdir(parents=True, exist_ok=True)

for name, data in collections.items():
    (root/'custom'/'Loon'/f'{name}.lsr').write_text('\n'.join(data['loon'])+'\n', encoding='utf-8')
    (root/'custom'/'Clash'/f'{name}.yaml').write_text('payload:\n' + '\n'.join(f'  - {x}' for x in data['clash']) + '\n', encoding='utf-8')
