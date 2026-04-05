# AI 平台映射与取用建议

这页把你截图里常见的平台名，尽量映射到**当前上游已能明确找到的规则项**，或给出更稳妥的取用方式。

## 1. 可直接对应到现有规则的

| 平台名 | 建议对应规则 | 备注 |
|---|---|---|
| OpenAI | OpenAI | 可直接用单项规则 |
| Copilot | Copilot | 可直接用单项规则 |
| GitHub Models | GitHub | 当前更适合归到 GitHub |
| Gemini | Gemini | 可直接用单项规则 |
| Anthropic | Anthropic | 可直接用单项规则 |
| JetBrains AI | Jetbrains | 名称不同，规则项是 `Jetbrains` |
| Nvidia AI | Nvidia | 可直接用单项规则 |
| Claude | Claude | 可直接用单项规则 |
| Vercel AI | Vercel | 当前更适合归到 `Vercel` |
| Google Antigravity | Google / Gemini / BardAI | 上游暂无同名单项，先按 Google 生态处理 |

## 2. 建议先用 AI 聚合规则的

下面这些平台，当前更建议：**先用聚合规则，再按需要补单项**。

- Meta AI
- Perplexity
- Mistral / Mistral AI
- Grok AI
- Trae AI
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
- Cerebras AI
- Hugging Face AI
- TokenFlux

### 推荐做法
1. 先使用聚合规则：`AI.lsr`
2. 再补已存在的单项规则：
   - OpenAI
   - Claude
   - Copilot
   - Gemini
   - Anthropic
   - GitHub
   - Vercel
   - Nvidia
3. 如果后续上游新增了更细平台规则，再继续补进来

## 3. 你现在最实用的 AI 组合

### 精简组合
- OpenAI
- Claude
- Copilot
- Gemini
- Anthropic

### 开发 / AI 组合
- GitHub
- Copilot
- OpenAI
- Claude
- Gemini
- Vercel
- Nvidia

### 聚合优先组合
- AI.lsr
- 再补 OpenAI / Claude / Copilot / Gemini

## 4. 说明
- 这页是 fork 补充说明，不是上游官方规则目录
- 具体可点击链接，优先看 `docs/CATEGORIES.md`
- 上游未来新增平台规则后，可以继续扩充这张映射表
