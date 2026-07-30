# Effect Capability Tree Example

This example starts with the smallest valid Effect projection and adds optional files only after their pressure appears.

## Minimum base: Effect Service as the application Port

```text
src/
  host/
    api.composition.ts
  modules/
    notifications/
      notification.send.use-case.ts
      notification-gateway.service.ts
      notification-gateway.postmark.live.ts
```

## Defaults used

- `notification-gateway.service.ts` is the one canonical application capability contract;
- the use case is an Effect program that depends on that contract;
- the provider-qualified live file may export the implementing Layer;
- the host composition selects the live Layer and owns resource lifetime;
- product models and pure decisions remain ordinary TypeScript and may stay co-located while small.

## Alternative: ordinary application Port

A project that wants a framework-neutral contract may use:

```text
notification-gateway.port.ts
notification-gateway.postmark.live.ts
```

and omit `notification-gateway.service.ts`. Do not keep both contracts by default.

## Pressure-labelled additions

| Add | Pressure |
| --- | --- |
| `notification.model.ts` | several operations share cohesive values or pure behavior |
| `notification-gateway.memory.fake.ts` | an actual test needs a behavioral substitute |
| `api.runtime.ts` | a non-Effect HTTP/framework host needs a stable prepared-Runtime facade |
| `notification.queue.ts` | buffering/backpressure is a deliberate module capability |
| `notification.stream.ts` | Stream is a stable capability surface rather than an internal operator chain |
| `notification.actor.ts` | a real long-lived identity owns private state and a mailbox |
| `notification-gateway.layer.ts` | Layer construction itself has an independent named responsibility beyond the live adapter |

## Intentionally omitted

- a parallel `.port.ts` and `.service.ts` contract for the same gateway;
- a Service for every mapper and helper;
- a Layer file separate from the live implementation when it adds no semantic value;
- a Runtime file in an all-Effect host;
- an Actor or Queue without long-lived state or buffering pressure.

## Related Skills

- `$effect-best-practices`
- `$evolvable-application-architecture`
