# Backend Integration

Use this after `evolvable-application-architecture` has established authority, use cases,
transactions, and capability ports. This reference only maps those decisions to
Effect.

## Mapping

```text
application capability port -> Context Service
live adapter                -> Layer using SDK/DB/platform Services
use-case orchestration       -> Effect program/flow
composition profile         -> closed Layer graph + Runtime/entry point
expected failure            -> typed error channel
time/deadline/cancel         -> Clock/Schedule/timeout/interruption policy
resource                     -> Scope/acquireRelease/scoped Layer
fake/conformance adapter     -> test Layer + shared contract tests
```

## Use-Case Shape

```text
handler decodes command
-> Effect flow loads capability Services
-> pure domain function decides typed changes
-> transaction capability commits accepted facts/events/outbox
-> handler maps outcome/error to public response
```

External provider/runtime calls remain outside database transactions. Effect can
sequence transaction A, external call, and transaction B, but it must not blur
the two consistency boundaries.

## Service Granularity

Create Services for real capabilities such as repository transaction, clock, ID,
runtime/provider, object store, mail, payment, or event delivery. Keep pure
aggregate rules and small transformations ordinary functions.

Do not expose one “ApplicationEnv” Service containing every repository and
provider. Do not make each use-case class a Service solely for uniformity.

## Entry Points

CLI, HTTP, worker, and daemon adapters may share Effect flows but own different
public contracts, deadlines, and resource lifetimes. Build profile-specific
Layers at each executable/bootstrap root.

## Proof

Use pure domain tests, fake Layer use-case tests, adapter contract tests,
database transaction/restart tests, resource finalizer tests, and real boundary
smokes according to the claim. A successful in-memory Effect test does not prove
database atomicity or real provider behavior.
