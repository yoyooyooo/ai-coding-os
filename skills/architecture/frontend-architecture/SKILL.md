---
name: frontend-architecture
description: Design frontend ownership when Query, store, URL, realtime, React, Effect, and client layers compete for authority; when user intent, acknowledgement, reconciliation, reload, SSR/hydration, or host lifetime is unclear; or when feature boundaries and source naming drift across projects.
---

# Frontend Architecture

Frontend architecture separates different kinds of truth and assigns each one a clear owner. The frontend proposes user intent, renders projections, owns local interaction state, and reconciles asynchronous reality. It does not become the final authority for product facts merely because it displays or caches them.

```text
intent        what the user asks to happen
proposal      optimistic or local candidate state
projection    server-derived view of accepted facts
interaction   local UI state such as focus, selection, draft, expansion
continuity    ordering, dedupe, gap detection, reconnect, and backfill
view model    pure composition for one user-facing surface
host          live clients, runtimes, caches, sockets, workers, and providers
```

## Semantic anchors

- **Intent Is Not Fact.** A click, draft, optimistic mutation, or queued command expresses what the user wants; it does not prove the product fact changed.
- **Projection Is Not Authority.** Query caches, views, and realtime frames render or update projections of accepted facts; they do not become the final writer.
- **One State Role, One Owner.** URL, remote projection, local interaction, continuity, and execution state need distinct ownership even when one screen composes them.
- **Realtime Restores Continuity; It Does Not Create Truth.** Realtime coordinates ordering, dedupe, gaps, reconnect, and backfill around authoritative facts.
- **Optimism Needs Reconciliation.** A fast proposal remains provisional until acknowledgement, rejection, timeout, reload, or later projection resolves it.

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| Query cache, store, URL, component state, and realtime all appear to own the same concept | [State roles and ownership](references/state-roles-and-ownership.md) |
| optimistic updates, acknowledgement, rejection, and reconciliation are unclear | [Intent, acknowledgement, and reconciliation](references/intent-acknowledgement-and-reconciliation.md) |
| reconnect, dedupe, sequence, gap, backfill, reload, or stale projection behavior is unclear | [Realtime continuity and reload](references/realtime-continuity-and-reload.md) |
| host roots, SSR/hydration, Runtime, Query client, socket, or worker ownership is unclear | [Topology, composition, and hosts](references/topology-composition-and-hosts.md) |
| features, public surfaces, generic buckets, or source names are inconsistent | [Naming and feature boundaries](references/naming-and-feature-boundaries.md) |
| a greenfield project needs deterministic frontend directories and suffix semantics | [Default frontend source conventions](references/default-frontend-source-conventions.md) |
| generated clients or transport contracts must evolve without freezing view models | [Client contract evolution](references/client-contract-evolution.md) |
| only a final UI symptom is visible | [Diagnosing frontend state](references/diagnosing-frontend-state.md) |
| React, Query, external stores, Suspense, or Effect need concrete integration boundaries | [React integration](references/react-integration.md) |
| mechanism examples are useful | [Mechanism examples](references/mechanism-examples.md) |

These are independent ownership questions, not a maturity ladder.

## State ownership defaults

```text
router       URL and navigation authority
query cache  remote projections and mutation lifecycle
local store  local interaction state only
realtime     continuity and projection-update coordination
Effect       execution, dependencies, resources, concurrency, typed failure
React        rendering and user-event adapter
```

If two mechanisms own the same state or lifetime, simplify before adding another abstraction.

## Portable frontend default

When the project has no coherent convention, use the feature topology, suffix semantics, and import rules in [Default frontend source conventions](references/default-frontend-source-conventions.md). Do not generate every suffix mechanically.

## Core invariants

- Components emit intent and render view models; they do not write accepted server facts directly.
- Remote projection and local interaction state remain distinct even when presented together.
- Optimistic state carries operation identity and a reconciliation path.
- Realtime delivery is not authoritative merely because it is immediate.
- Host-specific live resources are created and closed by the host, not by feature modules or components.
- Generated wire contracts do not become product view models by default.
- A feature consumes another feature only through an explicit public surface or host-level composition.

## Common smells

- a store mirrors the query cache and both are updated manually;
- components instantiate SDKs, sockets, Query clients, or Effect Runtimes;
- `status` mixes request lifecycle, business state, optimistic proposal, and UI visibility;
- realtime events patch projections without sequence, dedupe, gap, or backfill semantics;
- every feature deep-imports another feature's internals;
- `shared/`, `services/`, or `components/` becomes an unowned dumping ground;
- SSR and hydration create two live owners for the same resource.

## Adjacent owners

- Product obligations and acceptance belong to `$product-definition`.
- Final fact authority, transactions, and provider boundaries belong to `$evolvable-application-architecture`.
- Effect Scope, Runtime, failure, and concurrency semantics belong to `$effect-best-practices`.
- Browser, reload, reconnect, and UI proof belong to `$product-harness-system`.
- Durable placement and project routing belong to `$docs-governance`.

## Output principle

Identify the state roles, owners, acknowledgement/reconciliation behavior, host lifetimes, and smallest compatible source shape. Apply portable defaults only where the project is silent. Do not force every project to use Query, an external store, Effect, realtime, or a package boundary.
