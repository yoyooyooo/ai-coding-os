# Product

本层描述 AI Coding OS 的产品与方法论定位。

## Owns

- AI Coding OS 服务的工作场景与用户价值。
- grouped Skill Suite、薄 Router、项目权威、Preset 和可执行验证面的关系。
- 适用边界与非目标。

## Must Not Own

- CLI 具体实现。
- Goal Pack 当前状态。
- checker 规则细节。
- 未采纳迁移计划。

## Boundary

本层回答 AI Coding OS 解决什么问题、各方法为何存在，以及默认落地边界。
Schema、命令、源码布局规则和执行结果分别属于 Standards、实现和证据。

## Promotion / Demotion

- 稳定定位、用户价值和非目标可从 README、ADR 或完成证据 promote 到本层。
- 可执行规则 demote 到 Standards；结构关系 demote 到 Architecture；状态和 gate
  demote 到 Roadmap 或所选执行方法。

## 当前定位

AI Coding OS 是面向 repository/workspace 工作的 AI coding 方法与 Skill Suite。
它提供：

```text
薄用户路由
项目文档权威与生命周期治理
可演进的应用、前端和 Effect 架构 doctrine
界面能力与 Product Harness 规划
可选的 Goal Pack 长期执行方法
可复用 Preset 与确定性生成工具
```

核心原则是约束 durable system semantics，并让实际执行策略由当前任务、项目权威和
可用验证面决定。结构化 artifact 只在改善执行、验证、审计、交接或 claim 诚实时存在。

## 套件构成

| Skill | 作用 |
| --- | --- |
| `$ai-coding-os` | 用户显式入口；为跨域或不明确工作选择 Lead/Supporting Skill |
| `$ai-coding-os-suite-contracts` | 可独立安装的跨 Skill precedence/handoff、共享词汇和 Harness schemas |
| `$docs-governance` | 文档层、AGENTS.md、SSoT、Standards、ADR、Roadmap 的治理 |
| `$evolvable-application-architecture` | 事实权威、事务、模块、端口、组合根、源码拓扑与演进 |
| `$frontend-architecture` | 前端状态权威、feature topology、host composition 与 realtime reconciliation |
| `$effect-best-practices` | Effect Service/Layer/Scope/runtime 与版本映射 |
| `$interface-capability-planning` | UI/IA 能力、surface、交互状态和 testability handoff |
| `$product-harness-system` | 跨 Headless/UI 的 Harness 共享语言、coverage 与 lifecycle |
| `$headless-product-harness` | capability command、fixture/replay、DB/restart 与 boundary proof |
| `$ui-product-harness` | interface-headless、render wiring 与 browser-visible proof |
| `$frontend-test-system` | 具体前端 test lane 和 runner 选择 |
| `$evolvable-application-preset` | 发现现有权威并选择性采用可复用默认值，形成项目拥有的 snapshot |
| `$effect-api-app-kit` | 从已确定 Change Spec 原子生成 Effect API capability slice |
| `$goal-proof` | 显式采用时的 Goal Pack 目标、证据和跨会话延续方法 |

一轮内可完成且有明确证据路径的工作直接实施。只有用户明确选择 Goal Proof/Goal
Pack，或仓库将其声明为当前 workstream 方法时，才进入 `$goal-proof`。

## Read Next

- 根 README：`../../README.zh-CN.md`
- 当前事实：`../ssot/README.md`
- 执行规则：`../standards/README.md`
- 文档治理：`../standards/docs-governance.md`
