# Evidence Harness

Architecture claims need evidence at the boundary they describe.

## Evidence Ladder

Use the smallest honest level:

```text
static dependency / visibility check
unit or pure invariant test
offline fixture
strict replay
fake adapter conformance
durable-store / restart proof
transport and projection proof
browser or interface proof
real provider/runtime opt-in
production-near smoke
```

A lower level supports but does not prove a higher-level claim.

## Evidence Envelope

Capture:

```text
claim
proof_path
commands_or_scenarios
positive assertions or tokens
authority checked
boundary checked
adapter/profile
restart/replay/idempotency result
redaction/privacy result
not_claimed
not_proven
next_gap
```

Use `not_claimed` for adjacent capabilities outside the intended scope. Use
`not_proven` when the property should hold but was not checked.

## Boundary Checks

Mechanically enforce high-value rules where possible:

- forbidden imports/dependencies;
- public mutable state access;
- adapter dependence on infrastructure internals;
- transport access to domain persistence;
- core dependence on vendor SDKs;
- composition-root fact writes;
- direct UI mutation of product authority;
- test-only APIs exported in production.

## Conformance Suites

Each replaceable capability should have contract tests covering normalized
output, error taxonomy, cancellation/deadline, idempotency, capability
reporting, redaction, and fallback/rejection semantics.

Run at least fake/replay plus one realistic adapter path before claiming
replaceability.

## Harness Boundary

Harnesses may seed through supported fixture/setup paths, drive interfaces,
replay traces, and collect evidence. They should not create accepted facts
through an alternate privileged path when the claim concerns production
materialization.

Move smoke-only builders, proof report construction, and test fixtures out of
production application APIs when they begin to define a second architecture.

## Deletion Proof

A migration is incomplete until evidence shows:

- all intended callers use the new path;
- old writes are impossible;
- restart and idempotency pass on the new path;
- projections/backfill agree within the stated ceiling;
- bridge dependencies are zero;
- old code and schema paths are deleted or explicitly retained.
