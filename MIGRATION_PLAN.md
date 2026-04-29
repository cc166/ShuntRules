# ShuntRules 迁移方案：从 luestr fork 到独立同步

## 📊 当前状态
- **当前模式**：fork luestr/ShuntRules，自动同步上游
- **规则来源**：luestr/ShuntRules（iKeLee 规则）
- **GitHub Actions**：sync-upstream.yml（每天 03:19 UTC）

## 🎯 目标状态
- **新模式**：独立仓库，同步 dler-io + Code-Dramatist
- **规则来源**：
  1. dler-io/Rules（22 基础 + 44 Media = 66 Surge 规则）
  2. Code-Dramatist/Rule_Actions（3 Direct + 7 Proxy + 5 Reject = 15 规则）
- **总计**：81 项规则

## 📋 迁移步骤

### 1. 清理现有内容
- 删除 `mirror/` 目录（luestr 规则）
- 删除 `custom/` 目录（自定义规则）
- 删除 `docs/` 目录（luestr 文档）
- 删除 `scripts/` 目录（luestr 同步脚本）
- 保留 `.github/workflows/` 目录（稍后重写）
- 保留 `README.md`（稍后重写）

### 2. 创建新目录结构
```
ShuntRules/
├── surge/
│   ├── provider/          # dler-io 基础规则（22 项）
│   └── media/             # dler-io Media 规则（44 项）
├── clash/
│   ├── direct/            # Code-Dramatist Direct 规则（3 项）
│   ├── proxy/             # Code-Dramatist Proxy 规则（7 项）
│   └── reject/            # Code-Dramatist Reject 规则（5 项）
├── .github/workflows/
│   ├── sync-dler-io.yml   # 同步 dler-io/Rules
│   └── sync-code-dramatist.yml  # 同步 Code-Dramatist/Rule_Actions
├── README.md              # 新的规则列表文档
└── _sync_report.json      # 同步报告
```

### 3. 创建同步脚本

#### sync-dler-io.yml
- 同步频率：每天一次（UTC 03:00）
- 规则来源：https://github.com/dler-io/Rules/tree/main/Surge/Surge%203/Provider
- 目标目录：`surge/provider/` 和 `surge/media/`

#### sync-code-dramatist.yml
- 同步频率：每天一次（UTC 03:30）
- 规则来源：https://github.com/Code-Dramatist/Rule_Actions
- 目标目录：`clash/direct/`, `clash/proxy/`, `clash/reject/`

### 4. 删除 upstream remote
```bash
git remote remove upstream
```

### 5. 更新 README.md
- 说明新的规则来源
- 列出所有规则及其用途
- 提供 Raw 链接

## ⚠️ 风险与注意事项
1. **破坏性操作**：删除现有 mirror/ 和 custom/ 目录
2. **历史记录**：保留 Git 历史，但内容完全替换
3. **用户影响**：如果有人使用旧的 ShuntRules 链接，会失效
4. **备份建议**：迁移前创建完整备份

## 🔄 回滚方案
如果迁移失败，可以：
1. 恢复备份：`git reset --hard <backup_commit>`
2. 重新添加 upstream：`git remote add upstream https://github.com/luestr/ShuntRules.git`
3. 重新同步：`git fetch upstream && git merge upstream/main`
