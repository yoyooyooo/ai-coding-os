# Minimal Application Tree Example

A small single-host TypeScript service can stay compact while preserving host, capability, and verification roles.

```text
src/
  host/
    api.main.ts
    api.config.ts
    api.composition.ts
    api.shutdown.ts
  modules/
    orders/
      order.model.ts
      order.create.use-case.ts
      order.repository.port.ts
      order.repository.postgres.live.ts
      order.http.contract.ts
      order.http.handlers.ts
      order.public.ts
tests/
  order.create.integration.test.ts
docs/
  README.md
  product/
    README.md
    order-management.md
  architecture/
    README.md
    fact-authority-map.md
AGENTS.md
package.json
```

## Defaults used

- one host owns configuration, live composition, and shutdown;
- the capability is a private module with an explicit public surface;
- semantic dot filenames reveal responsibilities;
- the handler decodes and calls the use case rather than writing the database;
- docs exist only for durable product and architecture meaning.

## Intentionally omitted

```text
apps/
packages/
workflows/
Effect Service/Layer files
message bus
repository-per-table family
full product template set
```

None is earned by current pressure.

## Pressure that would justify the next step

- add `apps/worker/` when independent worker lifetime or throughput exists;
- promote a module to `packages/` when several hosts need a stable public API;
- add an outbox/event path when downstream publication must commit with the order;
- add Effect only when typed failure, resources, or structured concurrency materially help.

## Related Skills

- `$evolvable-application-architecture`
- `$product-harness-system`
