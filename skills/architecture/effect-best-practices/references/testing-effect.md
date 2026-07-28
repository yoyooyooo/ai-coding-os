# Testing Effect

Test the capability contract, failure semantics, lifetime, and concurrency property that matter. Do not test Effect syntax for its own sake.

## Capability substitution

Provide test implementations at the Service or application Port boundary. A fake should model the relevant behavior and failure, not simply return success.

## Clock and scheduling

Use TestClock or the installed-version equivalent when deadlines, retry, sleep, debounce, timeout, or scheduling are part of the property. Avoid real waiting in unit tests.

## Failure channels

Verify expected failure, defect, interruption, timeout, and unknown outcome separately when the capability distinguishes them.

## Resource tests

Observe:

```text
acquisition occurs once per intended lifetime
finalizer runs on success, failure, and interruption
partial acquisition is cleaned safely
host shutdown leaves no child work or live resource
cleanup failure remains visible
```

## Concurrency tests

Use deterministic coordination where possible:

```text
barriers or latches
controlled Queue/Deferred
versioned state
bounded parallelism
explicit interruption
```

Avoid tests that pass only because of arbitrary `sleep`.

## Retry and idempotency

Record operation identity and call count. Test duplicate, timeout, provider success after local timeout, and reconciliation. A retry unit test alone cannot prove live-provider idempotency.

## Layer tests

Test that host composition provides the required Services and closes them. Do not freeze internal Layer order when only the resulting capability matters.

## Runtime boundary

When a framework callback runs an Effect through a Runtime, test error translation, cancellation, and resource lifetime at that boundary.

## Test the test

Introduce a known failure or mutate a boundary to confirm that the test and observation surface actually detect the property.

## Related knowledge

- Use [Service, Layer, and Runtime](service-layer-runtime.md) for substitution boundaries.
- Use [Scope, resources, and finalization](scope-resources-and-finalization.md) for resource properties.
- Use [Version grounding](version-grounding.md) for concrete test APIs.
- Use `$product-harness-system` for dependency realities and claim limits.
- Return to the [Effect map](../SKILL.md).
