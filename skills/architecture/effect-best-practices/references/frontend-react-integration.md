# Frontend Integration

Use `$frontend-architecture` for state ownership, route/feature topology, Query,
store, realtime reconciliation, and React component boundaries. This reference
only maps a chosen frontend capability to Effect.

## Runtime Owner

Create the live Layer and Runtime in the browser/app/desktop host composition
root. Do not create them in component render, feature modules, Query functions,
Zustand stores, or mappers.

```text
host bootstrap
  -> normalize config and browser implementations
  -> build closed Layer
  -> create runtime-bound ProductClient
  -> inject client into providers/routes/features
  -> dispose at host shutdown
```

SSR/server hosts use request-safe composition. Do not share request-specific
mutable services through a process-global Runtime unless the Service contract is
explicitly safe to share.

## React Bridge

React consumers should usually receive ordinary methods or a focused hook built
on a runtime-bound facade. A component may trigger a method backed by Effect;
it should not provide live Layers or call global `Effect.runPromise` directly.

For subscriptions, expose an idempotent `close()` and ensure “close before open
completes” still releases the acquired resource. React development lifecycles may
mount and unmount repeatedly.

## Query and Store

Query functions call the injected client. They do not rebuild Layers or Runtimes.
Zustand/external stores own local interaction, not Effect dependencies or remote
business truth. Effect Services must not import React, Query, or Zustand.

## Effect-Native Frontend

A feature may intentionally be Effect-native when the team accepts that public
contract and its benefits are concrete. Even then:

```text
React remains the render adapter
runtime ownership remains explicit
external stores use stable React subscription integration
resources remain scoped
feature state authority follows frontend doctrine
```

## Tests

Test Effect programs with fake Layers without React, runtime-bound client
contracts without DOM, Query/store adapters independently, then browser behavior
for claims involving lifecycle, rendering, or real transport.
