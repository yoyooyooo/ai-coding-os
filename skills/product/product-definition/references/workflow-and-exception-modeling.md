# Workflow and Exception Modeling

A workflow describes how actors and systems move business objects from a trigger to an outcome. A state machine describes the lifecycle of one object. They are related but not interchangeable.

## Workflow anatomy

Define:

```text
workflow ID and name
business purpose
trigger
desired outcome
actors and systems
primary business object
preconditions
happy path
alternate paths
exception and recovery paths
handoffs and responsibilities
time constraints and escalation
generated objects, files, notifications, and logs
completion and cancellation conditions
```

## Step table

| Step | Actor/system | Action or event | Object/state before | Rule or decision | Object/state after | Side effects | Evidence/observation |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use swimlanes when handoffs, waiting, or ownership changes are central. Use a state diagram when lifecycle validity is central. Use both when necessary.

## Path families

Model only paths that carry product meaning, but do not stop at the happy path.

```text
happy path         expected successful progression
alternate path     valid variation that still reaches the outcome
exception path     error, missing input, rejection, timeout, or dependency failure
recovery path      retry, correction, resume, rollback, reassign, or reopen behavior
termination path   cancellation, rejection, expiry, withdrawal, or permanent failure
migration path     transition from old data or current behavior into the target workflow
```

## Challenge prompts

For each material step ask:

```text
What if required information is missing or invalid?
What if the responsible actor is absent, leaves, or loses access?
What if two actors act concurrently?
What if an approval is rejected, withdrawn, delegated, or expires?
What if an external service, notification, or file operation fails?
What if the object is edited after downstream work begins?
What if the workflow must pause, resume, transfer, cancel, or reopen?
What if a user has the action permission but not the data relationship?
What is reversible, and what requires a compensating action rather than rollback?
What remains visible after closure or deletion?
```

## Handoffs

A handoff should define:

```text
sender and receiver
object or artifact transferred
acceptance or acknowledgement behavior
time limit and escalation
visibility before and after handoff
what happens if the receiver rejects, ignores, or cannot access it
whether responsibility changes or only work assignment changes
```

## Time and SLA behavior

Separate:

```text
business due date
service-level target
warning threshold
overdue status
pause conditions
calendar and timezone
escalation and notification
completion event
```

Do not encode a deadline without defining its start event, calendar, pause/resume rules, and completion event.

## Concurrency and idempotency at product level

Product definition should state observable expectations without prescribing implementation:

```text
whether duplicate submissions create one or several objects
what the user sees when another person has changed the object
whether an action may be safely retried
which result wins when updates conflict
whether a stale approval or link remains valid
```

Engineering chooses the technical mechanism.

## Workflow completeness check

A workflow is ready when:

```text
entry and completion are clear
responsibility is clear at every step
state transitions are valid
rules and permissions are linked to actions
material alternate, exception, recovery, and termination paths are covered
side effects are observable
open decisions are isolated rather than hidden
```
