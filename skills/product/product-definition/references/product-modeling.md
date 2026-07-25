# Product Modeling

Model before screens. A product specification that starts from pages often hides broken object boundaries, inconsistent terminology, impossible states, and missing responsibilities.

## Minimum model

```text
Actors         who participates and what responsibility or goal they carry
Objects        things with stable identity and lifecycle
Relationships  how objects create, contain, reference, derive from, or close each other
Workflow       movement across actors and systems from trigger to outcome
State          lifecycle of an object, separated from approval, task, time, display, and archive state
Rules          validations, invariants, calculations, eligibility, precedence, and side effects
Permissions    who can see or act under which scope, relationship, state, and sensitivity
Artifacts      files, reports, exports, messages, notifications, logs, and generated records
Metrics        measures, formulas, grain, dimensions, time basis, and visibility
Quality        measurable product constraints such as accessibility, latency, availability, privacy, and localization
```

## Stable product language

Create a glossary when a term:

```text
has several business meanings
is used differently across teams or sources
maps to an object, status, rule, or metric
has a historical synonym that may still appear in code or data
is translated or localized
```

A definition should say what the term includes, excludes, and how it differs from nearby terms.

## Actor card

| Field | Prompt |
| --- | --- |
| Actor | Is this a person, role, team, external party, or system? |
| Goal | What outcome does the actor seek? |
| Responsibility | What is the actor accountable for? |
| Authority | What may the actor decide or approve? |
| Data visibility | What may the actor see and under what scope? |
| Delegation | May responsibility be delegated, transferred, or reassigned? |
| Conflict constraints | Are separation-of-duty or recusal rules needed? |
| Entry/exit | How does the actor join or leave the workflow? |

Do not confuse a business role with a job title, application role, permission bundle, or individual user.

## Object card

| Field | Prompt |
| --- | --- |
| Name | What is the stable business name? |
| Definition | What makes it this object and not another? |
| Identity | What is its unique identity and when is it assigned? |
| Created by / when | Which trigger creates it? |
| Owner | Who is accountable for its progress and correctness? |
| Relationships | Parent, children, references, derivations, generated artifacts |
| Lifecycle | States, transitions, terminal and reversible conditions |
| Invariants | What must always remain true? |
| Sensitive data | Personal, financial, legal, confidential, public, or none |
| Retention | How long, why, and what may be deleted or anonymized? |
| Closed by / when | Which event ends or archives it? |
| Open questions | Decisions needed before baseline |

## Relationship discipline

Name relationship semantics, not only cardinality:

```text
creates
generates
contains
belongs to
references
supersedes
is derived from
is a version of
closes
blocks
is assigned to
```

Ask whether deleting, replacing, closing, or changing one object should affect related objects.

## State discipline

Separate:

```text
business object state
approval state
task or assignment state
time/SLA state
visibility or publication state
archive or retention state
UI display state
integration or synchronization state
```

One overloaded `status` becomes a product and implementation trap. When states are derived, document the derivation instead of storing a second competing lifecycle.

A state model should define:

```text
meaning
entry condition
allowed actions
exit condition
terminality
reversibility
side effects
invalid transitions
```

## Product invariants

Invariants are rules that must always hold, independent of screen or workflow step. Examples:

```text
an object cannot approve itself when separation of duty applies
an accepted version cannot be silently overwritten
closed objects cannot return to an active state without an explicit reopen action
one active assignment may exist per responsibility at a time
currency totals must retain original amount and conversion basis
```

Express invariants in product language, then hand them to engineering and test.

## Files, artifacts, and generated records

For each artifact define:

```text
business meaning
source object
creator or generator
version behavior
visibility and download rules
retention and deletion rules
whether replacement creates a new version
whether an audit/log record is required
```

Do not collapse attachments, evidence, reports, exports, and archives into one product concept merely because they share storage technology.

## Cross-module model

When several modules share objects or rules, decide whether the shared concept has one product owner and one definition. Avoid copying object fields and lifecycle into each module PRD.

Use a shared product model or rule catalog when reuse outweighs the cost of a separate artifact.
