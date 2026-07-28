# Realtime Continuity and Reload

> **Realtime Restores Continuity; It Does Not Create Truth.** Delivery speed does not grant authority; realtime coordinates order, dedupe, gaps, reconnect, and backfill around accepted facts.

Realtime delivery is a projection transport. It does not become authoritative merely because it arrives quickly.

## Continuity concerns

```text
subscription identity
sequence or cursor
ordering scope
duplicate behavior
gap detection
reconnect policy
backfill or full refresh
schema/version compatibility
permission changes
resource lifetime
```

## Apply or invalidate

A realtime adapter may:

- apply a typed projection update when ordering and completeness are sufficient;
- invalidate a query and let the normal fetch path rebuild the projection;
- mark the surface stale and require backfill when a gap is detected.

Do not patch arbitrary cached objects without a declared projection model.

## Duplicate and out-of-order delivery

Use event or entity version, operation ID, sequence, or cursor. Ignore known duplicates; buffer, reject, or backfill when order matters. Arrival time is not a reliable version.

## Gap and backfill

A reconnect may miss events. Define whether the client:

```text
resumes from a cursor
requests changes since version
invalidates and refetches
rebuilds from a snapshot plus stream
```

A successful socket reconnection is not proof that the projection is current.

## Reload

State what survives a full page reload:

```text
accepted remote facts        fetched or rehydrated
shareable navigation         URL
unsaved draft                local durable store only when product requires it
optimistic operation         operation log/identity if recovery requires it
realtime continuity          cursor/version if safe and meaningful
```

Do not rely on in-memory stores for product recovery.

## SSR and hydration

Declare what is prefetched, serialized, dehydrated, revalidated, and client-only. Avoid creating a second live socket, Runtime, or Query owner during hydration.

## Permissions and logout

Realtime channels and caches must be cleared or re-scoped when identity/permission changes. A stale cache is a security risk as well as a correctness issue.

## Related knowledge

- Use [State roles and ownership](state-roles-and-ownership.md) for projection ownership.
- Use [Topology, composition, and hosts](topology-composition-and-hosts.md) for socket lifetime.
- Use [Diagnosing frontend state](diagnosing-frontend-state.md) for stale/reconnect bugs.
- Use `$product-harness-system` for reload, reconnect, duplicate, and backfill scenarios.
- Return to the [Frontend Architecture map](../SKILL.md).
