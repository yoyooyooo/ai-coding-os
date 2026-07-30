# Semantic Owners

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

all Owners <-> $product-harness-system
  claimed property and observed reality

$docs-governance <-> all Owners
  routes, freshness, naming, and durable placement without taking over meaning
```

任何 Specialist 都可以成为第一入口。大型任务不自动需要全部 Skill；只加载能够改变当前判断的最小 Owner 集。
