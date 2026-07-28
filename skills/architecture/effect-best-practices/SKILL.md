---
name: effect-best-practices
description: Use when Effect-specific failure, Scope, resource lifetime, structured concurrency, Queue/Stream, Service/Layer/Runtime composition, testing, or installed v3/v4 API semantics determine the correct implementation.
---

# Effect Best Practices

Effect is an execution, dependency, failure, resource, and concurrency model. It does not decide product meaning, fact authority, module/package boundaries, or documentation topology.

Use Effect where its semantics make a real capability clearer. Ordinary TypeScript remains preferable for pure transformations, simple local logic, and code that gains no value from typed failure, structured resources, concurrency, or replaceable capabilities.

## Semantic anchors

- **Use Effect for Execution Pressure, Not Architectural Decoration.** Adopt Effect where failure, resource, dependency, concurrency, or cancellation semantics become clearer.
- **Scope Owns Lifetime.** The Scope that can explain why a resource or child Fiber exists must also explain when and how it ends.
- **Structured Concurrency Leaves No Orphans.** Child work remains attached to an owning lifetime, cancellation policy, budget, and observation surface.
- **Timeout May Mean Unknown Outcome.** A local wait ended; an external effect may still have completed and may require operation identity and reconciliation.
- **Layer Wires Capabilities; It Does Not Own Product Meaning.** Services, Layers, and Runtimes assemble execution dependencies without becoming fact authority or product policy.

## Enter from the current pressure

| Current pressure | Continue into |
| --- | --- |
| it is unclear whether Effect, Promise, plain function, Service, Layer, Queue, Stream, or Actor is warranted | [Mechanism selection](references/mechanism-selection.md) |
| Service, Layer, Runtime, and public API responsibilities are mixed | [Service, Layer, and Runtime](references/service-layer-runtime.md) |
| expected error, defect, interruption, timeout, and unknown outcome are conflated | [Errors, interruption, and unknown outcomes](references/errors-interruption-and-unknown-outcomes.md) |
| a resource, subscription, worker, or Fiber lacks an owner and close path | [Scope, resources, and finalization](references/scope-resources-and-finalization.md) |
| child work, fanout, Queue, Stream, or backpressure may escape control | [Structured concurrency, Queue, and Stream](references/structured-concurrency-queue-stream.md) |
| tests need Clock, Layer substitution, interruption, retry, or finalizer observation | [Testing Effect](references/testing-effect.md) |
| the project uses HttpApi or an Effect backend boundary | [HttpApi integration](references/httpapi-integration.md) |
| Effect enters a React or frontend host | [Frontend integration](references/frontend-integration.md) |
| Effect Config, Cause, Span, Fiber, or resource observability needs a boundary | [Effect-specific configuration and observability](references/config-and-observability.md) |
| a long-lived state machine may benefit from a pure deterministic kernel and Actor interpreter | [Deterministic kernel and Actors](references/deterministic-kernel-and-actors.md) |
| a greenfield project needs deterministic Effect file roles | [Default Effect module conventions](references/default-effect-module-conventions.md) |
| concrete API syntax may differ between installed versions | [Version grounding](references/version-grounding.md) |
| scenario mappings help | [Scenario examples](references/scenario-examples.md) |

These are independent decisions, not an Effect adoption ladder.

## Failure and lifetime model

Keep these meanings distinct:

```text
expected failure  a modeled result the caller can handle
defect            an implementation error or violated assumption
interruption      cooperative cancellation from the owning Scope
timeout           a local waiting policy
unknown outcome   an external effect may or may not have completed
```

Retry requires an understanding of idempotency, duplicate effects, deadline, backoff, and unknown outcome. Fail fast inside the smallest untrusted Scope; an outer owner decides whether to retry, degrade, isolate, or recover.

Resources and child work belong to the Scope that can explain why they exist. A finalizer does not make a lifetime correct when the resource was created in the wrong host.

## Portable Effect default

When the project has no coherent Effect naming convention, use [Default Effect module conventions](references/default-effect-module-conventions.md). The default is intentionally small and does not require one Service or Layer per helper.

## Common smells

- every helper returns Effect without clearer capability, failure, or lifetime semantics;
- every feature, query callback, or component constructs a Runtime or live Layer;
- one catch maps expected failure, defect, and interruption to the same string;
- an unbounded Queue or detached Fiber hides overload and shutdown behavior;
- timeout is reported as "provider failed" without operation identity;
- a Service mirrors one pure function for directory symmetry;
- example code comes from another major version and is assumed correct without local verification;
- tests replace internal implementation rather than a capability boundary.

## Adjacent owners

- Fact authority, transactions, Ports, and application modules belong to `$evolvable-application-architecture`.
- Frontend Query/store/realtime and host ownership belong to `$frontend-architecture`.
- Runtime timeout, cancellation, restart, and leak reproduction belong to `$product-harness-system`.
- General build/release, CLI, and organization-wide observability do not become Effect semantics merely because a project uses Effect.

## Output principle

Choose the smallest Effect mechanism that clarifies the current capability, failure, resource, or concurrency problem. State installed-version evidence when syntax matters. Make resource owner, cancellation, unknown outcome, and key observations explicit. Do not impose a uniform Service/Layer graph or scaffold for visual consistency.
