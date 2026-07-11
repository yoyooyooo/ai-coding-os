# Evidence Harness

Architecture claims need evidence at the boundary they describe.

## Evidence Ladder

Use the smallest honest level:

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
failure injection / chaos / partition proof
load, soak, and production-near smoke
```

A lower level supports but does not prove a higher-level claim. Functional tests
do not prove throughput, privacy, crash safety, or replaceability.

## Evidence Envelope

Capture:

```text
claim
proof_path
commands_or_scenarios
positive assertions or evidence tokens
authority checked
consistency and transaction boundary checked
adapter/profile and capability version
restart/replay/idempotency result
ordering/backfill/reconciliation result
redaction/privacy result
load/failure envelope when claimed
not_claimed
not_proven
next_gap
```

Use `not_claimed` for adjacent capabilities outside intended scope. Use
`not_proven` when the property should hold but was not checked.

## Boundary Checks

Mechanically enforce high-value rules where possible:

- forbidden imports/dependencies;
- public mutable state access;
- adapter dependence on infrastructure internals;
- transport access to authority persistence;
- core dependence on vendor SDKs;
- composition-root fact writes;
- direct UI mutation of product authority;
- stale authority-epoch writes;
- test-only APIs exported in production;
- legacy bridge callers after cutover.

## Conformance Suites

Each replaceable capability should have contract tests for applicable behavior:

```text
normalized output
error taxonomy
deadline and cancellation
idempotency / retry / duplicate receipt
capability reporting and version negotiation
redaction and privacy
fallback or explicit rejection
restart and replay
unknown-outcome and reconciliation
```

Run fake/replay plus at least one realistic adapter path before claiming
replaceability.

## Distributed and Performance Claims

For P3/P4 slices, test the failure shape, not only the happy path:

```text
crash before and after commit
late duplicate delivery
reordering and gaps
network timeout after send-started
leader/lease change
partial dependency outage
hot partition and backpressure
restart with pending work
```

A benchmark must state dataset, concurrency, topology, hardware/profile,
duration, percentile, error budget, and saturation behavior. Do not translate an
architectural absence of global locks into an unsupported throughput claim.

## Harness Boundary

Harnesses may seed through supported fixture/setup paths, drive interfaces,
replay traces, and collect evidence. They should not create accepted facts
through a privileged alternate path when the claim concerns production
materialization.

Move smoke-only builders, proof report construction, and test fixtures out of
production application APIs when they begin to define a second architecture.

## Deletion Proof

A migration is incomplete until evidence shows:

- all intended callers use the new path;
- old writes are impossible or fenced;
- restart and idempotency pass on the new path;
- projections/backfill agree within the stated ceiling;
- bridge dependencies are zero;
- old code and schema paths are deleted or explicitly retained.
