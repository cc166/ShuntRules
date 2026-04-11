# Upstream rule mirror

这个仓库会定时把 `luestr/ShuntRules` README 里能解析到的规则文件同步到本仓库：

- `mirror/Loon/*.lsr`
- `mirror/Clash/*.yaml`

## 作用
- 让模板优先使用你自己的规则链接
- 降低直接引用外部规则地址的依赖
- 方便后续把自定义合集和模板统一到一个规则源

## 更新方式
- 手动触发 workflow
- 每天自动同步一次

## Loon 规则补充来源

由于 `rule.kelee.one` 直接抓取经常被 Cloudflare 拦截，已补充采用可访问的 GitHub 上游仓库：
- `mihoyo-typ/KeleeOne`（Loon 分支）

当前已导入一批常用 `.lsr` 到你自己的仓库：
- `mirror/Loon/Anthropic.lsr`
- `mirror/Loon/Apple.lsr`
- `mirror/Loon/AppleTV.lsr`
- `mirror/Loon/Bahamut.lsr`
- `mirror/Loon/Claude.lsr`
- `mirror/Loon/Copilot.lsr`
- `mirror/Loon/Disney.lsr`
- `mirror/Loon/Emby.lsr`
- `mirror/Loon/Game.lsr`
- `mirror/Loon/Gemini.lsr`
- `mirror/Loon/GitHub.lsr`
- `mirror/Loon/Google.lsr`
- `mirror/Loon/GoogleFCM.lsr`
- `mirror/Loon/HBO.lsr`
- `mirror/Loon/Microsoft.lsr`
- `mirror/Loon/Netflix.lsr`
- `mirror/Loon/OpenAI.lsr`
- `mirror/Loon/PrimeVideo.lsr`
- `mirror/Loon/Speedtest.lsr`
- `mirror/Loon/Spotify.lsr`
- `mirror/Loon/Steam.lsr`
- `mirror/Loon/TikTok.lsr`
- `mirror/Loon/YouTube.lsr`
