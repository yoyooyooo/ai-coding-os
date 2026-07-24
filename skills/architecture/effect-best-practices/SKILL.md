---
name: effect-best-practices
description: >-
  Effect execution architecture for TypeScript Services, Layers, runtimes,
  Scope, typed failures, structured concurrency, Stream, and Queue. Use when
  Effect is present or selected, when deciding its adoption depth, or when
  resolving version-specific API and type failures.
---

# Effect Best Practices

Use Effect as an execution and resource model. Product authority and source
boundaries remain upstream decisions. Choose the lowest adoption level that
solves real pressure; keep pure domain calculation ordinary TypeScript.

## Ownership

```text
Owns:
  exact-version Effect API idioms
  Service/Layer/Runtime mapping
  typed failures, defects, interruption, cancellation, deadlines
  Scope and resource ownership
  structured concurrency, Stream, Queue
  Effect tests and runtime-bound facades
  Effect-specific mapping of live/fake implementations to Layers, runtimes, and scopes

Adjacent owners:
  authority/ports/transactions/modules/source topology -> $evolvable-application-architecture
  frontend topology/state/query/store/realtime -> $frontend-architecture
  managed HttpApi scaffold -> $effect-api-app-kit
  docs placement -> $docs-governance
```

## Effect Pass

| Step | Completion criterion |
| --- | --- |
| Version gate | `package.json`, lockfile, installed `effect` declarations, and host runtime establish the exact API surface. |
| Pressure | Typed failure, replacement, lifetime, cancellation, concurrency/backpressure, retry/timeout, observability, or deterministic-test pressure is named. |
| Adoption | One level from [Adoption Ladder](references/adoption-ladder.md) is selected and every Effect abstraction serves the named pressure. |
| Capabilities | Services represent genuine capabilities; pure calculations remain pure; expected errors are typed at the right boundary. |
| Composition | Layers are built at named host roots; programs run only at owned boundaries or explicit facades. |
| Lifetime | Acquisition, child work, interruption, deadlines, finalizers, and termination share a coherent Scope. |
| Proof | Tests exercise the claimed error, cancellation, resource, concurrency, or version behavior; adjacent behavior is `not_proven`. |

Use `$effect-api-app-kit` only after architecture, source topology, and Effect
major-version choices are settled.

## Invariants

```text
Effect describes execution; running belongs at an owned boundary
pure function stays pure; Service represents a capability
Layer constructs dependencies; it does not define product authority
Layer graph != authority graph != package graph
resource acquisition and release share one Scope
child work follows structured lifetime unless explicitly daemonized
expected failures, defects, and interruption remain distinguishable
version-specific syntax follows installed declarations
```

## Topology and Naming

Application naming comes from `$evolvable-application-architecture`:

```text
<subject>.<operation>.use-case.ts
<subject>.<capability>.port.ts
<subject>.public.ts
<subject>.wiring.ts
<host>.composition.ts
```

Effect adds qualifiers only where they carry runtime meaning:

```text
<subject>.<capability>.<provider>.live.ts
<subject>.<capability>.memory.fake.ts
<host>.runtime.ts
<subject>.<purpose>.stream.ts
```

A genuine Effect-native library may use `.service.ts` for a Service key;
`service` remains guarded elsewhere. Each deployable host owns its runtime and
live Layer graph. Reusable packages export contracts, normalized errors,
programs, or Layer factories rather than an unowned global runtime.

## Read When Needed

| Condition | Reference |
| --- | --- |
| Establishing philosophy and boundaries | [Core Doctrine](references/core-doctrine.md) |
| Choosing adoption depth | [Adoption Ladder](references/adoption-ladder.md) |
| Designing Service, Layer, Runtime, or facade | [Service Layer Runtime](references/service-layer-runtime.md) |
| Modeling errors | [Errors and Boundaries](references/errors-and-boundaries.md) |
| Checking common APIs | [Cheatsheet](references/cheatsheet.md) |
| Working in stable v3 | [Version v3 Stable](references/version-v3-stable.md) |
| Working in explicit v4 beta | [Version v4 Beta](references/version-v4-beta.md) |
| Mapping a backend slice | [Backend Integration](references/backend-capability-slice.md) |
| Mapping React/frontend use | [Frontend Integration](references/frontend-react-integration.md) |
| Owning resources | [Scope Resources](references/scope-resources.md) |
| Handling Stream/Queue/concurrency | [Stream Queue Concurrency](references/stream-queue-concurrency.md) |
| Testing Effect code | [Testing Effect](references/testing-effect.md) |
| Building a CLI | [CLI Contract](references/cli-contract.md) |
| Building HttpApi | [HttpApi](references/httpapi.md) |
| Mapping modules and filenames | [Module Organization Coordination](references/module-organization-coordination.md) |
| Reaching advanced branches | [Advanced Index](references/advanced-index.md) |

## Output

```text
installed_version
adoption_level
pressure
pure_core
capability_services
layer_graph
runtime_and_scope_owner
error_model
cancellation_and_backpressure
source_naming_mapping
frontend_or_backend_mapping
tests_and_harnesses
migration_steps
not_proven
not_claimed
```
