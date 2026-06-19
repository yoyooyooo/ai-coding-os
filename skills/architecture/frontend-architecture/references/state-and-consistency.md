# State and Consistency

Classify state before selecting React state, a store, Query, URL params, IndexedDB,
or an Effect service.

## State Taxonomy

| Class | Typical owner | Examples | Reconciliation |
|---|---|---|---|
| Authoritative projection | query/cache layer | channel, issue, result, permissions | refetch, invalidate, patch with event/version checks |
| URL/navigation | router | selected entity, filters worth sharing, modal route | URL parse/serialize |
| Local interaction | component/feature store | draft, focus, open drawer, selection | direct local transition/reset |
| Optimistic proposal | mutation coordinator | pending echo, temporary row, unsaved patch | mutation id + accept/reject projection |
| External resource state | host/client capability | connecting, reconnecting, cursor, auth refresh | subscription lifecycle and diagnostics |
| Durable client-owned fact | explicit local authority | offline draft, device preference, local-first document | local schema/migration/sync protocol |
| Derived render state | pure function/view model | labels, grouped rows, enabled actions | recompute, do not persist |

## One Owner, One Reconciliation Path

For each state concept, record:

```text
owner
source of initialization
allowed writers
lifetime
identity/version
reconciliation trigger
reset/recovery path
```

Avoid mirroring the same server projection in Query cache, Zustand, component
state, and a realtime singleton. A second representation is justified only when
it has a different authority or lifetime and a defined reconciliation path.

## Choosing a Mechanism

Use component state when the value is local to a subtree and resets naturally.
Use URL state when navigation, sharing, history, or reload semantics matter.
Use a server-state cache when remote freshness, dedupe, invalidation, retries,
mutations, or shared observation matter.
Use an external store when independent subscriptions, cross-tree interaction,
high-frequency updates, or host integration justify it.
Use durable browser storage only when the product explicitly assigns client
ownership and migration/sync semantics.

Do not add a global store merely because multiple components read a value; a
query cache, URL, context, or lifted local state may already own it.

## Optimistic Change

Optimistic UI is a proposal, not an early accepted fact.

```text
create client mutation id
-> stage local proposal
-> send command
-> receive accepted/rejected/needs-review receipt
-> reconcile with authoritative projection
-> remove, replace, or mark proposal
```

Preserve enough identity to distinguish retry, duplicate acceptance, correction,
and rejection. Do not infer durable completion from HTTP 202, websocket delivery,
or runtime output alone.

## React Synchronization

Effects synchronize React with external systems. They are not the default way to
calculate derived data or mirror props into state. Prefer pure render derivation,
event handlers, router/query/store APIs, and stable subscriptions.

For external mutable stores, use a library integration based on
`useSyncExternalStore` or an equivalent concurrency-safe adapter. Avoid ad hoc
“read mutable singleton during render + useEffect subscription” patterns.

## Local-First Exception

A local-first frontend may own durable facts. In that case, promote the browser
store from “cache” to an explicit authority cell with:

```text
schema and migrations
command API
conflict/sync policy
idempotency/versioning
backup/export/recovery
projection and realtime semantics
```

Do not describe an IndexedDB table as authority merely because it persists.
