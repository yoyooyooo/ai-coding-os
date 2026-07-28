# TypeScript Backend Projection

Use for Node.js, Bun, Deno, Edge runtimes, serverless functions, or backend services written in TypeScript.

## Semantic mapping

```text
fact authority cell  host-private capability module or package
capability Port      application-owned interface or structural type
live adapter         provider/transport/database implementation
composition root     <host>.composition.ts / <host>.main.ts
Command              readonly discriminated data
Outcome/receipt      readonly typed result
boundary guard       exports, import rules, project references, architecture tests
```

Interfaces are useful at genuine boundaries. Do not add `IThingService` or DI tokens for every class and helper.

## Default module shape

```text
modules/
  orders/
    order.model.ts
    order.create.use-case.ts
    order.repository.port.ts
    order.repository.postgres.live.ts
    order.repository.memory.fake.ts
    order.http.contract.ts
    order.http.handlers.ts
    order.public.ts
```

Only create roles the capability needs.

## Runtime validation

TypeScript types disappear at runtime. Decode untrusted transport, provider, database, and file payloads at the edge, then convert to normalized application types. Do not leak `any`, SDK response types, ORM rows, or raw JSON through the core.

## Import policy

Follow [Source topology and semantic naming](source-topology-and-semantic-naming.md). In particular:

```text
model/policy        no framework, DB, SDK, live adapter, or process environment
use-case            model/policy/Port/transaction only; no live provider
Port                no SDK or ORM types
HTTP handler        decode/map/call/map; no direct SQL or fact write
composition         selects live implementations; not imported by business modules
```

## State and context

- keep mutable module state private;
- avoid process-global service locators and singleton domain stores;
- pass explicit operation/command context rather than reading request globals deep in the graph;
- keep cross-capability references as IDs or value objects;
- keep HTTP request/response objects in transport adapters.

## Persistence

Pass an explicit transaction context or unit of work into repositories used by one application operation. Commit business rows and event/audit/outbox records together when the invariant requires it.

## Public surfaces

Use explicit exports and architecture checks when private/deep imports become a recurring problem. Avoid path aliases that make app internals look like stable packages.

## Effect

Effect Services and Layers may implement Ports and host composition. Do not turn pure modules into Services solely for uniformity. Use `$effect-best-practices` and its Default Effect module conventions for compatible Effect-specific mechanics and naming.

## Mechanical evidence

Use as applicable:

```text
runtime decoder tests
Port conformance tests
transaction and migration tests
restart/replay/idempotency scenarios
host lifecycle and cleanup tests
exports/import-boundary checks
public API parity across real implementations
```

## Related knowledge

- Use [Default repository profile](default-repository-profile.md) for directory topology.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for Port semantics.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for host ownership.
- Use [Scenario examples](scenario-examples.md) for concrete mappings.
- Return to the [EAA map](../SKILL.md).
