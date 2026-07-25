---
name: ai-coding-os
description: Project knowledge-owner map for ambiguous or cross-cutting AI coding work.
disable-model-invocation: true
---

# AI Coding OS Router

Use this router as an Owner Map:

> **Router selects knowledge; Agent selects strategy.**

A route is an edge to relevant knowledge, not a reading, planning, or execution
sequence. Clear concerns go directly to their owner. Ambiguous or cross-cutting
concerns use the smallest set of owners whose decision surfaces actually change.

## Owner Map

| Concern | Lead | Add only for a distinct decision surface |
| --- | --- | --- |
| Documentation Authority, Routes, Earned Shape, lifecycle, cleanup | `$docs-governance` | semantic owner of affected content |
| Product framing, requirements, business model, decisions, acceptance | `$product-definition` | documentation, architecture, interface, or proof owner |
| Shared Suite vocabulary, Proof Surface, Evidence Envelope, eval schema | `$ai-coding-os-suite-contracts` | owner named by the contract |
| Fact authority, transactions, backend modules, migration | `$evolvable-application-architecture` | frontend, Effect, or proof owner |
| Monorepo, package promotion, source topology, semantic naming | `$evolvable-application-architecture` | `$evolvable-application-preset`, `$docs-governance` |
| Frontend state, feature topology, Query/store/realtime | `$frontend-architecture` | `$ui-product-harness` |
| Effect Service/Layer/Scope/runtime/API | `$effect-best-practices` | surrounding architecture owner |
| Discover or adopt reusable project defaults | `$evolvable-application-preset` | `$docs-governance` for Home conflicts |
| Generate a settled Effect API slice | `$effect-api-app-kit` | architecture and Effect owners for unsettled decisions |
| Cross-surface Harness vocabulary and coverage | `$product-harness-system` | headless or UI proof owner |
| Headless command, fixture, replay, DB/restart proof | `$headless-product-harness` | fact-authority owner |
| Component, surface, or browser proof | `$ui-product-harness` | `$frontend-architecture` |
| Concrete frontend test lane | `$frontend-test-system` | `$ui-product-harness` for reusable proof design |
| User-facing capability and interaction trace | `$interface-capability-planning` | product, frontend, and proof owners |

## Routing Decisions

Resolve only what the current concern needs; no ordering is prescribed.

```text
concern             semantic decision surface that may change
lead                owner of that surface
supporting owners   orthogonal decisions, not extra reviewers by default
project authority   current adopted facts, rules, decisions, contracts, evidence
available surfaces  existing Preset, generator, Harness, command, or test entry
external boundary   security, legal, policy, operations, or execution owner outside Suite
```

One Lead is preferred. Multiple Leads are justified only when the request
changes orthogonal Authorities. A supporting owner contributes a bounded
decision or artifact; it does not create a central workflow.

## Source Takeover Coverage

When inherited business material and AI-generated source must be understood
together, select any relevant rows. This is a coverage map, not a recipe.

| Concern | Knowledge owner | Bounded contribution |
| --- | --- | --- |
| Conflicting business sources and accepted intent | `$product-definition` | source synthesis, product decisions, requirements, acceptance, gaps |
| Current/target/future placement and retained evidence | `$docs-governance` | one documentation Authority per meaning and discoverable Routes |
| Backend facts, writers, transactions, APIs, persistence | `$evolvable-application-architecture` | current authority map and migration pressure |
| Routes, projections, Query/store/realtime, host composition | `$frontend-architecture` | frontend ownership and reconciliation map |
| Installed or settled Effect use | `$effect-best-practices` | version-correct runtime and resource constraints |
| Existing and missing proof surfaces | Harness/Test owners | bounded observations, claim ceilings, and `not_proven` |
| Security, privacy, legal, compliance, operations | accountable external owner | explicit unresolved boundary; no Suite proxy decision |

Useful project outputs may include a Current Implementation Map, an Observed
Behavior Map when executed Evidence exists, Implementation-to-Authority Gaps,
an API/Page/Table map, proof inventory, migration risk, or a
retain/refactor/rewrite/retire decision. Keep them inline unless durable project
value earns an artifact.

> **Source can evidence current implementation structure and static properties.
> Executed or observed Evidence is required for runtime, reachability,
> deployment, or environment behavior. Neither decides accepted product
> intent.**

## Authority by Question

```text
what should it do             -> accepted product/business decision or requirement
what implementation exists    -> source, schema, migration, lockfile, generated artifact
what behavior was observed    -> executed tests, Harness, runtime, release, operations
what does a shared term mean  -> project SSoT or accepted decision
why was it decided           -> product/business decision record or technical ADR
what does an interface accept -> adopted protocol/schema and contract evidence
what is in progress/complete -> repository-selected execution method and release evidence
```

Host instructions and repository policy constrain all owners. When adopted
Authority conflicts with executable reality, expose stale docs, implementation
drift, or an unaccepted implementation; do not silently rank the conflict away.

## External Execution Methods

Trackers, ticketing Skills, release processes, and other selected execution
systems are outside the core roster. When explicitly selected, they may consume
project Authority and bounded Evidence while retaining their own decomposition,
dependency, assignment, status, and completion lifecycle.
They do not become Product, SSoT, ADR, Architecture, Contract, or documentation
Authority.

## Output

Default to a short natural-language answer containing only:

```text
Lead Owner and reason
necessary adjacent Owners for distinct decision surfaces
applicable Project Authority and Evidence
uncovered external boundary
```

Emit structured YAML only when the user or an actual machine consumer requests
it. Keep routing inline. Durable state belongs to the selected project or
execution owner.
