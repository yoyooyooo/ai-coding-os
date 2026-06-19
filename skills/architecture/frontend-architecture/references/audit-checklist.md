# Audit Checklist

Use this for an existing frontend repo or one component/surface.

## System Trace

- Trace one intent through optimistic proposal, command receipt, committed
  projection, realtime/query reconciliation, and render.
- Identify which layer owns each state concept and resource lifecycle.
- Record gaps between claimed and exercised evidence.

## State

- Every state item is classified: authoritative projection, URL, interaction,
  optimistic proposal, resource, durable client fact, or derived render state.
- No unexplained server-state mirror exists in component/store/cache.
- Optimistic state has mutation identity and accept/reject reconciliation.
- Durable local state has schema, migration, and sync/recovery policy.

## Topology

- Host roots construct live clients/runtimes/config/resources.
- Routes translate framework concerns without absorbing feature logic.
- Features expose coherent product capabilities and do not deep-import another
  feature's private files.
- Packages do not import apps; public APIs prevent deep imports.
- Generated contracts remain distinct from view models.

## React and Libraries

- Components render/dispatch rather than construct live dependencies.
- Effects synchronize genuine external systems, not derived state.
- External stores use stable concurrency-safe subscriptions.
- Query/cache owns remote projections; local store owns interaction only.
- Each selected library has a distinct capability slot and test strategy.

## Realtime

- Raw frames are decoded before feature reduction.
- Dedupe, cursor/version, gap, reconnect, and backfill are explicit.
- Resource status is not presented as business completion.
- Close/unmount and StrictMode-like lifecycle behavior are tested.

## Naming and Imports

- Names communicate subject and responsibility.
- Generic buckets have narrow scope or a migration plan.
- Aliases/barrels preserve public boundaries rather than hide deep imports.
- Boundary checks automate important dependency rules.

## Component Overlay

For a single component, assess only code read:

```text
consumer API
data flow and derivation
effect/resource lifecycle
external boundary size
testability
extension points
render/update cost
mental model
```

## Output

```text
classification; code_read; intent_projection_trace; state_map; dependency_map;
patterns_to_keep; findings_by_severity; refactor_steps; verification_needed;
not_claimed.
```
