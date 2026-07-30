# Minimal Application Tree Example

A small single-host TypeScript service can stay compact while preserving host, capability, and verification roles. The tree below is the smallest coherent base for this example, not a suffix checklist.

## Minimum base

```text
src/
  host/
    api.main.ts
    api.composition.ts
  modules/
    orders/
      order.create.use-case.ts          # Command + Outcome + local policy may be co-located
      order.repository.port.ts
      order.repository.postgres.live.ts
      order.http.handlers.ts            # small decode/map logic may be co-located
tests/
  order.create.integration.test.ts
package.json
```

## Defaults used

- one host owns live composition and process entry;
- the capability remains a private lexical module until a real consumer needs a public surface;
- semantic dot filenames reveal the responsibilities that have earned independent files;
- the handler decodes and calls the use case rather than writing the database;
- the application-owned repository contract hides PostgreSQL details;
- the test proves only the path and dependency reality it actually exercises.

## Pressure-labelled additions

| Add | Pressure |
| --- | --- |
| `api.config.ts` | environment decoding has stable rules worth a named owner |
| `api.shutdown.ts` | resources/background work require explicit close coordination beyond composition |
| `order.model.ts` | several operations share cohesive order values or behavior |
| `order.create.command.ts` | several entries construct the Command or it becomes a stable contract |
| `order.create.outcome.ts` | several consumers need the complete use-case result |
| `order.create.receipt.ts` | durable replay or reconciliation requires stable minimal evidence |
| `order.http.contract.ts` / `.schema.ts` / `.mapper.ts` | the wire boundary becomes non-trivial, reused, or independently tested |
| `order.repository.memory.fake.ts` | an actual test requires a behavioral substitute |
| `order.public.ts` | another module or host needs a deliberate cross-module surface |
| `order.wiring.ts` | module-local construction has an independent responsibility |
| `AGENTS.md` | durable local Agent instructions need a thin discoverable entry |
| `docs/product/` or `docs/architecture/` files | durable product or architecture meaning is not already current elsewhere |

## Intentionally omitted

```text
apps/
packages/
workflows/
parallel Port and Effect Service contracts
message bus
module-local transaction/idempotency boilerplate
repository-per-table family
full product or documentation template set
```

None is earned by current pressure.

## Pressure that would justify the next structural step

- add `apps/worker/` when independent worker lifetime or throughput exists;
- promote a module to `packages/` when several hosts need a stable public API;
- add an outbox/event path when downstream publication must commit with the order;
- add a consistency-scope transaction capability when several writes must atomically protect one invariant;
- add Effect-specific Service, Layer, Runtime, Queue, or Stream roles only when their execution semantics materially help.

## Related Skills

- `$evolvable-application-architecture`
- `$effect-best-practices`
- `$product-harness-system`
