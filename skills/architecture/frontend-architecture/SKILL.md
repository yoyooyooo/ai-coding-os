---
name: frontend-architecture
description: >-
  Designs and audits frontend architecture as an intent, projection, and
  interaction system. Use for React or TypeScript app topology, route/feature
  boundaries, server versus local state, optimistic updates, client/query/store
  responsibilities, realtime/WebSocket/SSE consistency, host composition,
  frontend packages, naming, or UI harnessability. Use with evolvable-application-architecture
  when backend authority, transactions, or migrations are in scope, and with
  effect-best-practices only when Effect is already selected or present. Treat
  effect-api-app-kit as a backend generator, not a frontend topology authority.
---

# Frontend Architecture

Treat the frontend as a host that expresses intent, consumes authoritative
projections, owns local interaction, and reconciles asynchronous change. Folder
names are implementation carriers; ownership and dependency direction are the
architecture.

## Ownership Contract

```text
Owns: frontend state taxonomy, route/feature topology, client/query/store/
realtime boundaries, host composition, React adapters, naming semantics, and
frontend proof strategy.
Delegates: backend fact authority/transactions/migrations -> evolvable-application-architecture;
Effect Service/Layer/Scope/API details -> effect-best-practices; generated backend
HttpApi profile mechanics -> effect-api-app-kit.
Does not prescribe: one mandatory framework, state library, router, package
build mode, or visual design system.
```

Read [Skill Family Coordination](references/skill-family-coordination.md) when
more than one architecture skill or the executable kit applies.

## Workflow

1. Read project SSoT, route tree, package graph, runtime wiring, state/query
   ownership, realtime path, and tests. Project rules override defaults.
2. Classify the task: state ownership, topology, host composition, command/query,
   optimistic reconciliation, realtime continuity, naming, React adapter, or
   harness/evidence.
3. Trace one user intent to command acknowledgement and authoritative projection.
4. Classify every state item by authority and lifetime before choosing a library.
5. Place composition at host roots; keep feature logic independent of live
   transports, credentials, and runtime construction.
6. Recommend the smallest capability profile that meets the pressure. Do not add
   Query, a global store, or Effect merely for symmetry.
7. Separate observed facts, proposed refactor, verification, and `not_claimed`.

## Core Invariants

```text
intent is not accepted fact; optimistic state is a proposal
one state concept -> one owner -> one reconciliation path
commands request change; queries read projections; realtime announces committed change
components render and dispatch; host roots assemble live capabilities
external mutable stores integrate through stable subscription contracts
unknown/gapped realtime state -> invalidate or backfill, never invent truth
feature boundaries follow product capability, not technical file type alone
```

## Progressive Disclosure

| Need | Read |
|---|---|
| Baseline model and dependency principles | [Core Doctrine](references/core-doctrine.md) |
| State ownership and consistency | [State and Consistency](references/state-and-consistency.md) |
| Roles, packages, hosts, composition | [Topology and Composition](references/topology-and-composition.md) |
| Minimal/Query/store/Effect profiles | [Reference Profiles](references/reference-profiles.md) |
| Naming and file responsibility | [Naming Semantics](references/naming-semantics.md) |
| React-specific mapping | [React Adapter](references/react-adapter.md) |
| WebSocket/SSE/polling continuity | [Realtime Capability](references/realtime-capability.md) |
| Existing repo/component review | [Audit Checklist](references/audit-checklist.md) |

## Output

```text
classification; authorities_read; intent_projection_trace; state_ownership_map;
dependency_graph; host_composition; capability_profile; findings_by_severity;
target_topology; reconciliation_rules; realtime_recovery; migration_steps;
auto_fix_candidates; human_decisions; verification; not_claimed.
```
