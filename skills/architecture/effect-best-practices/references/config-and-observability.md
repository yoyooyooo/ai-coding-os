# Effect-Specific Configuration and Observability

This reference covers configuration and observability only where Effect semantics are material. General organization-wide logging and configuration standards belong elsewhere.

## Configuration

Use Effect Config/Schema or the installed-version equivalent when it helps:

```text
decode environment and external config at the host boundary
produce typed construction input for Layers
model missing/invalid configuration in the correct error channel
substitute configuration in tests
avoid deep reads of process environment
```

Do not make stable product invariants arbitrary configuration. Keep changeable policy under accountable product ownership.

## Secrets

Read secret references through the host's controlled secret mechanism. Avoid placing secrets in logs, errors, generated docs, or prompt-visible configuration.

## Cause

Retain Cause where defects, interruption, parallel failure, and nested errors matter. Translate to a stable public outcome at the boundary while keeping diagnostic detail for authorized observation.

## Spans and context

Propagate correlation/operation identity, request context, and spans through the Effect graph. Do not use a global mutable context object.

## Resource observability

Useful Effect-specific signals include:

```text
Fiber identity and parentage
interruption reason
retry attempt and deadline
Queue depth and backpressure
Stream lag and consumer state
Scope acquisition/finalization
finalizer failure
Runtime/Layer construction count
```

Measure only what supports diagnosis, capacity, or a product quality property.

## Log once at the semantic boundary

Avoid logging the same error at every layer. Add context where ownership or meaning changes, then preserve Cause for the final authorized boundary.

## Testing observability

Test that key failures, interruption, and resource cleanup remain observable. A structured log shape does not prove the underlying behavior.

## Related knowledge

- Use [Errors, interruption, and unknown outcomes](errors-interruption-and-unknown-outcomes.md) for failure meaning.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for lifetime signals.
- Use [Testing Effect](testing-effect.md) for evidence.
- Use `$docs-governance` for durable operational knowledge and runbook placement.
- Return to the [Effect map](../SKILL.md).
