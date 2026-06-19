# Use-Case Kernel

Use cases are the controlled paths by which intent and candidates become
accepted facts.

## Command, Query, Candidate, Projection

```text
Command: requested change or decision.
Query: read of accepted state.
Candidate: unaccepted external or computed proposal.
Projection: purpose-built representation of accepted or observed state.
```

Realtime, caches, and UI stores carry projections. They are not alternate
command or fact models.

## Command Context

Inject nondeterministic and policy-sensitive inputs:

```text
actor / principal
request or correlation id
client mutation / idempotency key
clock value
policy snapshot or version
causal frontier / expected aggregate version
trace context
deadline and cancellation
```

Do not let domain code reach directly into environment variables, global clocks,
random generators, or deployment configuration when deterministic replay or
concurrency correctness matters.

## Materialization Pipeline

```text
1. accept command or normalized candidate
2. load the minimum required facts
3. authorize and validate
4. check idempotency and expected version / freshness
5. calculate typed changes and decisions
6. atomically commit facts + event/outbox/audit
7. return specific outcome + CommitReceipt
8. publish or invalidate projections after commit
```

External model/runtime/tool calls belong outside the database transaction:

```text
transaction A: accept intent and create durable pending work
external call: execute through capability port
transaction B: validate and materialize returned candidate
```

## Typed Changes

Prefer a use-case-specific change set over direct mutation of a shared state
object. A change set makes review, transaction planning, replay, and adapter
conformance explicit.

Examples:

```text
AcceptMessageChangeSet
GovernIntentChangeSet
MaterializeRuntimeCandidateChangeSet
ApprovePaymentChangeSet
PublishResultVersionChangeSet
```

Do not force every change through one untyped map or universal event payload.

## Idempotency and Replay

Idempotency should survive process restart. Durable idempotency records or
reconstructable accepted facts are stronger than in-memory outcome caches.

Replay should rebuild projections or re-evaluate deterministic materialization
without repeating external side effects. Store enough source, policy, version,
and adapter evidence to explain what happened without retaining secrets or
private reasoning unnecessarily.

## Realtime Rule

```text
commit accepted fact
  -> append/deliver projection event
  -> client applies or backfills
```

Never claim business completion because a websocket frame, runtime event, or
transport acknowledgement was observed before the authoritative commit.
