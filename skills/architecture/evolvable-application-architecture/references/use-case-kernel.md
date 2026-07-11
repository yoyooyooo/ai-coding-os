# Use-Case Kernel

Use cases are controlled paths by which intent, observations, and candidates
become accepted facts.

## Vocabulary

```text
Intent:     a requested goal before acceptance.
Command:    an authoritative request to attempt a governed transition.
Observation:a report about an external or computed condition.
Candidate:  a non-authoritative proposal that may be materialized.
Decision:   the governed disposition of a command or candidate.
Query:      a read of accepted state.
Projection: a purpose-built representation of accepted or observed state.
Receipt:    evidence from an external effect or committed transition.
```

Realtime stores, caches, indexes, and UI state carry projections. They are not
alternate command or fact models.

## Command Context

Inject nondeterministic and policy-sensitive inputs:

```text
actor / principal
request or correlation id
client mutation / idempotency key
clock value
policy and schema snapshot/version
consistency domain / authority epoch
causal frontier / expected aggregate version
trace context
deadline and cancellation
```

Do not let authority logic reach into environment variables, global clocks,
random generators, request globals, or deployment configuration when replay or
concurrency correctness matters.

## Authoritative Command Path

Use this when the caller is allowed to request the transition directly:

```text
1. normalize Command + CommandContext
2. load the minimum required facts
3. authorize and validate
4. check idempotency, epoch, and expected version
5. calculate typed ChangeSet / Decision
6. atomically commit facts + event/audit/outbox
7. return specific outcome + CommitReceipt
8. publish or invalidate projections after commit
```

A command can be rejected, conflict, become a no-op, or return an already
committed idempotent result. It does not need an artificial candidate stage.

## Observation and Candidate Path

Use this when input comes from an external, inferred, imported,
nondeterministic, or otherwise non-authoritative source:

```text
1. authenticate source and normalize Observation
2. preserve provenance, source version, and capability evidence
3. derive or accept a typed Candidate
4. load governing facts and policy snapshot
5. decide freshness, dedupe, authorization, conflict, and trust
6. calculate a typed materialization plan
7. atomically commit accepted facts + decision/evidence/outbox
8. return disposition + CommitReceipt
```

Rejected candidates remain evidence when policy requires it; they do not become
product facts by transport acknowledgement.

## External Effects

External calls belong outside the database transaction:

```text
transaction A: accept intent and create durable pending work/outbox
external call: execute through capability port
transaction B: record receipt, reconcile, and materialize resulting facts
```

For irreversible or ambiguous effects, model `OutcomeUnknown`, reconciliation,
and compensation explicitly. Exactly-once materialization does not imply the
external side effect executed exactly once.

## Typed Changes and Outcomes

Prefer use-case-specific types over direct mutation of a shared state object or
one universal payload.

Examples:

```text
ApproveRefundChangeSet
ImportShipmentObservationDecision
MaterializeRiskAssessmentCandidate
PublishDatasetVersionChangeSet
AcceptCollaborativeOperationChangeSet
```

Return:

```text
UseCaseResult<SpecificOutcome> {
  value
  CommitReceipt
}
```

The receipt may contain accepted fact refs, event/outbox refs, idempotency
disposition, version/causal frontier, and trace/evidence refs.

## Idempotency and Replay

Idempotency must survive process restart. Durable idempotency records,
source-version uniqueness, or reconstructable accepted facts are stronger than
in-memory response caches.

Replay should rebuild projections or re-evaluate deterministic decisions without
repeating external effects. Retain enough source, policy, schema, version, and
adapter evidence to explain the result without retaining unnecessary secrets.

## Realtime Rule

```text
commit accepted fact
  -> append/deliver projection event
  -> client dedupes, applies, or backfills
```

Never claim business completion from a websocket frame, queue acknowledgement,
provider callback, scheduler wake-up, or adapter receipt before authoritative
materialization.
