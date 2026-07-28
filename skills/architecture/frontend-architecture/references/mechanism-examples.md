# Mechanism Examples

These examples show how to choose mechanisms from state and lifetime pressure rather than from a stack identity.

## Minimal React capability

Use ordinary React state and an injected client when data is simple and no shared remote-cache or cross-tree interaction pressure exists.

## Server projection

Add TanStack Query or an equivalent when the project needs shared remote cache, freshness, dedupe, background refetch, mutation lifecycle, invalidation, or SSR dehydration.

## Interaction-heavy surface

Add an external store when local interaction crosses many branches, has independent subscriptions, or must be consumed outside React. Keep remote projection in the query owner.

## Realtime projection

Add a typed subscription plus sequence/cursor, dedupe, gap detection, reconnect, and backfill. Apply projection updates or invalidate queries; do not construct the socket inside the feature reducer.

## Effect-integrated frontend

Use Effect when typed failures, replaceable capabilities, structured concurrency, or resource lifetime justify it. The host owns the Runtime. Features consume a narrow facade or React adapter.

## Combined profile

A project may use router + Query + local store + Effect + React when each has a distinct role:

```text
router       navigation
Query        remote projection and mutation lifecycle
store        local interaction
Effect       execution/resources/concurrency/failure
React        rendering/events
```

If two mechanisms own the same state, simplify.

## Related knowledge

- Use [State roles and ownership](state-roles-and-ownership.md) before selecting libraries.
- Use [Default frontend source conventions](default-frontend-source-conventions.md) for file roles.
- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) for resource ownership.
- Use `$effect-best-practices` for Effect-specific decisions.
- Return to the [Frontend Architecture map](../SKILL.md).
