---
name: product-definition
description: Clarify product outcomes and accepted meaning when a feature request may be only a means, sources conflict, roles/objects/states/rules/permissions/quality/acceptance are unclear, a prototype is mistaken for truth, or an accepted obligation must enter interface and engineering work.
---

# Product Definition

Product Definition owns what the product is supposed to mean. It turns business input, current implementation, user feedback, and observed behavior into a product model that an accountable authority can accept and revise. None of those inputs becomes product truth automatically.

```text
source / current behavior / observation  -> learning input
accountable decision                     -> accepted meaning
specification                            -> one expression of accepted meaning
implementation                           -> current executable reality
```

## Semantic anchors

- **Outcome Before Requested Means.** Treat the requested feature as one candidate way to improve a user result, not as the result itself.
- **Requirements Are Learned, Not Mined.** Product understanding changes through conversation, prototypes, Tracers, and real use.
- **Accepted Meaning Comes from Accountable Decision.** Source, current behavior, and observation are learning inputs until the responsible authority accepts meaning.
- **Quality Boundary Is Not Claim Ceiling.** Product and risk authority define what must be good enough; evidence defines only what can currently be claimed.
- **Prototype Learns; Tracer Grows.** A Prototype is disposable inquiry; a Tracer is a thin, real path intended to remain and expand.

## Core distinctions

- Understand the user outcome, context, and pain before accepting the requested feature as the solution.
- Requirements are a current learning model, not a fixed deposit extracted once.
- Product invariant, changeable policy, and operational configuration are different kinds of knowledge.
- A Quality Boundary is accepted by product/risk authority; evidence only determines the current claim ceiling.
- A Prototype is disposable learning; a Tracer is thin, real, and intended to grow.
- Product language should precede page, component, database, and framework vocabulary.

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| a requested feature has an unclear underlying outcome or success condition | [Outcome and accepted meaning](references/outcome-and-accepted-meaning.md) |
| documents, meetings, code, legacy behavior, and user feedback disagree | [Learning from sources and reality](references/learning-from-sources-and-reality.md) |
| terms, actors, objects, relationships, states, and invariants lack a stable model | [Product language and model](references/product-language-and-model.md) |
| the happy path is clear but time, concurrency, exceptions, recovery, and termination are not | [Workflow, state, and exceptions](references/workflow-state-and-exceptions.md) |
| rules, permissions, responsibility, quality, or metrics are buried in page descriptions | [Rules, permissions, quality, and metrics](references/rules-permissions-quality-and-metrics.md) |
| current scope, future candidates, Prototype, Tracer, MVP, or estimate are mixed together | [Scope, Prototype, Tracer, and estimation](references/scope-prototype-tracer-and-estimation.md) |
| an accepted obligation must become operable without prematurely choosing components or state libraries | [Interface obligations](references/interface-obligations.md) |
| it is unclear what the Agent may infer and what an accountable person must decide | [Decision boundaries and responsibility](references/decision-boundaries-and-responsibility.md) |
| the project needs a stable default product-document shape | [Default product knowledge shape](references/default-product-knowledge-shape.md) |
| concrete examples would help reframe a request or distinguish a POC from a product slice | [Product reframing examples](references/product-reframing-examples.md) |

These are independent knowledge surfaces, not product-definition phases.

## Minimum sufficient product model

For the current capability, make enough meaning discoverable to answer:

```text
who wants what outcome in which context
which product objects and states are real
which actions may change them
which rules and invariants must hold
who is responsible, who can see, who can act, and who can accept risk
how success, failure, waiting, recovery, and completion are perceived
what is in scope and explicitly out of scope
what feedback could invalidate the current understanding
```

The representation may be prose, a diagram, a table, an existing PRD, source-adjacent knowledge, or a project-owned schema. Do not create a second product DSL without real reuse, risk, or machine-consumer pressure.

## Portable default

When the project has no coherent product-document convention, use the homes and selective headings in [Default product knowledge shape](references/default-product-knowledge-shape.md). The default provides familiarity, not an obligation to fill every section or create one document per capability.

## Local agency

An Agent may infer reversible implementation detail from accepted meaning and project conventions. Temporary assumptions may support bounded work when visible and easy to invalidate. They must not silently expand scope, permissions, public promises, persistent data meaning, or trust boundaries.

If an external decision is required, isolate the affected rule or slice and continue unrelated reversible work. One unresolved product decision does not make the entire task impossible.

## Weak product understanding signals

- pages and components are specified before objects, states, and user obligations;
- current code is treated as intended behavior merely because it runs;
- one `status` represents business progress, approval, visibility, SLA, and archive state;
- permission is described only as button visibility;
- "fast", "stable", or "secure" has no condition, floor, or risk owner;
- a polished demo is treated as proof of real data, recovery, and authorization;
- the same decision has several peer owners across meeting notes, PRDs, code, and tests.

## Adjacent owners

- When product rules change fact writing, transactions, external capabilities, or migration, use `$evolvable-application-architecture`.
- When user-visible obligations require concrete query/store/realtime, route, or host ownership, use `$frontend-architecture`.
- When the question is what timeout, restart, browser, provider, or recovery behavior actually does, use `$product-harness-system`.
- When the question is where product knowledge is current and how it is discovered, use `$docs-governance`.

## Output principle

Use the smallest natural expression that supports the next real decision or implementation slice. Expose accepted meaning, critical assumptions, unresolved authority, quality/acceptance boundaries, portable defaults when needed, and adjacent implementation implications. Do not create a full PRD family, decision packet, RACI matrix, or trace matrix merely to demonstrate process.
