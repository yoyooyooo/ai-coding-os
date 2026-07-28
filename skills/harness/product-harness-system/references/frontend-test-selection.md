# Frontend Test Selection

Choose a frontend test surface from the property, not from a fixed pyramid or coverage target.

## Pure logic

Use ordinary unit or property tests for:

```text
mappers
view-model derivation
store transitions
realtime reducers
query-key builders
permission/visibility policy
formatting with product meaning
```

## Component behavior

Use a component rendering surface when the property concerns rendering, user events, accessible semantics, or local interaction and does not require full routing/browser behavior.

## Client and query integration

Use focused integration for decoding, error mapping, query invalidation, optimistic lifecycle, and injected client behavior. Label fake/replay/live dependencies.

## Browser

Use browser observation when route/history, focus, real layout, storage, hydration, service worker, clipboard, download, or browser network behavior matters.

## Realtime and reload

Use headless or browser scenarios with explicit sequence/cursor, disconnect, reconnect, gap, and reload depending on which host behavior matters.

## Avoid implementation-lock tests

Do not assert private hook call order, exact internal component structure, or store implementation when only user behavior is the contract.

## Test naming

Use semantic roles before the project runner suffix:

```text
order.view-model.unit.test.ts
order.client.contract.test.ts
order.realtime.integration.test.ts
checkout.reload.recovery.test.ts
```

## Related knowledge

- Use [Choosing an observation surface](choosing-observation-surface.md) for cross-system surfaces.
- Use [Browser and UI observation](browser-and-ui-observation.md) for browser properties.
- Use [Regression placement](regression-placement.md) after a defect.
- Use `$frontend-architecture` for state owners and source conventions.
- Return to the [Harness map](../SKILL.md).
