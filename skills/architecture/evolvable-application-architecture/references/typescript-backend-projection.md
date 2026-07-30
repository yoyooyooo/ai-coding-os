# TypeScript Backend Projection

Use for Node.js, Bun, Deno, Edge runtimes, serverless functions, or backend services written in TypeScript.

## Semantic mapping

```text
fact authority cell  host-private capability module or package
capability Port      application-owned interface, structural type, or Effect Service contract
live adapter         provider/transport/database implementation
composition root     <host>.composition.ts / <host>.main.ts
Command              readonly intent and operation identity
Outcome              readonly discriminated result of one use case
Receipt              smallest stable operation evidence when replay/reconciliation needs it
boundary guard       exports, import rules, project references, architecture tests
```

Interfaces are useful at genuine boundaries. Do not add `IThingService`, DI tokens, or paired Port/Service contracts for every class and helper.

## Projection invariant

> **Roles are semantic; files are earned.** Keep a responsibility distinguishable in code before deciding that it needs an independent file.

A small first slice may co-locate Command, Outcome, local Policy, and implementation:

```text
modules/
  orders/
    order.create.use-case.ts          # Command + Outcome + local policy may live here
    order.repository.port.ts
    order.repository.postgres.live.ts
    order.http.handlers.ts            # small contract/decoder/mapper may live here
```

This is a minimum base, not a mandatory four-file template. Add only the roles the capability needs.

## Pressure-labelled additions

| Add | Pressure that earns it |
| --- | --- |
| `order.model.ts` | several operations share cohesive product values or behavior |
| `order.create.command.ts` | several entries construct the Command or it becomes a stable contract |
| `order.create.outcome.ts` | several consumers need the complete use-case result type |
| `order.create.receipt.ts` | replay, reconciliation, or durable evidence needs a stable minimal record |
| `order.create.policy.ts` | policy changes independently, composes, or needs focused property tests |
| `order.repository.memory.fake.ts` | an actual test needs a behavioral substitute |
| `order.http.contract.ts` / `.schema.ts` / `.mapper.ts` | the wire boundary is stable, non-trivial, reused, or independently tested |
| `order.public.ts` | another module or host needs a deliberate stable surface |
| `order.wiring.ts` | module-local construction has become an independent responsibility |
| `<consistency-scope>.transaction.port.ts` | several writes share a real consistency boundary and the mechanism needs an owned contract |
| `<operation-scope>.idempotency.port.ts` | replay/storage policy is independently reusable or provider-backed |

Do not create optional siblings merely because a suffix exists.

## Runtime validation

TypeScript types disappear at runtime. Decode untrusted transport, provider, database, and file payloads at the edge, then convert to normalized application types. Do not leak `any`, SDK response types, ORM rows, or raw JSON through the core.

## Import policy

Follow [Source topology and semantic naming](source-topology-and-semantic-naming.md). In particular:

```text
model/policy        no framework, DB, SDK, live adapter, or process environment
use-case            model/policy/Port/consistency contracts only; no live provider
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

## Persistence and consistency

The transaction boundary follows the product invariant, not the module name or repository count. A transaction capability belongs to the consistency scope that must commit together.

Use one of the project's coherent mechanisms:

```text
explicit transaction context
transaction-scoped repositories
application Unit of Work
store-native transaction program hidden behind an application capability
```

Do not create one module-specific transaction Port by default. Cross-capability operations must be able to join the same consistency scope without importing one module's private infrastructure.

Idempotency is first an operation semantic: stable identity, scope, request fingerprint, retained result, expiry, and unknown-outcome behavior. Extract an idempotency capability only when storage, provider integration, reuse, or independent policy makes it valuable.

Commit business rows and event/audit/outbox records together when the invariant requires it. Database constraints and migrations are part of the fact-protection surface, not incidental adapter detail.

## Outcome and Receipt

The Outcome is the complete result of the use case. A Receipt is optional evidence carried by an accepted, attempted, or uncertain Outcome when replay or reconciliation needs it.

```text
Outcome
  accepted { receipt }
  incomplete { gaps }
  not accessible
  version conflict
  pending / unknown external result

Receipt
  operation identity
  resulting fact/version reference
  commit or provider reference
  timestamp or causal frontier when needed
  replay metadata when useful
```

A successful idempotent replay normally returns the prior accepted Outcome or equivalent Receipt; it is not automatically a rejection. Persist the smallest stable Receipt needed for replay, not a full mutable aggregate snapshot by default.

## Public surfaces

Use explicit exports and architecture checks when private/deep imports become a recurring problem. Avoid path aliases that make app internals look like stable packages. Do not create `*.public.ts` before a real cross-module consumer exists.

## Effect projection

Effect Services and Layers implement the same application roles; they do not create a parallel architecture.

```text
application Port
  -> ordinary TypeScript contract OR Effect Service contract
  -> choose one canonical contract by default

<capability>.<provider>.live.ts
  -> may export the live Layer that implements that contract

<host>.composition.ts
  -> may assemble the Layer graph and own resources

<host>.runtime.ts
  -> conditional facade when a non-Effect host needs to execute prepared Effects
```

An Effect Service may be the concrete representation of an application Port. Do not maintain parallel `.port.ts` and `.service.ts` contracts for the same capability unless each has a distinct consumer, compatibility boundary, or translation responsibility. Use `$effect-best-practices` for installed-version syntax, failure, Scope, Layer, Runtime, Queue, Stream, and Actor mechanics.

## Mechanical evidence

Use as applicable:

```text
runtime decoder tests
Port/Service conformance tests
transaction and migration tests
restart/replay/idempotency scenarios
host lifecycle and cleanup tests
exports/import-boundary checks
public API parity across real implementations
```

Each observation proves only the path and dependencies it exercised.

## Related knowledge

- Use [Source topology and semantic naming](source-topology-and-semantic-naming.md) for role vocabulary and extraction pressure.
- Use [Default repository profile](default-repository-profile.md) for directory topology.
- Use [Capability boundaries and adapters](capability-boundaries-and-adapters.md) for Port semantics.
- Use [Use cases, transactions, and idempotency](use-cases-transactions-and-idempotency.md) for operation identity and consistency.
- Use [Composition roots and lifetimes](composition-roots-and-lifetimes.md) for host ownership.
- Use [Scenario examples](scenario-examples.md) for concrete mappings.
- Return to the [EAA map](../SKILL.md).
