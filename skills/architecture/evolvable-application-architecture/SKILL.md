---
name: evolvable-application-architecture
description: >-
  Cross-language authority-first application architecture for durable facts and
  change. Use when deciding or auditing fact ownership, use cases,
  transactions, consistency, capability ports, composition, boundary promotion,
  forward migration, MVP takeover, replaceability, or architecture evidence.
  Frontend, Effect, and cross-owner decision-system details stay with their
  owning Skills.
---

# Evolvable Application Architecture

Use an **authority-first application hexagon**:

```text
accepted facts live behind governed use cases
external powers cross application-owned capability boundaries
composition selects implementations and owns resources
forward evolution preserves accepted facts and fences old writers
evidence bounds every architecture claim
```

The doctrine is language-, runtime-, repository-, and deployment-neutral.
Ecosystem projections decide idiomatic modules, types, traits/interfaces,
resource lifecycles, and package shapes after the semantic boundary is known.

## Ownership

```text
Owns:
  fact authority, consistency domain, and authority epoch
  Commands, Observations, Candidates, Decisions, and materialization
  use-case, transaction, idempotency, event, inbox/outbox, and reconciliation shape
  capability ports, receipts, outcome-unknown, and adapter conformance
  composition profiles, resource owners, and host boundaries
  repository / compilation / deployable / authority / data distinctions
  pressure-based boundary promotion and ecosystem projection contract
  forward migration, bridge fencing, deletion gates, and replaceability
  architecture claim ceilings

Adjacent Suite owners, when installed:
  product semantics, requirements, and acceptance -> $product-definition
  cross-owner ADIR, architecture diff, health, and commitment boundaries -> $architecture-decision-system
  frontend state, topology, realtime, and reconciliation -> $frontend-architecture
  Effect Service, Layer, Scope, API, and Runtime -> $effect-best-practices
  managed Effect API generation after decisions settle -> $effect-api-app-kit
  proof architecture and empirical probes -> $product-harness-system
```

The project or accountable external owner retains product truth, security,
privacy, legal/policy, public compatibility, retention, and destructive-decision
Authority.

## Architecture Coverage

Cover only the decisions exposed by the current pressure; this is not a project
workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | Project Authority, accepted decisions, current source/schema/runtime evidence, relevant language/runtime versions, and Suite defaults are distinguishable. |
| Authority | Each accepted durable fact has one final materialization authority inside a named consistency domain and epoch; forbidden writers are visible. |
| Change | Authoritative intent and non-authoritative inputs take separate paths through authorize/validate/decide/materialize/commit. |
| Capability | Genuine outer powers have application-owned contracts; timeout, cancellation, retry, receipt, unknown outcome, and conformance are explicit where pressure exists. |
| Composition | One owned host/profile selects implementations, constructs resources, and closes lifecycle without moving product transitions into bootstrap code. |
| Boundaries | The smallest sufficient lexical, module, compilation, host, trust, or deployable boundary is chosen from observed pressure. |
| Evolution | A vertical slice can migrate forward; any bridge has source of truth, divergence handling, fencing, and deletion conditions. |
| Proof | Proof surface matches the claim; source observation, execution evidence, inference, `not_proven`, and `not_claimed` remain distinct. |

Within accepted product semantics and binding constraints, choose ordinary
reversible writer, transaction, port, module, and composition details without
escalation. Escalate when materially different answers change product meaning,
permissions/trust, irreversible data, public compatibility, binding policy,
destructive migration, or irreversible external effects. Localize undecidable
slices and continue unaffected work.

## Core Invariants

```text
canonical accepted fact
  -> one final materialization authority
     within a declared consistency domain and authority epoch

authoritative intent
  -> Command -> authorize/validate -> transition -> commit

non-authoritative output
  -> Observation/Candidate -> governed Decision -> materialize -> commit

external call outside the database transaction
accepted fact + required audit/event/outbox inside one transaction
adapter cannot silently materialize product facts
composition chooses implementations; use cases own product transitions
replaceability requires conformance evidence, not an interface alone

repository boundary != compilation boundary != deployable boundary
package/crate sharing does not grant fact-writing authority
memory ownership != product fact authority
visibility != authorization
successful compilation != behavioral evidence
```

## Pressure and Boundary Promotion

Start with the least committed semantic boundary that preserves ownership and
legibility. Promote only when real pressure appears:

```text
lexical discoverability
  -> private semantic module
  -> enforceable compilation/public-API boundary
  -> independently runnable host
  -> independently deployed/trust/fault boundary
```

Pressure signals include durable facts, concurrent updates, external effects,
restart/replay, public compatibility, independent lifecycle, trust/fault
isolation, reuse, compilation enforcement, money, permissions, privacy, and
irreversible migration. A P-level is a summary; the raw pressure signals drive
the mechanism.

## Ecosystem Projection

The core expresses semantic roles, boundary strength, lifecycle ownership, and
proof obligations. A language/runtime projection maps them idiomatically.

```text
TypeScript -> private module / package export / bootstrap / deployable
Rust       -> module visibility / crate facade / binary composition / process
Effect     -> Service / Layer / Runtime / Scope projection
Frontend   -> intent / projection / local interaction / reconciliation projection
```

Do not translate directory templates mechanically across ecosystems.

## Read When Needed

| Condition | Reference |
| --- | --- |
| Establishing the baseline | [Core Doctrine](references/core-doctrine.md) |
| Sizing mechanisms to pressure | [Pressure Profiles](references/pressure-profiles.md) |
| Assigning fact ownership | [Authority Model](references/authority-model.md) |
| Promoting module/package/host/deployable boundaries | [Repository Topology and Packaging](references/repository-topology-and-packaging.md) |
| Deciding source shape without leaking one ecosystem | [Source Topology and Semantic Naming](references/source-topology-and-semantic-naming.md) |
| Taking over an MVP | [MVP Takeover](references/mvp-takeover.md) |
| Governing AI-generated changes | [AI Coding Change Protocol](references/ai-coding-change-protocol.md) |
| Designing commands and materialization | [Use-Case Kernel](references/use-case-kernel.md) |
| Isolating providers, devices, or plugins | [Capability Ports](references/capability-ports.md) |
| Handling federation, CRDT, saga, or leader epochs | [Consistency and Authority Topologies](references/consistency-and-authority-topologies.md) |
| Repairing modularity | [Evolutionary Modularity](references/evolutionary-modularity.md) |
| Designing persistence and outbox | [Persistence and Events](references/persistence-and-events.md) |
| Building composition roots | [Composition Roots](references/composition-roots.md) |
| Migrating public or durable state | [Forward Evolution](references/forward-evolution.md) |
| Choosing architecture evidence | [Evidence Harness](references/evidence-harness.md) |
| Auditing an existing repository | [Audit Playbook](references/audit-playbook.md) |
| Architecting LLM/agent products | [Agentic Systems Profile](references/scenario-agentic-systems.md) |
| Implementing in Rust | [Rust Projection](references/adapter-rust.md) |
| Implementing a TypeScript backend | [TypeScript Backend Projection](references/adapter-typescript-backend.md) |
| Handing off to frontend architecture | [Frontend Projection](references/adapter-frontend.md) |
| Adding another ecosystem | [Projection Authoring Contract](references/adapter-authoring-template.md) |

## Output

Return only the decision-bearing architecture view. Make fact authority,
change/capability/composition boundary, material unknowns, and proof limit
explicit when relevant. Add full maps, persistent ADIR, source topology,
migration ledgers, or risk tables only when they materially improve the task or
the user requests that branch.
