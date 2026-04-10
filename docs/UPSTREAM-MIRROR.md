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
