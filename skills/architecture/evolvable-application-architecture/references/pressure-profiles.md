# Pressure Profiles

Select architecture intensity per vertical slice, not once for the repository.
A product may contain P0 and P4 slices at the same time.

Record the **pressure signals** first; the P-level is a derived minimum profile,
not the source of truth.

```yaml
pressure_signals:
  - durable_fact
  - concurrent_update
  - external_effect
  - retry
  - process_restart
  - outcome_unknown
  - money
minimum_profile: P4
```

Different slices at the same level may require different mechanisms because the
signals differ.

## P0 — Simple / Local

Signals: local, reversible, process-private state; no durable accepted fact or
external lifecycle.

Minimum shape:

```text
private semantic module
explicit command/query functions when useful
clear dependency direction
proportionate tests
```

Usually avoid ports for internal helpers, event buses, candidates, sagas,
outbox, or independent deployables.

## P1 — Transactional

Signals: durable accepted facts, concurrent updates, restart correctness, or
material audit identity.

Add as applicable:

```text
named authority and consistency domain
transaction / unit of work
expected version or lock policy
durable idempotency
specific outcome + CommitReceipt
fact + event/audit/outbox atomicity when the side record represents acceptance
```

## P2 — External Capability

Signals: provider, gateway, device, external executor, plugin, model, remote
system, vendor lifecycle, or realistic fake/replay seam.

Add:

```text
application-owned capability contract
adapter normalization and stable error taxonomy
Observation / Candidate / Receipt / OutcomeUnknown boundary
external call outside database transaction
materialization or reconciliation transaction
capability conformance evidence
```

The external system may be authoritative for its own source claim while the
application remains authoritative for local product meaning.

## P3 — Distributed / Replayable

Signals: multiple processes, queues, retries, partial failure, independent
clients, partitions, or independently owned lifecycle.

Add as required:

```text
durable intent / outbox / inbox
retry and dedupe semantics
ordering or causal frontier
timeout and unknown-outcome handling
reconciliation / compensation
restart and replay proof
partition, backpressure, cancellation, and shutdown model
short compatibility epochs
```

Exactly-once materialization does not imply exactly-once external execution.

## P4 — Governed / High-Risk

Signals: money, permissions, safety, privacy, regulated data, irreversible
external effect, multi-party approval, adversarial participant, or high-cost
automation.

Add:

```text
policy and schema versions
provenance and decision records
proposal / approval / execution / acceptance separation
least privilege and disclosure boundaries
retention and redaction
forensic evidence
failure injection and realistic environment proof
explicit human or external-authority stop lines
```

## Selection Rules

1. Choose the highest real signal for the traced slice.
2. Apply lower-level requirements only when their signal is present.
3. Record `not_applicable` instead of fabricating mechanisms.
4. Do not treat anticipated scale, framework fashion, vendor marketing, file
   count, or model confidence as pressure evidence.
5. Upgrade or downgrade when observed ownership, lifecycle, trust, data,
   failure, or proof pressure changes.
6. Generate blind-spot probes from signals: restart, duplicate delivery,
   timeout-after-start, stale writer, cursor gap, cancellation, migration, or
   irreversible action.

## Quick Signals

| Signal | Minimum profile |
| --- | --- |
| local draft/settings | P0 |
| durable business transition | P1 |
| payment/LLM/device/plugin/remote API | P2 |
| queue/retry/restart/partial failure | P3 |
| permission/money/safety/privacy/irreversible action | P4 |
