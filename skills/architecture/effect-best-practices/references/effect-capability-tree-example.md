# Effect Capability Tree Example

```text
src/
  host/
    api.composition.ts
    api.runtime.ts
  modules/
    notifications/
      notification.model.ts
      notification.send.use-case.ts
      notification-gateway.port.ts
      notification-gateway.service.ts
      notification-gateway.postmark.live.ts
      notification-gateway.memory.fake.ts
```

## Defaults used

- the application-owned Port carries capability semantics;
- the Effect Service is present because several Effect programs consume the capability and tests replace it;
- the live implementation is provider-qualified;
- the host owns Layer composition and Runtime lifetime;
- pure models and use-case decisions remain ordinary TypeScript.

## Conditional elements

`api.runtime.ts` exists because a non-Effect HTTP framework needs a stable runtime-bound facade. An all-Effect host could execute the program directly and omit the file.

## Intentionally omitted

- a Service for every mapper and helper;
- a Layer file separate from the live implementation when it adds no semantic value;
- an Actor or Queue without long-lived state or buffering pressure.

## Related Skills

- `$effect-best-practices`
- `$evolvable-application-architecture`
