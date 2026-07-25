# 文档网络

本目录按语义 Authority 组织项目知识和规范。它是多入口网络，不是阶段目录、阅读清单、工作流或执行状态树。

## Discovery Surfaces

Agent 可以从任意与当前 concern 相关的表面进入：

```text
问题或用户意图
code area / source symbol
canonical term / object / state
Product、SSoT、Standard、ADR、Architecture artifact
API/schema/test/Harness Result/runtime evidence
仓库 AGENTS.md、本文或任一 layer router
```

只沿当前 claim 相关的 Authority、Evidence、source 和 neighboring routes 探索；不要求经过统一根节点，也不要求预读所有 layer。

## By Question

| 问题 | 主要 Authority |
| --- | --- |
| 系统应该做什么 | accepted product/business decision 或 baselined requirement |
| 当前存在什么实现结构 | source、schema、migration、lockfile、generated artifact |
| 哪些行为被实际观察 | executed tests、Harness、runtime、release 或 operational Evidence |
| 共享术语、对象、状态或不变量是什么意思 | `docs/ssot/**` 与 accepted decision |
| 为什么这样决定 | Product Decision Record 或技术 ADR |
| 接口接受什么 | adopted protocol/schema 与 contract evidence |
| 当前结构与 owner 是什么 | `docs/architecture/**` 与源码事实 |
| 做到什么程度 | bounded Evidence、selected execution method 与 release evidence |

源码证明实现结构和静态属性；runtime、reachability、deployment 和 environment behavior 需要执行或观察 Evidence。它们不静默改写产品意图、共享事实或已采纳取舍。Execution status 不自动成为 Product、Docs 或 release Authority。

## By Authority

| Layer | Owns | Must Not Own |
| --- | --- | --- |
| `docs/product/**` | AI Coding OS 产品/方法论定位、用户价值、非目标 | 工程规则、执行状态 |
| `docs/ssot/**` | 当前事实、术语、不变量和核心边界 | Roadmap、历史讨论、workflow state |
| `docs/standards/**` | 可执行规则、命令、质量门和协作标准 | 产品愿景、未采纳提案 |
| `docs/adr/**` | 已采纳取舍、替代方案和后果 | 当前任务状态、完整 Standards |
| `docs/architecture/**` | 系统结构、模块关系、运行时与发布边界视图 | 覆盖 SSoT 或执行队列 |
| `docs/roadmap/**` | 迁移顺序、gate 和 Evidence links | tracker/Goal/ticket 状态副本 |
| `docs/review-plan/**` | 历史或当前 plan/proposal review ledger | Product、SSoT、Standards、ADR 或 completion Authority |
| `docs/interface-capabilities/**` | 项目级 InterfaceCapability trace | 产品事实、测试代码、execution state |
| `docs/product-harness/**` | 项目级 HarnessScenario、coverage、claim ceiling、Evidence refs | 用户能力语义、测试代码、workflow state |

Layer 可以省略；新增 layer、partition 或 identity 需要通过 `$docs-governance` 的 Earned Shape 判断。

## By Code Area

当前仓库主要 code areas：

| Code area | Knowledge / rules | Evidence |
| --- | --- | --- |
| `skills/**` | [Skill source layout](standards/skill-source-layout.md)、[Core Suite architecture](architecture/repository-layer-breakdown.md) | core Suite audit、Skill eval assets |
| `skills/governance/docs-governance/**` | [Docs Governance Standard](standards/docs-governance.md) | Docs self-check、scanner fixtures、Docs audit |
| `skills/preset/**` | Preset Skill-local profiles、schemas 和 golden fixture | Preset render/validate/golden checks |
| `packages/cli/**` | [Goal Proof experiment](../experiments/goal-proof/README.md) | Bun build/typecheck/tests |
| `experiments/goal-proof/**` | experiment Skill、schemas、dogfood history | experiment self-check、CLI tests |

这张表只路由，不复制 owning artifact 的内容。新增稳定 code area 时只在 discovery value 足够时增加条目。

## Core Suite And Experiment Boundary

核心 AI Coding OS source 见 [skills/README.md](../skills/README.md)。核心 Router 选择知识 owner，不选择 workflow。

Goal Proof 是共仓早期实验，位于 [experiments/goal-proof/README.md](../experiments/goal-proof/README.md)。它不属于核心 Skill roster、Router branch、Docs layer 或核心 Suite bundle；历史 dogfood 也不承担当前项目 Authority。

## Placement

```text
current product meaning       -> docs/product/**
current shared fact/term      -> docs/ssot/**
current executable rule       -> docs/standards/**
accepted technical tradeoff   -> docs/adr/**
current topology / owner view -> docs/architecture/**
future sequence / gate        -> docs/roadmap/**
interface capability trace    -> docs/interface-capabilities/**
Harness proof contract        -> docs/product-harness/**
execution state               -> repository-selected external or experimental method
implementation spec           -> root specs/** when the project uses it
```

Portable Skill output paths are defaults. Existing project Authority wins and prevents a parallel Current Home.

## Routes

- 产品定位：[product/README.md](product/README.md)
- 当前事实：[ssot/README.md](ssot/README.md)
- 可执行规则：[standards/README.md](standards/README.md)
- 文档治理：[standards/docs-governance.md](standards/docs-governance.md)
- Skill source layout：[standards/skill-source-layout.md](standards/skill-source-layout.md)
- 结构视图：[architecture/README.md](architecture/README.md)
- 已采纳决策：[adr/README.md](adr/README.md)
- 后续迁移：[roadmap/README.md](roadmap/README.md)
- 评审账本：[review-plan/README.md](review-plan/README.md)
- InterfaceCapability：[interface-capabilities/README.md](interface-capabilities/README.md)
- Product Harness：[product-harness/README.md](product-harness/README.md)
