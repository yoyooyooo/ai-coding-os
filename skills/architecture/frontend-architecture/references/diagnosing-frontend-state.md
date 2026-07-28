# Diagnosing Frontend State

Frontend symptoms often appear far from the first wrong state. Preserve the user's exact path and determine which state owner first diverged.

## Capture the failure

```text
route and URL
identity/permission context
user actions and operation IDs
query cache and local-store snapshots when safe
realtime cursor/sequence/gap state
network request/response and timing
rendered state and console error
reload/reconnect behavior
```

## Common first wrong states

- a component reads a stale closure or wrong selector;
- query and local store both own the same projection;
- optimistic proposal lacks operation identity;
- a mutation response is treated as final fact when the outcome is pending;
- realtime update is applied out of order or after a gap;
- hydration creates duplicate live resources;
- permission change leaves old cache visible;
- a generated wire shape is used directly as a view model;
- a provider/client error is flattened into an unhelpful UI state.

## Diagnose by owner

Ask:

```text
is URL wrong?
is remote projection stale or invalid?
is local interaction state wrong?
is realtime continuity wrong?
is the view model deriving incorrectly?
is React rendering a correct view model incorrectly?
is the backend fact or contract itself wrong?
```

This prevents random edits across components, stores, and Query callbacks.

## Reproduction

Prefer a small browser or headless scenario that starts from known state and records the first divergence. A screenshot of the final symptom is not enough.

## Permanent defense

Place the fix at the lowest owner:

```text
type or mapper
query key/invalidation
store transition
realtime reducer/cursor check
client error mapping
view-model invariant
component accessibility behavior
browser or integration regression
```

## Related knowledge

- Use [State roles and ownership](state-roles-and-ownership.md) to identify the owner.
- Use [Realtime continuity and reload](realtime-continuity-and-reload.md) for reconnect and gap failures.
- Use [Intent, acknowledgement, and reconciliation](intent-acknowledgement-and-reconciliation.md) for optimistic bugs.
- Use `$product-harness-system` for browser observation and first-wrong-state investigation.
- Use `$evolvable-application-architecture` if the accepted fact or API contract is wrong.
- Return to the [Frontend Architecture map](../SKILL.md).
