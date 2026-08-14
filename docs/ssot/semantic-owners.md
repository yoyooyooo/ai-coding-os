# Semantic Owners

这里的 `Owner` 表示语义问题的 Authority，不等同于 package copy 的写入位置。本仓映射的 `skills/**` 内容是 Agent Kit admitted snapshot 的 outbound projection；八个 shared core Skill 接受 Synpraxis 与 SMIP 的候选增量，supporting `effect-server-module-design` 由 SMIP 独立 source group 供稿。package/release metadata 仍由本仓拥有。

## Package and experiment mapping

| Surface | Content Authority | Mapping boundary |
| --- | --- | --- |
| 八个 shared core Skill under `skills/**` | Synpraxis 与 SMIP 候选增量；Agent Kit accepted snapshot 负责采纳与分发 | outbound projection；不从本仓 mirror collect 正文 |
| `skills/architecture/effect-server-module-design/**` | SMIP 独立 strict tracked source；Agent Kit 负责采纳与分发 | supporting outbound projection；不扩大 shared core roster |
| `experiments/goal-proof/skill/**` | Goal Proof experiment | 独立 bidirectional mapping；不属于 Suite outbound ownership 或 Suite ZIP |
| package/release metadata | `ai-coding-os` | package-owned；不因此成为 Skill content Authority |

配置、PR 或 staged export 只证明候选关系。accepted package content 必须同时绑定 Agent Kit accepted commit 与精确 mirror commit；npm publication 另需 release evidence。`release/**` 在 release workflow 明确重生成前保持 historical pre-import evidence。

## Project-facing Owners

| Skill | Owns | Must not silently own | Local anchors |
| --- | --- | --- | --- |
| [`$product-definition`](../../skills/product/product-definition/SKILL.md) | user outcome, Accepted Meaning, product language, rules, permissions, Quality Boundary, scope, acceptance | source reality, implementation mechanism, runtime proof | **Outcome Before Requested Means.** **Requirements Are Learned, Not Mined.** **Prototype Learns; Tracer Grows.** |
| [`$docs-governance`](../../skills/governance/docs-governance/SKILL.md) | Current Home, routes, freshness, docs topology, naming, cleanup | domain meaning, fact writing, product decision | **One Scoped Meaning, One Current Home.** **Freshness Is Part of Meaning.** **Build Documentation In; Do Not Bolt It On.** |
| [`$evolvable-application-architecture`](../../skills/architecture/evolvable-application-architecture/SKILL.md) | final fact writer, governed use case, transactions, Ports, application source grammar, composition, consistency, migration | product acceptance, frontend interaction state, Effect API syntax | **One Fact, One Final Writer.** **Candidates Propose; Authorities Materialize.** **Composition Chooses; It Does Not Decide.** |
| [`$frontend-architecture`](../../skills/architecture/frontend-architecture/SKILL.md) | intent, proposal, remote projection, local interaction, URL, realtime continuity, frontend host | final product fact, backend transaction, Effect Runtime semantics | **Intent Is Not Fact.** **One State Role, One Owner.** **Optimism Needs Reconciliation.** |
| [`$effect-best-practices`](../../skills/architecture/effect-best-practices/SKILL.md) | Effect failure, Scope, resources, structured concurrency, Queue/Stream, Service/Layer/Runtime, installed API semantics | product meaning, fact authority, repository topology, application source grammar or module/package boundaries | **Scope Owns Lifetime.** **Structured Concurrency Leaves No Orphans.** **Timeout May Mean Unknown Outcome.** |
| [`$product-harness-system`](../../skills/harness/product-harness-system/SKILL.md) | runnability, dependency reality, observation, diagnosis, recovery evidence, regression placement | product meaning, fact writing, risk acceptance | **Observe Only What You Exercised.** **Find the First Wrong State.** **A Pass Is Not Product Acceptance.** |

## Supporting Skills

| Skill | Role | Boundary |
| --- | --- | --- |
| [`$ai-coding-os`](../../skills/router/ai-coding-os/SKILL.md) | 仅在问题真正模糊或跨域时提供薄 Owner Map | 不是入口门禁、任务状态机或编排器 |
| [`$ai-coding-os-evolution`](../../skills/meta/ai-coding-os-evolution/SKILL.md) | 维护知识投资组合、Portable Default、Instruction ablation、Skill independence 与 anti-Cargo-Cult 判断 | 不拥有项目产品/架构含义，不建立发布或评测 Workflow |
| [`$effect-server-module-design`](../../skills/architecture/effect-server-module-design/SKILL.md) | 将已定案的 application/Effect v4 决策投影为 earned Server Module source shape | 不拥有产品意义、final writer、package admission 或 Effect Runtime 语义；不是第九个 semantic Owner |

## Common relationships

```text
$product-definition <-> $docs-governance
  Accepted Meaning and its Current Home

$product-definition <-> $evolvable-application-architecture
  product rules and authoritative fact transitions

$product-definition <-> $frontend-architecture
  user-operable obligations and concrete frontend ownership

$evolvable-application-architecture <-> $frontend-architecture
  fact, projection, intent, acknowledgement, reconciliation

$evolvable-application-architecture <-> $effect-best-practices
  semantic capability and execution mechanism

$evolvable-application-architecture + $effect-best-practices -> $effect-server-module-design
  settled authority and Effect v4 semantics projected into earned module files

all Owners <-> $product-harness-system
  claimed property and observed reality

$docs-governance <-> all Owners
  routes, freshness, naming, and durable placement without taking over meaning
```

任何 Specialist 都可以成为第一入口。大型任务不自动需要全部 Skill；只加载能够改变当前判断的最小 Owner 集。
