# Reference Profiles

Profiles are examples of capability choices, not mandatory stacks. Select the
smallest profile that satisfies current pressure and document deviations only
when they affect architecture or proof.

## Minimal React Profile

Use when data and interaction are simple:

```text
React
router of project choice
plain typed client/fetch adapter
component/context state
pure mappers/view models
```

Do not add Query, Zustand, or Effect until remote cache, cross-tree interaction,
resource, concurrency, or replacement pressure appears.

## Server-State Profile

Add TanStack Query or an equivalent when the frontend needs shared remote cache,
freshness, dedupe, background refetch, mutation lifecycle, invalidation, or
SSR dehydration. Query owns server projections; local interaction remains
outside the cache unless it is mutation metadata.

## Interaction-Heavy Profile

Add Zustand or another external store for cross-tree UI state, independent
subscriptions, high-frequency interaction, or non-React consumers. Keep server
truth in the query/projection owner. Use concurrency-safe React bindings.

## Realtime Profile

Add a typed client subscription with cursor/version, dedupe, gap detection,
reconnect, and backfill. Feature adapters patch or invalidate projections; live
transport remains at the host/client boundary.

## Effect-Integrated Profile

Add Effect when typed errors, replaceable capabilities, structured concurrency,
resource lifecycles, retry/timeout/cancel, or a shared Effect backend/client
justify it. The app host owns the runtime. Feature APIs consume runtime-bound
facades or dedicated React adapters. Load `$effect-best-practices` for details.

## Full Reference Combination

A project may use React + a router + TanStack Query + Zustand + Effect, but each
library must have a distinct job:

```text
router       navigation/URL authority
Query        remote projection cache and mutation lifecycle
Zustand      local interaction state only
Effect       execution, dependencies, resources, concurrency, typed failures
React        render and event adapter
```

If two tools own the same state or lifecycle, simplify before adding another
abstraction.
