---
name: ai-coding-os
description: Use only when an AI-coding concern is genuinely ambiguous, cross-domain, or difficult to assign to a specialist owner. Provides a thin semantic map; any specialist Skill may be the first entry.
disable-model-invocation: true
---

# AI Coding OS

This is a map legend, not a gate, reading order, or execution plan.

> **Route Is an Edge, Not a Sequence.** A route exposes relevant knowledge; it is not a stage the task must pass through.

## Semantic anchors

- **Project Authority First.** Accepted project meaning and direct evidence outrank portable guidance and model guesswork.
- **Source Is Not Decision.** Source can reveal drift or implementation reality, but cannot silently accept product or architecture intent.
- **Evidence Bounds Claims.** An observation supports only the property and path it actually exercised; it cannot accept quality or residual risk.
- **Route Is an Edge, Not a Sequence.** Enter through the node closest to the current question and follow only relationships that can change the judgment.
- **Local Agency, Bounded Authority.** The Agent owns reversible local choices, not silent changes to accepted meaning, durable data, permissions, public contracts, or material risk.
- **Portable Defaults Standardize the Boring Choices.** When the project is silent, use the owning Skill's default before inventing another dialect.

## Project-facing owners

| The current question changes... | Owner |
| --- | --- |
| user outcomes, accepted product meaning, scope, rules, permissions, quality, or acceptance | `$product-definition` |
| where project knowledge is current, how it is found, when it becomes stale, or whether a new documentation shape is justified | `$docs-governance` |
| who writes persistent facts, how use cases and transactions form, how external capabilities are isolated, or how implementations migrate | `$evolvable-application-architecture` |
| user intent, remote projection, local interaction state, URL, query/store/realtime ownership, or frontend host composition | `$frontend-architecture` |
| Effect-specific failure, Scope, resource, concurrency, Runtime, or installed-version semantics | `$effect-best-practices` |
| how a property is run, observed, reproduced, diagnosed, and protected by the lowest correct regression layer | `$product-harness-system` |

Choose the smallest owner set. A large task does not automatically require every Skill.

## Common adjacent relationships

```text
$product-definition
  <-> $docs-governance
      accepted meaning and its Current Home

$product-definition
  <-> $evolvable-application-architecture
      product rules and authoritative fact transitions

$product-definition
  <-> $frontend-architecture
      user-operable obligations and concrete frontend ownership

$evolvable-application-architecture
  <-> $frontend-architecture
      fact, projection, intent, acknowledgement, and reconciliation

$evolvable-application-architecture
  <-> $effect-best-practices
      semantic capability and Effect execution mechanism

all owners
  <-> $product-harness-system
      claimed properties and observed reality

$docs-governance
  <-> all owners
      routes, freshness, naming, and durable placement without taking over meaning
```

## Authority legend

```text
what should it do?            -> accepted product/business/policy authority
what implementation exists?   -> source, schema, configuration, dependency lockfile
what happened this time?       -> executed test, runtime, browser, provider, operations
what does a shared term mean?  -> project glossary, SSoT, or accepted semantic decision
why was this choice accepted?  -> applicable product or technical decision
what is still unknown?         -> the owner whose decision could change because of the unknown
```

Source may challenge stale knowledge, but it does not silently become accepted intent. Evidence limits a claim; it does not accept quality or residual risk.

## Local agency boundary

An Agent should make reversible, local choices that preserve accepted semantics and the project's adopted conventions. Escalate only when the decision changes product meaning, public compatibility, persistent data semantics, permissions, irreversible external effects, or acceptance of material risk.

## Portable defaults

When a project is silent, follow the owning Skill's invariant and default references. A coherent project override remains authoritative; use `$ai-coding-os-evolution` when a portable default itself needs admission, revision, or retirement.

## Response principle

Enter through the owner closest to the current symptom. Expose only the authority, assumptions, tradeoffs, observations, defaults, and adjacent knowledge that can change the current judgment. Do not manufacture a cross-Skill handoff protocol or turn this map into an orchestrator.
