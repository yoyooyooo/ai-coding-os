# AI Coding OS Repository Guide

本仓库维护 AI Coding OS Core Skill Suite 与其当前项目 Docs。

## Knowledge Surfaces

- [文档网络](docs/README.md)
- 当前定位与用户价值：`docs/product/README.md`
- 当前事实与 Skill Owner：`docs/ssot/README.md`
- 当前结构：`docs/architecture/README.md`
- 约束与发布门：`docs/standards/README.md`
- 决策原因：`docs/adr/README.md`
- 未来候选：`docs/roadmap/README.md`
- 点时审计：`docs/reports/README.md`
- Skill 源码入口：`skills/README.md`

这些路径是并列 Route，不是强制阅读顺序。明确问题直接进入 owning Skill；跨 Owner 或意图含混时使用 `$ai-coding-os`。

## Working Rules

- Project Authority First；Skill、Preset 和已有源码都不能静默覆盖项目 Current Home。
- 不把足以改变结果的 material unknown 静默转为实现假设。
- 普通可逆技术选择由 owning Agent/Skill 自主完成；产品语义、权限、公共兼容性、持久数据和不可逆外部行为遵守相应 Stop Line。
- Source 证明实现结构；运行、迁移、真实 Adapter 和生产行为必须由匹配的 Evidence 支持。
- 新文档、目录、Schema、Registry、IR 持久化和 Workflow 都必须在真实压力下 Earn。

## Verification

```bash
python3 skills/tooling/suite_audit.py --suite skills --out release/suite-audit.json
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo . --readability
```

未运行独立模型行为评测、真实 Rust 迁移或生产验证时，不得声称这些层面已经成立。
