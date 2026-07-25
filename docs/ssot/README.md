# SSoT

## Owns

- AI Coding OS 0.5.0-experimental.1 的当前 Suite 身份、核心 Doctrine 和 Skill Owner Map。
- Architecture Decision IR、Skill evaluation 和 Suite evolution 的当前边界。
- 不应被旧 ADR、Preset candidate、源码偶然形态或点时报告静默改写的事实。

## Must Not Own

- 单个项目的业务 SSoT、执行状态、未来路线或模型运行结果。

## Current Facts

### Suite Identity

- 当前完整快照版本为 `0.5.0-experimental.1`；Core Skill 版本由 [`skills/VERSION`](../../skills/VERSION) 声明。
- Canonical source 只维护 grouped layout，不生成 Flat 副本；目录服务维护，不是运行时合同。
- `$ai-coding-os` 是 user-invoked Owner Map，只路由知识 Owner，不保存项目状态或控制 Agent loop。
- 轻量入口、强 Route、Skill-local References、Tools 和 Evidence 共同实现 Progressive Disclosure。

### Core Doctrine

```text
Project Authority First
Question-scoped Ownership
One Scoped Meaning, One Current Home
Source Is Not Decision
No Silent Material Assumption
Evidence Bounds Claims
Route Is an Edge, Not a Sequence
Strong Invariants, Weak Choreography
Minimal Context, Maximal Legibility
Earned Persistence
Preserve Semantics; Re-earn Scaffolding
```

### Skill Owners

| Concern | Lead Owner |
| --- | --- |
| 跨域或不明确的知识路由 | `$ai-coding-os` |
| 最小共享术语、Proof/Evidence/Harness Schema | `$ai-coding-os-suite-contracts` |
| Docs Authority、Routes、Earned Shape、freshness | `$docs-governance` |
| 产品模型、矛盾、模糊点、要求与验收 | `$product-definition` |
| 跨语言 authority-first 应用架构 | `$evolvable-application-architecture` |
| 跨架构 Owner 的 ADIR、冲突、Diff 与 Health | `$architecture-decision-system` |
| 前端状态、投影、交互和 host 边界 | `$frontend-architecture` |
| Effect Service、Layer、Runtime、Scope 与 typed failure | `$effect-best-practices` |
| InterfaceCapability 规划 | `$interface-capability-planning` |
| 共享、Headless、UI 和 frontend test Proof | Harness/Test Skills |
| 可复用候选默认与 Profile 组合 | `$evolvable-application-preset` |
| 已确定 Change Spec 的确定性实例化 | `$effect-api-app-kit` |
| Skill 行为评估、Ablation 与 held-out Gate | `$skill-evaluation-system` |
| Agent Capability Epoch 下的 Suite 重标定与发布候选 | `$ai-coding-os-evolution` |

### Architecture

- `$evolvable-application-architecture` 是跨语言语义内核；TypeScript、Frontend、Effect、Rust 和 repository topology 是独立投影。
- Rust 当前由 EAA 的 Rust Projection 和 Preset `rust` Profile 承载；尚未晋升为独立 Skill。
- `application-core`、`monorepo-core`、`typescript-node` 和 `rust` 是相互独立的 Preset Profile；TypeScript 不隐含 Monorepo，Rust 也不继承 `.ts` 文件名。
- ADIR 是当前问题即时构建的局部、部分、decision-bearing graph。它默认临时存在，只在跨 Agent、长期迁移、多生态一致性、持续 Health/Diff 或机器消费压力下 Earn 持久化。
- Decision tree 是 owner-scoped rule forest 针对当前问题的局部投影，不是全局固定流程。

### Unknown And Autonomy

- Unknown 是否阻塞取决于影响、可逆性、决定权、证据路径和 Commitment Boundary，而不是“未知”这个标签本身。
- Decision readiness 分为 Exploration、Reversible Implementation、Commitment Closure 和 Claim Closure。
- Autonomy Envelope 是复杂 Slice 的可选投影，不是每个任务的必填模板。
- Unknown 没有中央 Owner；产品、架构、经验、文档、安全等未知回到相应语义或外部 Authority。

### Evidence And Evolution

- `observed`、`supports`、`does_not_decide`、`not_proven` 与 `claim_ceiling` 保持非等价。
- Harness 可以关闭经验 Unknown，但不能替产品或架构 Owner 做决定。
- Skill 失败必须先归因；execution lapse、routing/retrieval/tool/evaluator defect 和 noise 不得自动转成新的 Canonical 指令。
- Skill evaluation 使用 Discovery/Train、Selection、Sealed Release Test 和 Transfer/Canary 分层，并按 case family 防止语义泄漏。
- Suite evolution 可以自主形成候选，但不能循环自证或自动发布；新模型发布只是 Capability Probe trigger。
- Canonical Suite 优先面向声明的 Agent Capability Baseline；兼容脚手架在真实压力下以 Overlay 形式 Earn，不污染稳定语义内核。

## Claim Ceiling

当前源码与离线审计可以证明结构、链接、Schema、Eval 合同、Preset fixture、Docs routes 和发布 provenance。未运行独立模型行为 Eval、SkillOpt 训练、真实 Rust 项目迁移、真实 Adapter、生产运行或自动采纳验证时，这些结论保持 `not_proven`。

## Routes

- [Core Doctrine](core-doctrine.md)：慢变语义宪法的详细 Current View。
- [产品定位](../product/README.md)
- [架构](../architecture/README.md)
- [标准](../standards/README.md)
- [决策](../adr/README.md)
- [点时报告](../reports/README.md)
