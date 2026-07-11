# TypeScript Backend Adapter

Use for Node.js, Bun, Deno, Edge runtimes, serverless functions, or backend
services written in TypeScript.

## Idiom Mapping

```text
Authority cell   -> module/package with unexported state and command/query API
Capability port  -> interface or structural type owned by application layer
Adapter          -> SDK/transport/database implementation module
Composition root -> bootstrap.ts, server.ts, worker.ts, or profile module
ChangeSet        -> discriminated union or use-case-specific object
CommitReceipt    -> readonly typed result
Boundary guard   -> package exports, import rules, lint/architecture tests
```

Interfaces are useful at genuine boundaries. Do not add `IThingService` for
every class or create a DI token for every helper.

## Boundary Validation

TypeScript types disappear at runtime. Validate untrusted adapter and transport
payloads at the edge with a schema/decoder, then convert them to normalized
application types. Do not leak `any`, provider SDK response types, ORM records,
or raw JSON through the core.

## Module and State Rules

- keep mutable module state private;
- avoid process-global service locators and singleton domain stores;
- expose explicit commands and queries;
- pass `CommandContext` rather than reading request globals or environment deep
  in the call graph;
- make cross-cell references explicit IDs/value objects;
- keep HTTP framework request/response objects in input adapters.

## Example Shape

```ts
export interface IdentityVerificationPort {
  verify(request: VerificationRequest): Promise<VerificationCandidate>
}

export type UseCaseResult<T> = Readonly<{
  value: T
  receipt: CommitReceipt
}>

export const createApplication = (deps: ApplicationDeps): ApplicationFacade => {
  // composition only; no product transition rules
}
```

If using Effect, Services/Layers can implement capability ports and composition
profiles. Do not turn every internal pure module into a Service solely for
uniformity.

## Persistence

Pass an explicit transaction context or unit of work into repositories used by
one application operation. Commit business rows and event/audit/outbox together.
Do not treat a process-global ORM client as the transaction boundary.

Prefer use-case-specific outcomes and discriminated unions over one giant DTO
with optional properties for every command.

## Composition and Profiles

Construct SDK clients, adapters, credentials, decoders, and resource scopes in
bootstrap or profile modules. A reusable application module should not import
every provider implementation or branch on vendor names.

## Mechanical Proof

Use package `exports`, TypeScript project references where useful, lint/import
rules, dependency-cruiser-style checks, contract tests, runtime decoder tests,
database integration tests, restart/replay scenarios, and migration tests.
