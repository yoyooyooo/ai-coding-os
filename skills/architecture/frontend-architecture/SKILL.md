---
name: frontend-architecture
description: >-
  Frontend ownership architecture for React and TypeScript intent, projection,
  and interaction systems. Use when deciding or auditing route/feature
  topology, server versus local state, optimistic or realtime reconciliation,
  host composition, frontend packages, client-contract evolution, semantic
  naming, POC takeover, or harnessability.
---

# Frontend Architecture

Treat the frontend as a host that expresses intent, consumes authoritative
projections, owns local interaction, and reconciles asynchronous change.
Ownership and dependency direction are the architecture; folders carry them.

Inherit Bounded Semantic Flatness and the shared vocabulary from
`$evolvable-application-architecture`. This skill owns frontend meanings such as
`client`, `query`, `store`, `realtime`, `view-model`, `page`, and `surface`.

## Ownership

```text
Owns:
  frontend state taxonomy
  route and feature topology
  client/query/store/realtime boundaries
  host composition and React adapters
  frontend naming extensions
  wire-contract / feature-projection / view-model separation
  optimistic and realtime reconciliation
  frontend harnessability

Adjacent owners:
  backend fact authority/transactions/migrations -> $evolvable-application-architecture
  Effect Service/Layer/Scope/API -> $effect-best-practices
  shared harness language -> $product-harness-system
  reusable UI proof surfaces -> $ui-product-harness
  concrete test lane -> $frontend-test-system
  docs placement -> $docs-governance
```

## Frontend Pass

| Step | Completion criterion |
| --- | --- |
| Ground | Project authority, route tree, package graph, host wiring, state/query ownership, contracts, realtime path, and nearby tests are identified. |
| Trace | One user intent reaches command acknowledgement, authoritative projection, reconciliation, and render; every temporary proposal is marked. |
| Own | Every state concept has one owner, lifetime, persistence rule, and reconciliation path. |
| Compose | Live clients, Query clients, stores, runtimes, sockets, and credentials are created at named host roots; features consume contracts. |
| Size | The smallest profile that satisfies current pressure is selected; each added library has one owned responsibility. |
| Evolve | For legacy/POC code, new writes to mirrors are fenced, readers migrate to the selected owner, and deletion conditions are visible. |
| Prove | The chosen mapper, state, render, or browser surface matches the claim and names adjacent unproven behavior. |

## Invariants

```text
intent != accepted fact; optimistic state is a proposal
one state concept -> one owner -> one reconciliation path
commands request change; queries read projections
realtime announces committed change plus continuity metadata
components render and dispatch; host roots assemble live capabilities
unknown or gapped realtime state -> invalidate/backfill
wire contract != feature projection != view model
feature boundaries follow product capability
```

## Source Topology

Inside a feature owner, semantic flat files are the default:

```text
features/orders/
  order.client.ts
  order.client.browser.live.ts
  order.query.ts
  order.store.ts
  order.realtime.ts
  order.wire-to-projection.mapper.ts
  order.view-model.ts
  order.page.tsx
  order.surface.tsx
```

A repeated prefix is a lexical cluster. Promote it only for real ownership,
dependency, lifecycle, reuse, compile, or host pressure. Framework-controlled
route files keep framework names and remain thin.

## Read When Needed

| Condition | Reference |
| --- | --- |
| Establishing the baseline | [Core Doctrine](references/core-doctrine.md) |
| Assigning state ownership | [State and Consistency](references/state-and-consistency.md) |
| Designing packages, hosts, and composition | [Topology and Composition](references/topology-and-composition.md) |
| Selecting Minimal/Query/store/Effect profiles | [Reference Profiles](references/reference-profiles.md) |
| Naming frontend source | [Naming Semantics](references/naming-semantics.md) |
| Mapping to React | [React Adapter](references/react-adapter.md) |
| Handling WebSocket/SSE/polling continuity | [Realtime Capability](references/realtime-capability.md) |
| Evolving wire/client contracts | [Client Contract Evolution](references/client-contract-evolution.md) |
| Auditing an existing frontend | [Audit Checklist](references/audit-checklist.md) |

## Output

```text
classification
sources_read
intent_projection_trace
state_ownership_map
dependency_graph
host_composition
capability_profile
findings_by_severity
target_topology
contract_evolution
reconciliation_rules
realtime_recovery
migration_steps
verification_surfaces
not_proven
not_claimed
```
