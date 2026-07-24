# SSoT

本层保存当前事实、术语和不变量。

## Owns

- 当前方法对象的权威含义。
- 顶层命名和字段语义。
- 不应被 Roadmap、Goal Pack 或 README 静默改写的事实。

## Must Not Own

- 迁移顺序、临时任务状态、历史讨论或未采纳提案。

## Boundary

ADR 解释采用原因；Standards 规定执行方式；Roadmap 记录未来顺序；所选执行方法记录
运行状态和证据。代码与测试能证明实际行为，不能静默重定义本层事实。

## Promotion / Demotion

- 从 ADR、完成证据或 Roadmap gate 中抽取稳定事实时 promote 到本层。
- 迁移计划、历史解释和执行状态分别 demote 到 Roadmap、ADR、source/report 或执行方法。
- 废弃事实从当前口径移除；追溯依赖 Git history 或明确历史材料。

## 当前事实

- 本仓是 AI Coding OS 方法套件、grouped Skill source 和 `goal-proof` CLI 源码仓。
- 默认落地边界是 workspace/repo。
- `$ai-coding-os` 是 user-invoked 薄路由，只选择知识和 execution surface，不拥有 durable artifact。
- `$ai-coding-os-suite-contracts` 是可独立安装的跨 Skill precedence/handoff、共享词汇、文件模式和 Harness schema owner；它不保存静态 Skill 清单。
- 项目 `AGENTS.md`、SSoT、Standards、ADR、contracts、源码和可执行证据优先于 Preset 与通用 Skill 默认值。
- `$docs-governance` 拥有 docs layer、AGENTS.md entry、authority placement、cleanup 和 audit。
- `$evolvable-application-architecture` 拥有 authority-first doctrine、事务、Capability Port / Adapter、composition root、Monorepo/source topology、迁移与可替换性。
- `$frontend-architecture` 拥有前端状态、feature topology、host composition、contract evolution 和 realtime reconciliation。
- `$effect-best-practices` 拥有 Effect Service/Layer/Scope/runtime、错误通道、资源生命周期和版本映射。
- `$interface-capability-planning` 拥有 UI/IA 能力合同、surface、状态/数据归属与 proof handoff。
- `$product-harness-system` 拥有共享 Harness 词汇、descriptor/result、coverage、claim ceiling 与 lifecycle。
- `$headless-product-harness`、`$ui-product-harness` 和 `$frontend-test-system` 分别拥有 headless、UI 和具体前端 test lane。
- `$evolvable-application-preset` 是 Agent-guided 可复用默认来源；可按 surface 增量采用，应用后项目 resolved docs 与 AGENTS.md 成为当前权威。
- `$effect-api-app-kit` 只实例化已确定的 Change Spec；结构验证不能替代项目真实编译或行为证据。
- `$goal-proof` 是显式选择的可选执行方法；任务复杂度本身不触发 Goal Pack。
- CLI/npm package 继续使用 `goal-proof`。
- Goal Pack v2 主路径为 `goal.yaml`、`progress.yaml`、`evidence.jsonl` 和按需存在的 `plans/<work_id>.md`。
- Goal Pack ready 需要稳定 contract 与能在 `claim_limit` 内产出或检查 required evidence 的 `proof_step`。
- Evidence 结论不得超过实际执行或检查的 surface；相邻面用 `not_claimed`、叙事性 `not_proven` 或 remaining gaps 表达。
- 真实 `evidence.jsonl` 保持 append-only。
- 路由分支只在 `$ai-coding-os` 中维护；跨 Skill 合同按 `$ai-coding-os-suite-contracts` 发现，不使用 sibling path。
- 本仓只维护 grouped Skill source，不生成 Flat 版本；每个 Skill 必须兼容独立、重排或扁平安装。

## Authority Resolution

Authority is claim-scoped rather than one universal file order:

```text
host instructions and repository AGENTS.md
  -> adopted project authority for the claim
     current facts -> docs/ssot/**
     executable rules -> docs/standards/**
     accepted tradeoffs -> docs/adr/**
     wire compatibility -> project protocol/schema contract
  -> executable reality for implementation claims
     source, lockfiles, tests, command evidence
  -> unadopted Preset source/candidate
  -> specialist doctrine and router recommendation
```

An adopted Preset output belongs to its project docs layer. It is not a second
Preset authority. If project authority and executable reality disagree, record a
stale-doc or implementation-drift conflict; do not silently rank one away.

## Read Next

- 执行规则：`../standards/README.md`
- 文档治理：`../standards/docs-governance.md`
- Skill source layout：`../standards/skill-source-layout.md`
- 文档路由：`../README.md`
