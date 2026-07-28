# React Integration

React should remain the rendering and user-event adapter. Live capabilities, remote projections, local interaction, and resource lifetimes retain their own owners.

## Provider composition

The host may provide:

```text
router
query client
product clients
Effect Runtime facade when needed
external local store
identity/session context
feature flags or policy projections
```

Construct live resources outside ordinary components. Providers expose already-owned capabilities; they should not become service locators for unrelated internals.

## Components

Components should:

```text
receive a view model or focused state
emit user intent through callbacks/hooks
render loading, empty, error, permission, pending, and recovery states
preserve accessibility and interaction semantics
```

They should not decode provider payloads, open sockets, create Runtime instances, or write accepted facts.

## Query

Query hooks/options consume an injected client. Query owns remote projection cache and mutation lifecycle. Use stable keys, explicit invalidation, and typed outcomes.

## External stores

Use an external store when cross-tree local interaction, independent subscriptions, non-React consumers, or high-frequency interaction justifies it. Use React-safe subscription APIs. Keep server projection out of the store.

## Suspense and transitions

Suspense and transitions affect rendering and user experience, not product authority. Define which pending and failure states remain visible and recoverable.

## Strict Mode

React development behavior may intentionally mount/effect more than once. Resource creation inside component effects must be idempotent and correctly cleaned up; host-owned resources avoid many duplicate-lifetime problems.

## Server components and SSR

Keep secrets, server-only capabilities, and non-serializable resources on the server side. Make the projection and hydration contract explicit.

## Effect

If React consumes Effect, prefer a host-owned Runtime or a narrow runtime-bound facade. Do not create live Layer graphs in each hook. Use `$effect-best-practices` for failure, Scope, and Runtime semantics.

## Related knowledge

- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) for provider ownership.
- Use [State roles and ownership](state-roles-and-ownership.md) for Query/store/component state.
- Use [Default frontend source conventions](default-frontend-source-conventions.md) for `.surface.tsx` and `.page.tsx`.
- Use `$product-harness-system` for browser and accessibility observation.
- Return to the [Frontend Architecture map](../SKILL.md).
