# Source to Product Truth

Product work starts by refusing to treat every input as the same kind of truth.

## Source kinds

```text
formal policy or regulation        binding only inside its actual scope, jurisdiction, and effective version
draft policy                       strong source input, not final authority
strategy or vision                 intent, outcome, and roadmap pressure; usually not detailed scope
business requirements              source input until accepted into a version baseline
meeting notes, chat, or email       source input; capture owner, date, and whether a decision was actually made
research, analytics, or support     problem and prioritization evidence; not a complete solution definition
screenshots or prototype            interaction or current-state evidence; not necessarily product truth
legacy code or AI coding output     current-implementation and migration evidence; not an automatic requirement
production behavior                 current fact when verified; may still be a defect or temporary compromise
technical design                    implementation intent; does not redefine product behavior without a product decision
test or release evidence            delivery proof; not the source of why the product should behave that way
```

## Register source metadata

For material sources capture:

```text
source ID
name and location
kind
owner or issuing authority
version and date
effective scope
current validity
confidence in extraction or interpretation
sensitivity and access constraint
known limitations or superseding sources
```

Authority and confidence are different:

```text
A formally issued source may be authoritative but ambiguously written.
A verified production observation may be highly confident but not authoritative for future scope.
A senior stakeholder opinion may matter but remain an undecided preference.
```

## Decompose sources into claims

Do not treat a whole document as one indivisible requirement. Extract atomic claims such as:

```text
scope claim
actor or responsibility claim
object-definition claim
workflow or state claim
business-rule claim
permission claim
metric claim
quality or constraint claim
roadmap or future claim
implementation claim (source path, module, route, schema, migration, table)
observed-behavior claim (bounded execution or observation)
```

Each claim should preserve provenance and avoid paraphrasing away uncertainty.
Source presence supports an `implementation` claim; it does not become an
`observed-behavior` claim until a bounded path is executed or observed.

## Source synthesis table

Use this shape when several materials compete:

| Claim ID | Source ID | Claim | Kind | Horizon | Confidence | Product impact | Conflict group | Decision needed | Recommended treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Recommended treatment values may include:

```text
promote after confirmation
retain as current fact only
use as problem evidence
convert into a decision packet
place outside current scope
mark as future candidate
supersede with a newer accepted decision
verify against production or data
retire as obsolete
```

## Promotion path

```text
source claim
→ synthesized product issue or evidence
→ recommendation and alternatives
→ responsible-owner decision
→ Product Decision Record when durable
→ scope baseline / product model / PRD / rule / metric / acceptance
→ implementation and delivery evidence outside product truth
```

Do not promote a claim merely because it is old, detailed, senior-sounding, already implemented, or repeated in several places.

## Conflicting sources

When two claims cannot both be true:

1. State the conflict in neutral language.
2. Identify the actual question that must be decided.
3. Show affected versions, users, objects, workflow, rules, permissions, metrics, and delivery work.
4. Recommend one option and explain why.
5. Name the decision owner and deadline.
6. Preserve both source claims until the decision is closed.

Do not silently average, merge, or choose the newest source without checking scope and authority.

## Implementation and observed behavior as sources

Source, schema, and migration evidence answer what implementation structure,
static logic, and durable shapes exist. Executed tests, Harnesses, runtime, and
operational Evidence answer what happened on a bounded path and what users may
currently experience. Neither decides whether the product should retain that
implementation or behavior.

Classify an implementation-only capability as one of:

```text
accepted target with implementation evidence but unverified behavior
unaccepted implementation
legacy implementation retained temporarily
technical shortcut to replace
future candidate already prototyped
obsolete implementation to retire
unknown until product decision or observation
```

When target, implementation, and observed behavior differ, record separate
claims rather than treating one as a transcription error.

## Staleness and supersession

Use content and effective scope, not file modification date alone. A recently copied old document may still be obsolete; a long-lived specification may remain authoritative.

Mark:

```text
supersedes       this source or decision replaces an earlier one
superseded-by    the newer authority
still-valid-for  a narrower version, market, role, or workflow
historical-only  useful evidence, not current product target
```

## Sensitive sources

Minimize copied personal, financial, legal, health, security, or confidential data. Use identifiers, summaries, redaction, or approved secure references. Product definition rarely needs raw sensitive case data to define the product behavior.
