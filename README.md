# AI Coding OS Skill Suite 0.5.0-experimental.1

这是一个面向 AI Coding Agent 的项目认知、决策与验证 Skill Suite 源码快照。

本快照同时包含：

- `skills/`：完整、分组维护的 Core Skill Suite；
- `docs/`：按 `$docs-governance` 收敛后的当前项目知识网络；
- `CHANGELOG.md`：本次能力纪元升级的变更摘要；
- `release/`：机械审计、清单、变更报告与校验值。

核心定位不是为 Agent 规定固定工作流，而是让项目本身成为一个可理解、可决策、可探测、可实施、可验证并可持续演进的环境。

```text
Agent-legible project, not Agent-scripted workflow
Strong invariants, weak choreography
Minimal context, maximal legibility
No silent material assumption
Evidence over confidence
Commitment-aware autonomy
Earned persistence
Preserve semantics; re-earn scaffolding
```

从 [docs/README.md](docs/README.md) 按当前问题进入；不要把文档索引理解为必读顺序。

## 交付边界

本包只声明源码、文档、Schema、Eval 合同和离线机械审计成立。它不声明已执行独立模型行为评测、真实项目迁移、生产运行或自动采纳自演进候选。
