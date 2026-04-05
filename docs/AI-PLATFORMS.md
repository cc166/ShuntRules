# AI / 大模型平台补充说明

这页用来补充说明：**截图里提到的很多 AI 平台，并不一定在上游仓库里都有单独规则项**。

## 已在上游中能明确找到的常见项
- Claude
- OpenAI
- Copilot
- GitHub
- Gemini
- Anthropic
- Jetbrains
- Vercel
- Nvidia
- BardAI
- aiXcoder

## 当前未在上游 README 中明确检索到单独规则名的项
下面这些名字，我目前没有在上游 README 里检索到明确的单独规则项：
- Meta AI
- Perplexity
- Mistral
- Grok
- Trae
- OpenRouter
- Groq
- Together
- Fireworks
- Hyperbolic
- Jina AI
- GPUStack
- VoyageAI
- Vertex AI
- Poe
- Cerebras
- Hugging Face AI
- TokenFlux
- Google Antigravity

## 这意味着什么
- 不是说这些平台一定不能用
- 而是上游仓库当前未必按这些名字单独提供规则项
- 更实际的做法是：
  1. 先用聚合规则，例如 `AI.lsr`
  2. 再补已经明确存在的单项规则，比如 Claude / OpenAI / Copilot / Gemini
  3. 其余平台按实际域名或后续上游更新再补

## 建议
如果你后面特别想补某个平台，我可以再继续：
- 检查该平台是否应归入现有规则
- 或为你的 fork 单独补一页“平台对应关系说明”
