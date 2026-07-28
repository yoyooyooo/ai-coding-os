# Intent, Acknowledgement, and Reconciliation

> **Intent Is Not Fact. Optimism Needs Reconciliation.** A local proposal remains provisional until acknowledgement, rejection, timeout, reload, or authoritative projection resolves it.

User intent and accepted facts are separated by time, failure, authorization, and concurrency. A robust frontend makes that gap visible rather than pretending a click is already truth.

## Operation model

```text
intent
  -> operation identity
  -> local pending/optimistic proposal
  -> command sent through product client
  -> acknowledgement, rejection, timeout, or unknown outcome
  -> authoritative projection refresh/realtime result
  -> proposal reconciled or removed
```

## Operation identity

Use a stable operation ID when duplicates, retries, offline work, or unknown outcomes matter. It connects optimistic UI, request, server use case, provider effect, and reconciliation evidence.

## Acknowledgement

An HTTP 200 may acknowledge transport or use-case acceptance. It is not necessarily proof that every downstream external effect completed. Model the product semantics of `accepted`, `pending`, `rejected`, `conflict`, or `unknown`.

## Optimistic updates

Optimism is appropriate when:

```text
rejection is rare and understandable
rollback/reconciliation is clear
the user benefits from immediate response
operation identity prevents duplicate ambiguity
```

Do not optimistically fabricate irreversible or high-risk facts without a visible pending state.

## Conflict

When the server rejects a stale version, preserve the user's intent and current authoritative projection. Offer a meaningful merge, reapply, or reload path rather than silently discarding work.

## Unknown outcome

A client timeout means local waiting ended. The server or provider may have completed. Reconcile by operation ID or authoritative status before resubmitting a non-idempotent command.

## Offline and delayed delivery

Offline intent is a candidate until accepted. Record version, operation identity, ordering assumptions, and user-visible pending/failure states.

## Error semantics

Keep distinct:

```text
validation rejection
permission rejection
business conflict
transport unavailable
timeout / unknown outcome
client defect
```

The interface should communicate what the user can do next.

## Related knowledge

- Use [State roles and ownership](state-roles-and-ownership.md) for proposal versus projection.
- Use [Realtime continuity and reload](realtime-continuity-and-reload.md) for eventual projection updates.
- Use [Client contract evolution](client-contract-evolution.md) for typed outcomes.
- Use `$evolvable-application-architecture` for idempotency and authoritative use cases.
- Use `$product-harness-system` for retry, duplicate, timeout, and reconnect observation.
- Return to the [Frontend Architecture map](../SKILL.md).
