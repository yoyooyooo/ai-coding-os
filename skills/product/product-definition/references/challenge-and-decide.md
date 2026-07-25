# Challenge and Decide

A product definition run is not complete until it has attacked the specification and prepared the decisions needed to make it coherent.

## Challenge lenses

```text
Conflict          two sources, rules, flows, or metrics cannot both be true
Gap               implementation or acceptance cannot proceed because product behavior is missing
Ambiguity         a term, actor, object, state, rule, or metric can mean several things
Assumption        the team relies on something no responsible owner has accepted
Drift             current behavior differs from the accepted target
Shadow scope      future, legacy, prototype, or code-only capability sneaks into current scope
Edge case         alternate, exception, recovery, termination, or migration path is uncovered
Risk              safety, privacy, legal, financial, operational, accessibility, or reputational exposure
Dependency        an external decision, system, team, data source, or policy is required
Metric conflict   the same measure has different formula, population, time, or visibility rules
Permission gap    access or responsibility is inconsistent across role, state, relationship, or channel
```

## Attack checklist

Challenge across these surfaces:

```text
scope and version boundary
actor responsibility and separation of duty
object identity and relationship
workflow handoff and waiting
state transition and reversibility
validation, calculation, and precedence
permissions, field visibility, exports, files, and notifications
concurrent action, duplicate submission, stale data, and retry
external-service failure and manual fallback
timezone, calendar, localization, currency, and rounding
migration, historical data, deletion, retention, and reopening
metrics, filters, drill-down, and data-scope consistency
quality attributes and acceptance observability
```

## Issue record

Keep an issue inline when it can be resolved locally and reversibly. Create a
durable issue record only when decision, traceability, risk, or cross-owner
handoff pressure earns it. A durable material issue should include:

```text
issue ID and type
neutral problem statement
source claims or current evidence
affected version and scope
impact on users, objects, workflow, state, rules, permissions, metrics, data, design, delivery, and risk
recommended treatment
alternatives and tradeoffs
responsible decision owner
needed-by date
status and follow-up artifacts
```

## Decision packet

Use this before asking stakeholders to decide:

```text
Decision ID
Topic
Decision statement
Background
Source claims and evidence
Conflict, gap, ambiguity, assumption, or risk
Why it matters now
Recommended option
Rationale and decision principles
Alternative options and tradeoffs
Impact matrix
Decision owner and required participants
Needed-by date
Final decision
Effective version
Follow-up artifact updates
Residual risks
```

The recommendation is part of the product lead's job. Do not reduce the packet to “please confirm”.

## Recommendation quality

A recommendation should:

```text
resolve the actual product question
fit the stated outcome and version boundary
preserve coherent object and lifecycle semantics
consider user cost, operational cost, delivery cost, and future lock-in
state risks and reversibility
avoid treating current code as mandatory scope
identify a safe default when delay is unavoidable
```

## Decision ownership

The product lead may recommend but should not manufacture authority. Match the decision to the owner:

```text
business outcome or responsibility      business owner
scope, workflow, or product behavior    product and business owner
policy or legal interpretation          policy/legal authority
privacy or security boundary            privacy/security authority
financial or metric definition          accountable business/data owner
technical mechanism                     architecture/engineering owner through ADR or technical design
release readiness                        delivery and business acceptance owners
```

## Isolate blockers

When a decision is missing:

1. Mark only the affected claims or paths as blocked or assumed.
2. State the temporary working behavior, if one is safe.
3. Name its expiry or decision point.
4. Continue unaffected modeling and specification.
5. Do not present the assumption as accepted.

## When to create a Product Decision Record

Create a durable record when the accepted decision changes one or more of:

```text
scope or version promise
object meaning or identity
workflow or handoff
state or lifecycle
role responsibility or permission boundary
business rule or metric definition
quality target
acceptance criteria
migration or deprecation behavior
roadmap commitment
```

Do not create durable records for editorial changes, local UI wording, temporary notes, or issues that remain undecided.

## Close the loop

A decision is not closed merely because it appears in meeting notes. Update the authoritative product artifacts and record:

```text
what changed
which version it affects
which assumptions are removed
which artifacts, requirements, acceptance criteria, and UAT scenarios must change
which current behavior now represents drift
which delivery teams need the decision
```
