# ProxyResource 上游分类清单

以下分类已在 `ProxyResource/Resource/Markdown/Rule/README.md` 中确认存在真实上游链接，并指向 `yuumimi/rules`：

| 分类 | Loon | Clash |
|---|---|---|
| telegram | https://raw.githubusercontent.com/yuumimi/rules/release/loon/telegram.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/telegram.txt |
| discord | https://raw.githubusercontent.com/yuumimi/rules/release/loon/discord.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/discord.txt |
| whatsapp | https://raw.githubusercontent.com/yuumimi/rules/release/loon/whatsapp.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/whatsapp.txt |
| signal | https://raw.githubusercontent.com/yuumimi/rules/release/loon/signal.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/signal.txt |
| line | https://raw.githubusercontent.com/yuumimi/rules/release/loon/line.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/line.txt |
| twitter | https://raw.githubusercontent.com/yuumimi/rules/release/loon/twitter.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/twitter.txt |
| instagram | https://raw.githubusercontent.com/yuumimi/rules/release/loon/instagram.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/instagram.txt |
| facebook | https://raw.githubusercontent.com/yuumimi/rules/release/loon/facebook.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/facebook.txt |
| reddit | https://raw.githubusercontent.com/yuumimi/rules/release/loon/reddit.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/reddit.txt |
| github | https://raw.githubusercontent.com/yuumimi/rules/release/loon/github.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/github.txt |
| youtube | https://raw.githubusercontent.com/yuumimi/rules/release/loon/youtube.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/youtube.txt |
| netflix | https://raw.githubusercontent.com/yuumimi/rules/release/loon/netflix.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/netflix.txt |
| tiktok | https://raw.githubusercontent.com/yuumimi/rules/release/loon/tiktok.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/tiktok.txt |
| google | https://raw.githubusercontent.com/yuumimi/rules/release/loon/google.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/google.txt |
| apple | https://raw.githubusercontent.com/yuumimi/rules/release/loon/apple.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/apple.txt |
| microsoft | https://raw.githubusercontent.com/yuumimi/rules/release/loon/microsoft.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/microsoft.txt |
| steam | https://raw.githubusercontent.com/yuumimi/rules/release/loon/steam.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/steam.txt |
| speedtest | https://raw.githubusercontent.com/yuumimi/rules/release/loon/speedtest.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/speedtest.txt |
| disney | https://raw.githubusercontent.com/yuumimi/rules/release/loon/disney.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/disney.txt |
| spotify | https://raw.githubusercontent.com/yuumimi/rules/release/loon/spotify.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/spotify.txt |
| bahamut | https://raw.githubusercontent.com/yuumimi/rules/release/loon/bahamut.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/bahamut.txt |
| category-entertainment@!cn | https://raw.githubusercontent.com/yuumimi/rules/release/loon/category-entertainment@!cn.txt | https://raw.githubusercontent.com/yuumimi/rules/release/clash/category-entertainment@!cn.txt |

## 同步建议
- 这些链接能作为你自建镜像脚本的真实输入源
- 但当前环境直连 `raw.githubusercontent.com` 不稳定
- 如果要同步进你自己的仓库，建议用 GitHub Actions 在线拉取并提交
- 模板层面：优先引用你自己的镜像链接，镜像失败时再回退上游
