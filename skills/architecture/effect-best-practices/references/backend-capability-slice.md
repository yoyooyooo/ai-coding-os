# Backend Capability Slice

Use this reference when adding or reviewing one backend capability in an Effect-first TypeScript repository. It turns architecture doctrine into an agent-executable slice without creating a project-specific framework.

## Core Thesis

A backend capability slice is a narrow, evidence-bounded path from accepted authority to a runnable surface:

```text
authority refs
  -> contract / protocol boundary
  -> pure domain model
  -> capability port
  -> application flow
  -> adapter live / memory / fake
  -> runtime composition root
  -> API / CLI / worker surface
  -> headless proof
  -> reported claim + not_claimed
```

Do not start from folder shape. Start from the accepted fact, command, or projection the capability owns.

## Topology Rule

Prefer a hybrid topology when a repository has multiple durable architectural packages:

```text
horizontal package = dependency boundary and architectural responsibility
vertical folder    = domain / capability locality inside that package
```

Good shape:

```text
packages/api-contract/src/<capability>/...
packages/domain/src/<domain-or-capability>/...
packages/ports/src/<capability>/...
packages/application/src/<capability>/...
packages/adapters-*/src/<capability>/...
packages/runtime/src/<capability>/...
apps/<surface>/src/<capability>/...
tools/<proof>/src/...
```

Do not collapse architectural responsibilities into one app-local module just to keep files nearby. Also do not spread a tiny capability across every package for symmetry. A layer exists only when the current claim gives it an independent responsibility.


## When To Use

Use this for:

- adding a new backend use case;
- turning a business proof into API / CLI / worker code;
- reviewing whether an Effect implementation kept authority, dependency direction, and proof boundaries intact;
- deciding where Service, Layer, runtime, handler, repo, memory/db implementation, and smoke proof belong.

If the project has no accepted product/domain authority yet, stop at the first proof path or proposal. Do not invent business truth from a template.

## Slice Contract

Before coding, the agent should be able to name:

```text
capability:
authority_refs:
command_or_projection:
surface: api | cli | worker | internal
claim_ceiling:
not_claimed:
verification_commands:
stop_rules:
```

Missing local helpers, test wrappers, smoke command plumbing, or small docs links are implementation scope. Missing product truth, public API/schema posture, security/private-data policy, or claim standard is not.

## Implementation Ladder

### 1. Authority and claim

Read host instructions, SSoT / standards / ADR / protocol docs, and existing tests. Freeze the narrow claim before choosing files.

Good output shape:

```text
This slice proves <capability> at <claim_ceiling>.
It does not prove <not_claimed>.
```

### 2. Contract boundary

Contract modules own wire-safe schemas, route / command literals, DTOs, canonical examples, and stable error envelope fields. They do not do IO, read env, import Node, import adapters, or call application flows.

Use project-local contract technology. In Effect projects this is often `Schema`, `HttpApi`, or explicit DTO literals. The invariant is separation, not a specific package.

### 3. Pure domain model

Pure domain code owns deterministic facts, invariants, mappers, normalizers, parsers, and small state transitions. Prefer ordinary TypeScript functions, `Option`, `Either`, or explicit parse results. Do not wrap pure values in `Effect.succeed` just to look Effect-first.

Domain code must not import HTTP, DB, runtime, adapters, client, UI, or host app packages.

### 4. Capability port

Use `Context.Service` for replaceable side-effectful boundaries. The interface should expose the smallest capability the application flow needs, not a DB client, HTTP SDK, transport, or broad manager.

Port files contain:

```text
Service Tag
minimal interface
stable typed errors when owned at this boundary
```

They do not contain live IO, config reads, runtime creation, or transport types.

### 5. Application flow

Application flow is Effect orchestration. It may:

- fetch Services;
- validate authority-level preconditions;
- coordinate repositories / gateways / publishers;
- choose command vs projection behavior;
- return domain / DTO-ready results;
- fail with typed domain or application errors.

It must not:

- write SQL;
- create DB / HTTP clients;
- read env directly;
- import API handler types;
- call `Effect.runPromise`;
- assemble production Layers.

### 6. Adapter live / memory / fake

Adapters implement ports. Live adapters translate infra details into stable typed errors and preserve behavior expected by the port.

Memory or fake adapters are not throwaway mocks. They should match live semantics for constraints, missing records, sorting, pagination, idempotency, and error tags as far as the claim requires.

DB-backed adapters should enter only when the claim needs persistence. Gate DB integration tests with explicit env and keep default proof fast.

### 7. Runtime composition root

Composition roots assemble Layers, config, resources, observability, and host profile selection. They may create `ManagedRuntime`, provide Layers, open scopes, start servers, or wire workers.

They must not own business rules.

Default rule:

```text
one runtime per app / server / worker profile
not one runtime per request
```

Short-lived command helpers may create a runtime for a one-shot proof, but long-running servers should bind runtime once and reuse it.

### 8. Surface handler

API / CLI / worker handlers are transport adapters. They decode input, call the application flow, map typed errors to the surface envelope, and emit a stable response.

Handlers must not write SQL, instantiate clients, assemble ad hoc Layers, or hide business decisions in transport-specific branches.

HTTP tests should prefer black-box `Request -> Response` or real local server smoke when that is the claim. If a project exposes a test-only handler, ensure it uses the same underlying app path as production.

### 9. Headless proof

Every capability slice needs the smallest honest proof. Good default ladder:

```text
unit tests near pure domain / flow
contract test for API / CLI surface
boundary check for forbidden imports
smoke command with JSON output
optional DB integration gate when persistence is claimed
optional browser/UI proof only when user-visible claim is made
```

Smoke output should include:

```text
claim
claim_ceiling
positive_tokens
not_claimed
not_proven or gaps when useful
```

Do not report UI, DB, provider, production, or realtime claims from an offline fixture.

## File Naming Guidance

Use project conventions first. When absent, group by capability folder and keep filenames semantic enough to be searchable in editor tabs:

```text
packages/<layer>/src/<capability>/<capability>.contract.ts
packages/<layer>/src/<capability>/<capability>.model.ts
packages/<layer>/src/<capability>/<capability>.repo.ts
packages/<layer>/src/<capability>/<capability>.repo.memory.ts
packages/<layer>/src/<capability>/<capability>.repo.live.ts
packages/<layer>/src/<capability>/<capability>.flow.ts
packages/<layer>/src/<capability>/<capability>.runtime.ts
apps/<surface>/src/<capability>/<capability>.http.ts
apps/<surface>/src/<capability>/<capability>.worker.ts
tools/<proof>/src/<capability>.smoke.ts
```

This is a promotion ladder, not a file-generation checklist. Create only layers required by the slice and current claim.

### Collapse Rule

| Situation | Minimum home |
|---|---|
| health/readiness/debug route | app surface, optionally contract |
| pure calculation / validation / value object | domain |
| wire-only DTO / route literal | contract |
| app-private transport glue | app surface |
| DB / provider / external IO | port + adapter |
| workflow / policy / typed error orchestration | application |
| long-lived Layer profile | runtime |
| proof claim | smoke / nearest test |

When a slice touches a layer, the report should name that layer's independent responsibility. If it cannot, the layer should not exist.

## Review Checklist

```text
authority_refs named
contract has no IO
domain is pure unless IO is necessary
ports expose minimum capability
application flow has no infra details
adapters map infra errors to stable typed errors
runtime owns wiring and resources only
handler maps transport errors only at boundary
tests cover behavior, not current defaults
smoke reports claim_ceiling and not_claimed
no stronger claim than evidence supports
```

## Common Failure Modes

- Starting from package layout instead of authority.
- Creating a generic `Service` / `Manager` before naming the capability.
- Building runtime or Layer inside a request handler.
- Returning naked `Error` or leaking provider / SQL errors through the API.
- Treating memory adapter as a mock with different behavior from DB.
- Writing a smoke command that prints success tokens without checking the underlying behavior.
- Calling an offline fixture proof a production, DB, provider, or browser proof.
- Adding compatibility shims for internal callers instead of updating them directly.
