# PRD and Acceptance

A PRD is a testable product contract for a business capability. It is not a design dump, database design, ticket list, implementation plan, or transcript of source documents.

## Module PRD shape

Use only sections that materially improve the specification:

```text
Metadata and version
Background, problem, and outcome
In scope / out of scope / future candidates
Users, roles, and scenarios
Business objects and relationships
End-to-end workflow
State machine and transition rules
Fields and validation
Business rules and calculations
Permissions and data visibility
Notifications and system side effects
Files, versions, logs, retention, and generated artifacts
Errors, empty states, alternate paths, exceptions, and recovery
Metrics and reporting definitions
Product quality attributes
Acceptance criteria
UAT scenarios
Open decisions, dependencies, traceability, and change log
```

## Requirement statements

A useful product requirement states:

```text
actor or trigger
expected business behavior
conditions or scope
observable result
relevant state, permission, rule, metric, artifact, or side effect
```

Avoid requirements that only name a page, button, database field, or technical component.

Use stable requirement IDs when traceability, coordination, or risk justifies them. Do not number every sentence merely to appear rigorous.

## Fields and validation

For each material field define:

```text
business meaning
type and unit
required or optional by action/state
editable and visible conditions
default or source
validation and cross-field rules
localization, timezone, currency, or precision behavior
sensitivity and retention when relevant
```

Keep create, edit, resubmit, import, and API behavior consistent unless the product explicitly requires differences.

## Product interaction states

The product requirement should identify the states design must cover:

```text
normal
empty
loading or processing
validation failure
system failure
partial success
read-only or locked
no permission
expired or stale
conflict or concurrent update
offline or external dependency unavailable when relevant
```

Design owns the final interaction and visual solution.

## Acceptance criteria

Write acceptance criteria as observable behavior:

```text
Given <preconditions>
When <actor action or system event>
Then <business result>
And <state/data/permission/notification/log/metric consequence>
```

Good criteria are:

```text
atomic enough to diagnose failure
observable by business, QA, or an agreed proof method
state-aware
permission-aware when relevant
explicit about side effects and partial failure
linked to a requirement, rule, state, metric, or decision when traceability matters
free of unnecessary implementation detail
```

Include negative and boundary criteria when they carry meaningful risk.

## Acceptance coverage families

Consider:

```text
happy path
validation and boundary values
alternate and rejection paths
permission and data-scope behavior
state transition and invalid action
notification, generated artifact, and logging side effects
external-service failure and retry
concurrent update or duplicate action
localization, timezone, currency, and accessibility
migration or legacy-data behavior
metric and dashboard consistency
```

Not every family applies to every requirement.

## UAT scenarios

UAT should use end-to-end business stories rather than field-by-field checks:

```text
scenario and business purpose
actors and seed data
preconditions
business steps
expected product outcome
expected object and state result
expected permission result
expected notification, file, metric, or log result
evidence to capture
pass/fail notes and defects
```

UAT scope is owned by product definition; UAT execution and evidence belong to the selected business and delivery process.

## PRD review checklist

Before baseline:

```text
scope agrees with the version baseline
terms and objects agree with the product model
workflow and state model agree
rules, permissions, and metrics are not duplicated inconsistently
open decisions are explicit
future candidates are separated from current requirements
acceptance is observable
technical implementation is not prescribed unless it is itself a product constraint
```
