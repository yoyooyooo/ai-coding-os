# Pressure Profiles

Select architecture intensity per vertical slice, not once for the whole
repository. A product may contain P0 and P4 slices at the same time.

## P0 — Simple / Local

Use when one process and one trusted writer own low-risk state.

Minimum shape:

```text
private module state
explicit command/query functions
clear dependency direction
basic tests
```

Usually avoid ports for internal helpers, event buses, candidate ledgers,
plugins, sagas, outbox, and microservices.

Promote when durable concurrency, an external capability, or independent
lifecycle appears.

## P1 — Transactional

Use when accepted durable facts, concurrent updates, or restart correctness
matter.

Add:

```text
named authority cell
transaction / unit of work
expected version or lock policy
durable idempotency
specific outcome + CommitReceipt
fact + event/audit atomicity when events represent accepted change
```

Do not add a candidate pipeline unless the input is genuinely
non-authoritative.

## P2 — External Capability

Use when a provider, gateway, device, external executor, plugin, model, or
remote system influences behavior.

Add:

```text
application-owned capability port
adapter normalization and stable error taxonomy
Observation/Candidate/Receipt boundary
external call outside database transaction
materialization or reconciliation transaction
capability conformance evidence
```

The external system may be authoritative for its own source claim while the
application remains authoritative for local product meaning.

## P3 — Distributed / Replayable

Use when work spans processes, retries, queues, partial failure, or
independently deployed clients.

Add as required:

```text
durable intent/outbox/inbox
retry and dedupe semantics
ordering or causal frontier
timeout and unknown-outcome handling
reconciliation / compensation
restart and replay proof
partition and backpressure model
short, explicit compatibility epochs
```

Do not infer exactly-once execution from exactly-once materialization.

## P4 — Governed / High-Risk

Use for money, permissions, safety, privacy, regulated data, irreversible
external effects, multi-party approval, adversarial participants, or high-cost
automation.

Add:

```text
policy and schema versions
provenance and decision records
separation of proposal, approval, execution, and acceptance
least privilege and disclosure boundaries
retention/redaction rules
audit and forensic evidence
failure injection and production-near proof
explicit human stop lines
```

## Selection Rules

1. Choose the highest *real* pressure for the traced slice.
2. Apply lower-level requirements cumulatively only when relevant.
3. Record `not_applicable` for branches the slice does not use.
4. Do not treat anticipated scale, vendor marketing, or folder count as
   pressure evidence.
5. Upgrade a boundary when observed failures, ownership, deployment, trust,
   data, or proof needs justify it.
6. Downgrade recommendations when the complexity cost exceeds the pressure.

## Quick Decision Table

| Signal | Minimum profile |
|---|---|
| local draft or settings | P0 |
| durable business transition | P1 |
| payment gateway, LLM, device, plugin, remote API | P2 |
| queue/retry/restart/partial failure | P3 |
| permission, money, safety, privacy, irreversible action | P4 |
