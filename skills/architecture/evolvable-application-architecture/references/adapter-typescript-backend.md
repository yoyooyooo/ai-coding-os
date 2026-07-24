# TypeScript Backend Adapter

Use for Node.js, Bun, Deno, Edge runtimes, serverless functions, or backend
services written in TypeScript.

## Idiom mapping

```text
Authority cell   -> host-private module/package with unexported state
Capability port  -> application-owned interface or structural type
Adapter          -> provider/transport/database implementation module
Composition root -> <host>.composition.ts / <host>.main.ts
ChangeSet        -> use-case-specific readonly discriminated data
CommitReceipt    -> readonly typed result
Boundary guard   -> package exports, import rules, project references, architecture tests
```

Interfaces are useful at genuine boundaries. Do not add `IThingService` or a DI
token for every class/helper.

## Monorepo reference

```text
apps/api/src/
  host/
    api.main.ts
    api.config.ts
    api.composition.ts
    api.shutdown.ts
  modules/
    orders/
      order.public.ts
      order.wiring.ts
      order.model.ts
      order.create.use-case.ts
      order.repository.port.ts
      order.repository.postgres.live.ts
      order.repository.memory.fake.ts
  workflows/
    checkout/
      checkout.start.workflow.ts
```

Start with a private module. Promote to a workspace package only when compile,
reuse, release, trust, ownership, or multiple-host pressure is real.

`apps/api` and `apps/worker` importing the same package does not grant both hosts
materialization authority. Allowed writers and transaction ownership remain
explicit project facts.

## Semantic filenames

Use `$ai-coding-os-suite-contracts` for Suite defaults and the project's
resolved vocabulary for adopted rules. Preferred patterns include:

```text
<subject>.<operation>.command.ts
<subject>.<operation>.use-case.ts
<subject>.<purpose>.query.ts
<subject>.<decision>.policy.ts
<subject>.<capability>.port.ts
<subject>.<capability>.<provider>.live.ts
<subject>.<capability>.memory.fake.ts
<subject>.http.contract.ts
<subject>.http.handlers.ts
<subject>.public.ts
<subject>.wiring.ts
```

Do not generate all roles mechanically. A simple operation may keep command,
outcome, and implementation in one `*.use-case.ts` file.

## Boundary validation

TypeScript types disappear at runtime. Validate untrusted transport and adapter
payloads at the edge with a schema/decoder, then convert to normalized
application types. Do not leak `any`, provider SDK response types, ORM records,
or raw JSON through the core.

## Import policy

```text
*.policy.ts
  no HTTP, DB, SDK, live adapter, or environment import

*.use-case.ts
  may import model/policy/port/transaction contracts
  must not import *.live.ts or framework handlers

*.port.ts
  must not expose provider SDK or ORM types

*.http.*.ts
  decode/map/call use case; no direct repository live import or SQL

*.public.ts
  normal cross-module surface

*.wiring.ts
  host composition surface; not imported by ordinary business modules
```

Use package `exports` and architecture checks to reject deep imports. Avoid
path aliases that make private app internals look like public packages.

## State and context

- Keep mutable module state private.
- Avoid process-global service locators and singleton domain stores.
- Expose explicit commands and queries.
- Pass `CommandContext` rather than reading request globals deep in the graph.
- Keep cross-cell references as explicit IDs/value objects.
- Keep HTTP request/response objects in input adapters.

## Persistence

Pass an explicit transaction context or unit of work into repositories used by
one application operation. Commit business rows and event/audit/outbox together.
A process-global ORM client is not a transaction boundary.

Prefer use-case-specific outcomes and discriminated unions over one giant DTO
with optional fields for every command.

## Composition and runtime

Construct SDK clients, adapters, credentials, decoders, database pools, and
resource scopes in host composition. Reusable application modules do not import
every provider implementation or branch on vendor names.

If using Effect, Services/Layers may implement ports and composition profiles.
Do not turn every pure module into a Service solely for uniformity.

## Mechanical proof

Use as applicable:

```text
package exports and project references
lint/import/dependency checks
runtime decoder tests
port conformance suites
database transaction and migration tests
restart/replay/idempotency scenarios
host lifecycle and cleanup tests
public API parity tests across profiles
```
