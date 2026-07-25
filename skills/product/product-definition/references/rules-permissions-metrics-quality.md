# Rules, Permissions, Metrics, and Quality

These cross-cutting concerns often become inconsistent when buried in page descriptions. Define them independently when they span several workflows or modules.

## Business rule taxonomy

```text
eligibility       who or what qualifies
validation        what input is accepted
invariant         what must always remain true
calculation       how a value is derived
classification    how an object is categorized
routing           which path, owner, or destination applies
precedence        which rule wins when several apply
time               start, duration, pause, expiry, and escalation
numbering         identity or display-code generation
side effect        generated object, notification, log, or downstream update
retention          archive, deletion, anonymization, or legal hold
```

A rule should include:

```text
stable ID when reuse or traceability justifies it
plain-language statement
trigger and scope
inputs and output
exceptions and precedence
source or decision
owner and effective version
observable acceptance consequence
```

Do not write implementation pseudocode as the only business rule. A technical design may later translate the accepted rule.

## Enumerations and classifications

For each value define:

```text
code
business label
definition
when it may be selected or derived
whether it is active, deprecated, or future
mapping from legacy values
localization behavior
impact on workflow, permission, metric, or reporting
```

A list of codes without semantics is not a product definition.

## Permission model

For process-heavy or sensitive products, model product permission requirements as:

```text
actor or role
× operation
× data scope
× object relationship
× object state
× sensitivity
× delegation, separation-of-duty, or recusal constraints
```

Define both positive and negative rules:

```text
who may perform the action
who may see the object or individual fields
when access begins and ends
what happens after reassignment or role removal
whether an administrator may override
whether exports, files, or logs have stricter rules than the page
```

Button visibility is only one UI consequence. The product requirement must remain valid for direct URLs, APIs, exports, notifications, and background actions.

## Responsibility versus permission

Keep these separate:

```text
responsibility   who is accountable for the business outcome
permission       who is allowed to view or act in the product
assignment       who currently performs the work
approval         who has decision authority
```

RACI may clarify accountability; the permission matrix clarifies product access. One does not replace the other.

## Metric definition

A metric should answer a business question and define:

```text
name and stable ID when needed
business question and purpose
formula
population and exclusions
grain and deduplication key
dimensions and filters
time basis, timezone, and reporting window
units, currency, rounding, and conversion basis
status or lifecycle inclusion rules
visibility and data-permission behavior
refresh cadence
thresholds and drill-down behavior
owner, source, caveats, and acceptance check
```

Avoid metrics that change meaning between a card, export, and detail view.

## Product quality attributes

Product definition may state measurable constraints that affect user or business outcomes. Engineering owns the technical solution and proof.

Common attributes:

```text
performance and responsiveness
availability and recoverability
accessibility
security and privacy behavior
localization, language, timezone, currency, and regional format
capacity and scale assumptions
auditability and traceability
data retention, deletion, portability, and export
compatibility and device support
resilience to external-service failure
```

A useful requirement includes:

```text
context and user/business rationale
measurable target or threshold
conditions under which the target applies
priority and decision owner
verification method and evidence owner
known tradeoffs or dependencies
```

Avoid “fast”, “secure”, “user-friendly”, “high availability”, or “supports global use” without observable criteria.
