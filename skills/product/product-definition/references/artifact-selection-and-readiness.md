# Artifact Selection and Readiness

Product definition should create the smallest durable artifact set that resolves the actual product pressure. Templates are available capabilities, not a mandatory document tree.

## Admission questions

Before creating a separate artifact, ask:

```text
Does it answer a distinct product-authority question?
Does it have a different primary reader or decision owner?
Does it change at a different cadence from the surrounding specification?
Will several modules reuse it?
Would keeping it inline make the parent artifact hard to review or maintain?
Does risk, regulation, team count, or handoff complexity justify durable traceability?
```

If the answers are mostly no, keep the content inside the product brief or module PRD.

## Pressure-to-artifact map

| Pressure | Create or strengthen | Usually avoid |
| --- | --- | --- |
| One clear request, one team, low risk | Product Brief or compact PRD | Full artifact suite |
| Several source documents or code snapshots compete | Source Synthesis + Clarification Register | Copying all inputs into the PRD |
| Version scope repeatedly changes | Scope Baseline | Roadmap bullets without inclusion rules |
| Terms or object boundaries are unstable | Product Model | Page-first specification |
| Several roles hand work to each other | Workflow Specification | One happy-path diagram only |
| An object has meaningful lifecycle | State Machine | One overloaded status field |
| Rules repeat or conflict across modules | Business Rule Catalog | Duplicate rule text in several PRDs |
| Responsibility or visibility is disputed | RACI / Permission Matrix | Button-only permission descriptions |
| A stakeholder choice blocks the product | Decision Packet; PDR after acceptance | Passive “please confirm” lists |
| Cross-cutting quality targets matter | Quality Attribute Requirements | Unmeasurable “fast, secure, scalable” claims |
| Dashboard numbers are disputed | Metric Dictionary | Metric names without formulas and time basis |
| Design needs complete interaction states | Design Handoff | Treating a PRD as final visual design |
| Accepted behavior is changing | Change Impact Assessment | Editing one PRD in isolation |
| High risk or multi-team coordination | Requirements Traceability Matrix | Full traceability for every low-value detail |
| Business validation is required | Acceptance Criteria + UAT Scenarios | Field-by-field UAT only |

## Typical artifact sets

### Lightweight

```text
Product Brief
compact product model inside the brief
Module PRD
Acceptance Criteria
```

### Standard workflow product

```text
Source Synthesis when needed
Scope Baseline
Product Model
Workflow Specification and/or State Machine
Module PRDs
Decision Packets / PDRs
Acceptance Criteria and UAT
```

### High-change, high-risk, or multi-team product

```text
all relevant standard artifacts
Business Rule Catalog
RACI / Permission Matrix
Metric Dictionary
Quality Attribute Requirements
Requirements Traceability Matrix
Change Impact Assessments
Alignment Meeting Packs
```

## Product baseline readiness

A baseline is ready for a stated version when:

```text
outcomes and scope boundaries are explicit
sources and assumptions are visible
objects and terms are stable enough for shared use
workflows cover the material alternate and exception paths
states, rules, permissions, and metrics do not contradict each other
material decisions are accepted or isolated with owners and deadlines
requirements are observable and acceptance criteria are testable
adjacent teams can identify what they own next
```

Readiness is question-scoped. One module may be ready while another remains blocked. Do not withhold all progress because a separate capability is unresolved.

## Compression before separation

Prefer these moves in order:

```text
remove empty sections
use a table inside the existing artifact
add a clearly named section
split a reusable or independently governed artifact only when pressure persists
```

Do not pre-create symmetrical folders, empty templates, or one file per concept before the product earns that shape.
