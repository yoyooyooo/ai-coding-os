# Frontend Feature Tree Example

```text
src/
  host/
    web.composition.tsx
    web.providers.tsx
  features/
    orders/
      order.client.ts
      order.client.browser.live.ts
      order.client.fake.ts
      order.query.ts
      order.store.ts
      order.realtime.ts
      order.wire-to-projection.mapper.ts
      order.view-model.ts
      order-list.surface.tsx
      order-details.page.tsx
      order.fixture.ts
      order.public.ts
  shared/
    money/
      money.model.ts
      money.format.ts
```

## Defaults used

- the feature is named after product work, not a component type;
- the host constructs the live client, Query client, socket, and providers;
- Query owns remote projection;
- the store owns local interaction only;
- realtime owns sequence/gap/backfill coordination, not transport construction;
- the surface consumes a view model and callbacks;
- `public.ts` is the only cross-feature entry.

## Conditional elements

- `.store.ts` exists because local selection and batch-edit state crosses the component tree;
- `.realtime.ts` exists because the product requires live updates with reconnect;
- `.client.fake.ts` exists for deterministic component and demo behavior.

## Intentionally omitted

- a global app store for server data;
- an Effect Runtime inside the feature;
- a generic `components/` folder;
- a package boundary.

## Related Skills

- `$frontend-architecture`
- `$product-harness-system`
