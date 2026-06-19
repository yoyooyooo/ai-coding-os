# React Adapter

React owns rendering, component lifecycle, and event adaptation. It does not
determine backend authority or construct every external capability.

## Component Boundary

Components should primarily:

```text
read props/hooks/selectors
render derived state
emit user intent through callbacks/actions
synchronize with genuine external systems through focused hooks
```

Avoid live client/runtime/credential construction, raw transport decoding,
manual server-cache mirrors, and derived-state Effects inside components.

A component may call a runtime-bound facade or a dedicated hook that executes an
Effect. The important rule is that components do not create/provide live Layers
or own the global runtime. Do not ban Effect values merely by file extension;
keep execution and lifecycle centralized and testable.

## Query Adapter

When using TanStack Query or an equivalent, feature query option factories own
query keys, fetch/mutation mapping, cache invalidation, and optimistic proposal
coordination. They consume a client contract.

```ts
export const channelProjectionOptions = (
  client: ChannelQueryClient,
  channelId: string
) => queryOptions({
  queryKey: ["channel", channelId, "projection"],
  queryFn: () => client.fetchProjection(channelId)
})
```

Option factories make route prefetch, SSR, and headless tests reuse the same
semantics. Do not create a live client or runtime inside `queryFn`.

## Local State

Start with component state. Promote to context or an external store when the
state outlives a subtree, needs independent subscriptions, crosses non-React
boundaries, or has high-frequency updates. Keep remote projections out of the
local store unless a deliberate snapshot/offline authority is being built.

## External Stores

Use `useSyncExternalStore` directly or through a library binding for external
mutable stores. The subscribe function and snapshot identity must be stable.
Avoid reading mutable singletons during render and hoping an Effect keeps them
in sync.

## Effects

Use React Effects to synchronize with external systems such as subscriptions,
browser APIs, or third-party widgets. Do not use them to calculate render data,
mirror props into state, or orchestrate state transitions that belong in event
handlers/reducers.

Subscription glue:

```ts
useEffect(() => {
  const subscription = client.subscribeProjection(input, handlers)
  return () => subscription.close()
}, [client, inputKey, handlers])
```

Keep handlers stable or route events through a stable adapter to avoid reconnect
loops. Cleanup must be idempotent because development StrictMode and host
transitions can mount/unmount more than once.

## Host and SSR

The browser entry/provider owns live clients, Query client, external stores, and
optional Effect runtime. Server-render hosts own their own request-safe
composition. Explicitly define dehydrate/hydrate and client revalidation; never
share request-specific mutable state through process globals.

## Surface Design

Prefer a container/surface split when it materially improves harnessability:

```text
page/container  reads query/store/realtime and maps actions
surface         receives view model + callbacks and renders
```

Do not split every component mechanically. Keep pure derivation in view-model or
mapper functions when it can be tested without React.
