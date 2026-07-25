# Evidence Harness

Architecture should make important claims executable and observable. Harnesses
provide discovery and observation surfaces; execution strategy remains with the
active engineering context.

## Core distinction

```text
Harness execution
  -> structured observations

Agent interpretation against project authority
  -> bounded supported conclusions

unexercised adjacent properties
  -> not_proven / not_claimed
```

The same Agent may execute and interpret. Keep the epistemic distinction between
what ran and what is inferred; do not require a separate verifier by default.

## Evidence ladder

Choose the smallest surface that can honestly test the current property. An
Agent may enter at any appropriate level; this is a capability menu, not a fixed
stage gate.

```text
static dependency / visibility check
unit or pure invariant test
offline fixture
strict deterministic replay
fake adapter conformance
durable-store / restart proof
transport, queue, and projection proof
browser or interface proof
real external adapter opt-in
failure injection / partition proof
load, soak, and local-stack or staging smoke
```

A lower level supports but does not prove a higher-level claim. Functional tests
do not prove throughput, privacy, crash safety, or replaceability.

## Lightweight contracts

`$ai-coding-os-suite-contracts` provides optional portable Harness Descriptor
and Result schemas. Load them by Skill name rather than assuming a sibling path.

A normal local result may be as small as:

```yaml
harness: order.checkout.retry
status: pass
observed:
  order_version_before: 7
  order_version_after: 8
  duplicate_version_after: 8
supports:
  - duplicate retry did not create a second committed transition
not_proven:
  - multi-process contention
  - real provider behavior
```

Add commit, lockfile, fixture, scenario, runtime, and artifact provenance only
when evidence must survive across Agents, commits, release decisions, audit, or
high-risk operation.

## Boundary checks

Mechanically enforce durable edges where useful:

- forbidden imports/dependencies;
- public mutable state access;
- core dependence on provider SDKs or ORM records;
- transport access to authority persistence;
- composition-root product writes;
- direct UI mutation of product authority;
- fake implementation in production composition;
- stale authority-epoch writes;
- test-only APIs exported in production;
- legacy bridge callers after cutover.

Use hard errors for durable violations. Use warnings when a universal rule would
replace sound engineering judgment with style enforcement.

## Conformance suites

A replaceable capability may need shared behavior checks for:

```text
normalized output and error taxonomy
deadline, cancellation, retry, idempotency
capability/version reporting
redaction/privacy
restart/replay
unknown outcome and reconciliation
explicit rejection of unsupported features
```

Run a deterministic fake/replay and at least one realistic adapter path before
claiming behavioral replaceability.

## Negative controls

Negative controls are a high-value technique, especially for authorization,
idempotency, recovery, dedupe, cursor gaps, and version conflicts. The harness
framework itself should prove that it can fail. Do not mechanically require a
mutation test for every simple pure function.

## Isolation matches the claim

```text
pure function claim          -> ordinary process-local test may be enough
resource cleanup claim       -> owned Scope/lifecycle needed
restart durability claim     -> real persistence plus restart needed
browser reload claim         -> real browser context needed
cross-request isolation      -> multiple requests/instances needed
```

Clean-room ceremony is not universal; isolation is a proof condition.

## Harness boundary

Harnesses may seed through supported fixture/setup paths, drive formal
interfaces, replay traces, and collect observations. They must not create
accepted facts through a privileged alternate path when the claim concerns
production materialization.

Do not copy a second business algorithm into test utilities. Do not report fake,
replay, headless, render, or declared local-stack/staging evidence as a stronger real
surface than actually exercised.

## Deletion proof

A migration is incomplete until evidence shows:

- intended callers use the new path;
- old writes are fenced or impossible;
- restart and idempotency pass on the new path when claimed;
- projections/backfill agree within the stated ceiling;
- bridge dependencies are zero;
- old code/schema paths are deleted or explicitly retained.
