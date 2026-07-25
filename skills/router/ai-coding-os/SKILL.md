---
name: ai-coding-os
description: Project knowledge-owner map for ambiguous or cross-cutting AI coding work.
disable-model-invocation: true
---

# AI Coding OS Router

Use this Router only as an Owner Map:

> **Router selects knowledge; Agent selects strategy.**

A route is an edge to relevant knowledge, not a reading, planning, or execution
sequence. Clear concerns go directly to their owner. Ambiguous or cross-cutting
concerns use the smallest owner set whose decision surfaces actually change.

## Owner Map

| Concern | Lead | Add only for a distinct decision surface |
| --- | --- | --- |
| Documentation Authority, Routes, Earned Shape, freshness, cleanup | `$docs-governance` | semantic owner of affected content |
| Product framing, source synthesis, business model, rules, permissions, acceptance | `$product-definition` | docs, architecture, interface, or proof owner |
| Shared vocabulary, guarded terms, Proof/Evidence/Harness/Eval contracts | `$ai-coding-os-suite-contracts` | owner named by the contract |
| Fact authority, use cases, transactions, ports, consistency, migration | `$evolvable-application-architecture` | ecosystem, frontend, Effect, or proof owner |
| Ordinary Rust application architecture projection | `$evolvable-application-architecture` | `$architecture-decision-system` only for cross-owner Health/Diff/IR |
| Cross-owner architecture conflict, ADIR, Current/Target reconciliation, Health, Diff | `$architecture-decision-system` | relevant semantic architecture owners |
| Frontend state, feature topology, Query/store/realtime | `$frontend-architecture` | interface or UI proof owner |
| Effect Service/Layer/Runtime/Scope/failure/concurrency | `$effect-best-practices` | surrounding architecture owner |
| Discover or adopt reusable project defaults | `$evolvable-application-preset` | `$docs-governance` for Home conflicts |
| Generate a settled Effect API slice | `$effect-api-app-kit` | architecture and Effect owners for unsettled decisions |
| Cross-surface Harness vocabulary and coverage | `$product-harness-system` | headless or UI proof owner |
| Headless command, fixture, replay, DB/restart proof | `$headless-product-harness` | fact-authority owner |
| Component, surface, or browser proof | `$ui-product-harness` | `$frontend-architecture` |
| Concrete frontend test lane | `$frontend-test-system` | `$ui-product-harness` for reusable proof design |
| User-facing capability and interaction trace | `$interface-capability-planning` | product, frontend, and proof owners |
| Skill behavior Eval, corpus, attribution, ablation, held-out gate | `$skill-evaluation-system` | domain Harness/evaluator owner |
| New Agent capability epoch, Suite-wide redesign, candidate release/rollback | `$ai-coding-os-evolution` | `$skill-evaluation-system` and affected semantic owners |

## Unknown Routing

Unknown is not one central domain. Route by the claim it can change:

```text
product meaning, workflow, state, rule, permission
  -> $product-definition

writer, transaction, consistency, port, migration, lifecycle
  -> applicable architecture owner; use $architecture-decision-system when cross-owner

document Current Home, target/future classification, stale route
  -> $docs-governance

actual source structure
  -> source plus applicable architecture owner

empirical behavior, retry, timeout, restart, browser or provider outcome
  -> Harness/Test owner

Skill behavior or evaluator quality
  -> $skill-evaluation-system

security, legal, privacy, production operations
  -> accountable external Authority
```

Do not create a global Unknown Registry or let one undecidable slice block
unrelated reversible work.

## Routing Decisions

Resolve only what the concern needs:

```text
concern             decision-bearing question
lead                semantic owner of that question
supporting owners   orthogonal decisions, not extra reviewers by default
project authority   adopted facts, rules, decisions, contracts, and evidence
material unknowns   only unknowns that can change the result
safe boundary       what can proceed before the next commitment
external boundary   accountable owner outside the Suite
```

One Lead is preferred. Multiple Leads are justified only when orthogonal
Authorities change. A supporting owner contributes a bounded decision or
artifact; it does not create a central workflow.

## Authority by Question

```text
what should it do             -> accepted product/business decision or requirement
what implementation exists    -> source, schema, migration, lockfile, generated artifact
what behavior was observed    -> executed tests, Harness, runtime, release, operations
what does a shared term mean  -> project SSoT or accepted decision
why was it decided            -> product decision record or technical ADR
what does an interface accept -> adopted protocol/schema and contract evidence
what is in progress/complete  -> selected execution method and release evidence
```

When adopted Authority conflicts with executable reality, expose stale docs,
implementation drift, unaccepted implementation, or Evidence gap. Do not rank
sources by recency alone and do not let source silently become intent.

## Source Takeover

Inherited business material and AI-generated source may require product,
documentation, architecture, and Harness owners. Select only applicable owners.
Source can prove implementation structure and static properties; executed or
observed Evidence is required for runtime/reachability claims; neither decides
accepted product intent.

## External Execution Methods

Trackers, ticketing Skills, release processes, and other execution systems stay
outside the Core roster. They may consume project Authority and bounded Evidence
while retaining decomposition, dependency, assignment, status, and completion.
They do not become Product, SSoT, ADR, Architecture, Contract, or documentation
Authority.

## Output

Default to a short natural-language route:

```text
Lead Owner and reason
necessary adjacent Owners
applicable Project Authority / Evidence
material unknown or external boundary
safe-to-proceed boundary when relevant
```

Emit structured data only for a real consumer. Durable state belongs to the
selected project, semantic, evidence, or execution owner.
