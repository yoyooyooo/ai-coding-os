---
name: effect-best-practices
description: >-
  Implements reliable TypeScript systems with Effect using an explicit adoption
  level, version gate, typed failures, Service/Layer composition, Scope-managed
  resources, structured concurrency, Stream/Queue, runtime ownership, and
  testable adapters. Use when Effect is already present, explicitly selected,
  being evaluated for a concrete pressure, or producing API/type errors. Use
  agentic-architecture for authority, transactions, and module boundaries,
  frontend-architecture for React topology and state ownership, and
  effect-api-app-kit for generating or verifying version-isolated Node HttpApi
  applications.
---

# Effect Best Practices

Use Effect as an execution and resource model, not as a substitute for product
architecture. Choose the lowest adoption level that solves a real pressure and
keep pure domain logic ordinary TypeScript.

## Ownership Contract

```text
Owns: Effect API idioms, version separation, Service/Layer/Runtime mapping,
typed failures, Scope/resource ownership, structured concurrency, Stream/Queue,
Effect tests, and runtime-bound facades.
Delegates: authority/ports/transactions/migrations -> agentic-architecture;
frontend topology/state/query/store/realtime -> frontend-architecture; managed
v3/v4 Node HttpApi scaffolding and verification -> effect-api-app-kit.
Does not decide that every module, helper, repository, or frontend needs Effect.
```

Read [Skill Family Coordination](references/skill-family-coordination.md) when
architecture, frontend, and executable-profile concerns overlap.

## Workflow

1. Inspect `package.json`, lockfile, installed `effect` types, runtime host, and
   existing project architecture. Never mix v3 and v4 examples.
2. Identify the pressure: typed failure, capability replacement, resource
   lifetime, cancellation, concurrency/backpressure, retries/timeouts,
   observability, or deterministic tests.
3. Choose an adoption level from [Adoption Ladder](references/adoption-ladder.md).
4. Keep pure calculation and domain decisions outside Effect unless composition
   materially benefits from lifting them.
5. Define Services only for genuine capabilities; construct them with Layers at
   a composition root; run programs at host boundaries or runtime-bound facades.
6. Model expected errors, defects, interruption, deadlines, and cleanup
   explicitly. Verify finalizers and termination paths.
7. State installed-version evidence and `not_claimed`; beta APIs require an
   exact pinned fixture or local typecheck. For executable Node HttpApi project
   generation, hand off to `effect-api-app-kit` after the design is settled.

## Core Invariants

```text
Effect describes execution; running belongs at an owned boundary
pure function stays pure; Service represents a capability, not every file
Layer constructs dependencies; it does not define product authority
resource acquisition and release share one Scope
child work follows structured lifetime unless explicitly daemonized
expected failures are typed; defects and interruption remain distinguishable
version-specific syntax follows installed d.ts, not memory
```

## Progressive Disclosure

| Need | Read |
|---|---|
| Philosophy and non-goals | [Core Doctrine](references/core-doctrine.md) |
| Decide how much Effect to use | [Adoption Ladder](references/adoption-ladder.md) |
| Service, Layer, Runtime, facade | [Service Layer Runtime](references/service-layer-runtime.md) |
| Error channels and boundary mapping | [Errors and Boundaries](references/errors-and-boundaries.md) |
| Quick API checklist | [Cheatsheet](references/cheatsheet.md) |
| Stable v3 project | [Version v3 Stable](references/version-v3-stable.md) |
| Explicit v4 beta project | [Version v4 Beta](references/version-v4-beta.md) |
| Backend mapping | [Backend Integration](references/backend-capability-slice.md) |
| React/frontend mapping | [Frontend Integration](references/frontend-react-integration.md) |
| Scope and resources | [Scope Resources](references/scope-resources.md) |
| Stream/Queue/concurrency | [Stream Queue Concurrency](references/stream-queue-concurrency.md) |
| Tests and harnesses | [Testing Effect](references/testing-effect.md) |
| CLI | [CLI Contract](references/cli-contract.md) |
| HttpApi | [HttpApi](references/httpapi.md) |
| Optional advanced topics | [Advanced Index](references/advanced-index.md) |

## Output

```text
installed_version; adoption_level; pressure; pure_core; capability_services;
layer_graph; runtime_and_scope_owner; error_model; cancellation_and_backpressure;
frontend_or_backend_mapping; tests; migration_steps; not_claimed.
```
