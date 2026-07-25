---
name: architecture-decision-system
description: >-
  Composes local architecture decisions across semantic owners. Use when
  current, target, source, and evidence disagree; multiple architecture Skills
  must be reconciled; material ambiguity or false-known risk affects a design;
  an Architecture Decision IR, architecture diff, commitment boundary, or
  evidence-bounded health assessment is needed.
---

# Architecture Decision System

Build the smallest architecture decision model needed for the current question.
Do not create a central architecture database merely because structured output is
possible.

```text
ADIR                    a local, decision-bearing reference graph
Decision calculus       owner-scoped rules applied to the current question
Decision tree           a temporary projection of relevant rules
Architecture health     a derived comparison of claims, source, rules, evidence, and time
```

The durable project Authorities remain where the project already owns them.
ADIR connects those Authorities; it does not replace them.

## Ownership

```text
Owns:
  local Architecture Decision IR construction and reconciliation
  architecture Conflict / Ambiguity / Gap / Assumption / Drift modeling
  cross-owner decision composition and concise Decision Trace
  current / accepted-target / future architecture comparison
  Map–Territory reconciliation and Architecture Diff
  commitment boundaries and optional Autonomy Envelopes
  evidence-bounded Architecture Health derivation
  earned persistence and projection of architecture decision models

Adjacent Suite owners, when installed:
  product meaning, tacit expectations, requirements, acceptance -> $product-definition
  fact authority, use cases, transactions, ports, migration -> $evolvable-application-architecture
  frontend state, projection, realtime, host composition -> $frontend-architecture
  Effect Service, Layer, Runtime, Scope, failures -> $effect-best-practices
  documentation Current Home and lifecycle -> $docs-governance
  empirical probes and claim ceilings -> $product-harness-system and specialist Harness Skills
```

This Skill may compose decisions from those owners. It must not silently redefine
their domain semantics.

## Decision Coverage

Cover only the decisions relevant to the current scope; revisit them in any
order as new evidence appears.

| Decision | Completion criterion |
| --- | --- |
| Ground | The question, object/version/market/host scope, project Authorities, source observations, accepted decisions, and evidence are distinguishable. |
| Normalize | Apparent disagreements are checked for scope, temporal plane, representation, and semantic-owner differences before being called conflicts. |
| Surface | Material conflicts, ambiguities, gaps, assumptions, hypotheses, drift, violations, risks, and evidence gaps are explicit; incidental unknowns remain local. |
| Compose | Applicable owner-scoped rules expose required inputs, allowed Agent decisions, escalation boundaries, probes, and proof obligations. |
| Decide | Ordinary reversible architecture choices are made; semantic, irreversible, public-contract, permission, privacy, or destructive choices are routed to their Authority. |
| Bound | Exploration, reversible implementation, commitment, and claim boundaries are named where they materially affect autonomy. |
| Project | Settled semantics are projected to the requested language, runtime, frontend, repository, migration, or Harness view without changing the underlying decision. |
| Persist | Decision Trace or ADIR is written only when cross-Agent handoff, long migration, audit, diff, or a real machine consumer earns it. |
| Verify | Health and completion claims cite current source/evidence and name invalidation conditions and `not_proven` neighbors. |

## Core Invariants

```text
one problem scope before one conflict judgment
normative claim != source observation != inference != assumption
current != accepted target != future candidate
unknown != unhealthy
not_proven != failed
source existence != accepted intent
best-looking implementation != product or architecture Authority

ADIR node kinds are owner-qualified
ADIR references owning artifacts instead of copying them
partial information stays partial; schema completion never justifies invention
health is derived and multi-dimensional, not a permanent scalar score
an unresolved issue blocks only the affected commitment
```

A `False Known` is more dangerous than an explicit unknown. Treat stale docs,
current/target confusion, unsupported single-writer claims, and fake-only proof as
Map–Territory findings rather than trusted inputs.

## Commitment-Aware Autonomy

Use these distinctions when the task needs them:

```text
Exploration Readiness
  enough truth and stop lines to investigate, prototype, or probe safely

Reversible Implementation Readiness
  enough closure for low-commitment changes with a credible rollback

Commitment Closure
  relevant decisions are closed before durable data, public compatibility,
  permissions, destructive migration, or irreversible external effects change

Claim Closure
  evidence covers the exact completion, correctness, or release claim
```

An Autonomy Envelope is an optional projection containing settled facts,
material residual unknowns, decision rights, allowed assumptions, stop lines,
and proof obligations. Do not generate it for ordinary local choices.

## Read When Needed

- ADIR structure and epistemic axes: [Architecture Decision IR](references/architecture-decision-ir.md)
- Conflict, ambiguity, gaps, assumptions, and false knowns: [Issue and Uncertainty Model](references/issue-and-uncertainty-model.md)
- Owner-scoped rules and local decision trees: [Decision Calculus](references/decision-calculus.md)
- Decision rights and commitment-aware autonomy: [Decision Trace and Autonomy](references/decision-trace-and-autonomy.md)
- Source reconciliation and diff: [Map–Territory Reconciliation](references/map-territory-and-health.md)
- Evidence-bounded dimensions and findings: [Architecture Health](references/architecture-health.md)
- When and where an IR becomes durable: [Project Materialization](references/project-materialization.md)
- How architecture owners extend the model: [Extension Contract](references/extension-contract.md)

## Output

Return the smallest decision-bearing view. Make the resolved scope, semantic
owners, material issue, decision, commitment boundary, and proof limit visible
when they matter. Use tables, graph notation, a Decision Trace, Architecture
Health findings, or an Autonomy Envelope only when the request benefits from
those durable structures.
