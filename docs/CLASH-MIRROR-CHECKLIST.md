# Clash / OpenClash 成品镜像清单

以下是当前按 iKeLee `Clash_Sample_Config_By_iKeLee.yaml` 抽出来的“核心成品规则清单”。

## 原生核心 provider（建议优先镜像）

| 名称 | 上游链接 | 模板中用途 |
|---|---|---|
| LAN | https://kelee.one/Tool/Clash/Rule/LAN_SPLITTER.yaml | DIRECT |
| Direct | https://kelee.one/Tool/Clash/Rule/Direct.yaml | DIRECT |
| Proxy | https://kelee.one/Tool/Clash/Rule/Proxy.yaml | 兜底后备策略 |
| AI | https://kelee.one/Tool/Clash/Rule/AI.yaml | AI |
| TikTok | https://kelee.one/Tool/Clash/Rule/TikTok.yaml | TikTok |
| SpeedtestIntl | https://kelee.one/Tool/Clash/Rule/SpeedtestInternational.yaml | Speedtest国际 |
| Game | https://kelee.one/Tool/Clash/Rule/Game.yaml | 游戏选择 |
| Netflix | https://rule.kelee.one/Clash/Netflix.yaml | Netflix |
| ESET_China | https://kelee.one/Tool/Clash/Rule/ESET_China.yaml | DIRECT |

## 当前结论
- 这 9 个是最接近 iKeLee Clash 模板原生结构的“核心成品规则”。
- 如果目标是尽量保持和 iKeLee 成品一致，优先镜像这 9 个最合理。
- 其它像 Telegram / SocialMedia / GitHub / YouTube / Google / Apple / Microsoft / Steam / ForeignMedia 属于你自己加的增强分类，和 iKeLee Clash 样板不完全一一对应。

## 建议顺序
1. 先镜像上面这 9 个核心成品规则
2. 模板切到你自己的镜像链接
3. 再决定是否补镜像扩展分类
