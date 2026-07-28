# Browser and UI Observation

Browser observation is required for properties that depend on actual rendering, navigation, focus, accessibility, hydration, storage, or browser APIs.

## Candidate properties

```text
route and history behavior
rendered information and actions
keyboard and focus order
screen-reader semantics and accessible names
loading, empty, pending, error, permission, and recovery states
responsive layout when material
SSR/hydration behavior
reload and local persistence
real network/client integration
```

## Locator discipline

Prefer roles, labels, and user-visible names. Test IDs are useful when no stable accessible or semantic locator exists. Avoid brittle selectors tied to styling or DOM depth.

## Observe user behavior, not implementation choreography

Assert the product-visible result and meaningful states. Do not freeze every internal hook call or component tree detail.

## Accessibility

Accessibility is product behavior. Observe keyboard-only operation, focus placement after navigation/error, accessible names, status announcements, and permission/error messaging where relevant.

## Network and state

A browser test should make dependency reality visible. Mocked network can support focused UI behavior; real API integration is needed for contract and lifecycle claims.

## Reload and recovery

Reload is a useful boundary for detecting accidental in-memory authority. Test what should survive, refetch, restore, or disappear.

## Flake diagnosis

A flaky browser test is evidence of an unclear wait, race, environment, selector, resource, or product transition. Replace arbitrary sleep with an observable condition. Preserve traces, screenshots, console, and network only when they help locate the first wrong state.

## Related knowledge

- Use [Frontend test selection](frontend-test-selection.md) to decide whether browser is necessary.
- Use [Restart, retry, reconnect, and recovery](restart-retry-reconnect-and-recovery.md) for reload/reconnect.
- Use [Investigation and the first wrong state](investigation-and-first-wrong-state.md) for flake diagnosis.
- Use `$frontend-architecture` for state ownership and host lifetime.
- Return to the [Harness map](../SKILL.md).
