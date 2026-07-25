---
name: product-definition
description: >-
  Product definition from ambiguous or competing inputs. Use when synthesizing
  product sources into a versioned Baseline, modeling actors, objects,
  workflows, rules, permissions, and metrics, preparing product decisions or
  PRDs, or defining acceptance, UAT, traceability, alignment, and change impact.
---

# Product Definition

Use four leading words throughout the run:

```text
Baseline   the accepted product target for a version, not raw input and not delivery proof
Model      the actors, objects, workflows, states, rules, permissions, artifacts, and metrics that make the product coherent
Challenge  the conflicts, gaps, ambiguity, assumptions, edge cases, and risks exposed before the specification hardens
Trace      the visible path from source and decision to requirement, acceptance, and delivery handoff
```

Source is not Decision. Decision is not Specification. Specification is not Delivery.

## Operating Contract

```text
Owns:
  product framing and outcome definition
  source registration, synthesis, and product-claim classification
  scope baselines and version slicing
  actors, responsibilities, business objects, relationships, workflows, states, and rules
  product permission requirements, data visibility, artifacts, files, metrics, and quality attributes
  conflict/gap/ambiguity/risk analysis and product decision preparation
  modular PRDs, acceptance criteria, UAT scope, product traceability, and product change impact
  stakeholder alignment packs and product handoff constraints

Hands off:
  binding business/legal/policy/compliance/privacy/security choices -> accountable domain owners
  interaction and visual solution -> design owners
  implementation, release, and runtime state -> their delivery owners

Adjacent Suite owners, when installed:
  documentation authority, artifact home, lifecycle, and cleanup -> `$docs-governance`
  accepted product obligations -> interface capability mapping -> `$interface-capability-planning`
  technical facts, modules, transactions, and boundaries -> `$evolvable-application-architecture`
  proof architecture and claim ceilings -> `$product-harness-system`
```

### Default judgment and blocking policy

Infer ordinary reversible details from the current Product Baseline, SSoT,
accepted rules, and nearby project patterns. Use a low-commitment assumption
when it does not widen scope, permissions, public contracts, durable data, or a
trust boundary; keep the assumption visible and continue.

Create a Decision Packet only when materially different answers would change
product scope, shared meaning, workflow/state semantics, permissions, rules,
metrics, acceptance, or a version promise and current Authority cannot decide.
Keep the run moving by isolating that unresolved claim, workflow, rule, or
version slice; label it blocked or assumed, state the recommendation and owner,
and continue unaffected work.

Stop the whole run only when:

```text
source access is too incomplete to produce an honest product model
continuing would expose sensitive data outside the approved workspace
the user requires an unsupported claim to be presented as accepted or delivered
the product question cannot be separated from a binding decision and no responsible owner can be identified
```

Outputs are destination-neutral. Place them in the repository's established document homes and follow its routers, identifiers, and naming rules; a template name does not create a parallel document tree.

## Product-Claim Labels

Every material claim should carry one of these meanings, explicitly or by clear context:

```text
accepted                  approved product target for the stated version
recommended               product lead recommendation awaiting decision
assumed                    temporary working assumption with owner and expiry/decision point
source-derived             restatement of an input, not yet promoted into product truth
observed-behavior-derived  behavior verified by bounded execution or observation, not automatically future scope
future-candidate           possible later capability, outside the current baseline
rejected-or-superseded     explicitly not part of the current target
unknown                    insufficient evidence; leave the claim unresolved
```

Resolve precedence by question, scope, and accountable authority rather than document age, implementation existence, stakeholder seniority, or repetition count.

## Product Definition Coverage

Select the applicable decisions in the order suggested by current evidence.
Baseline, Model, accepted decisions, and requested handoffs constrain one
another, but this coverage is not a project workflow.

### Frame

Identify the product question, version horizon, users, business outcomes, constraints, source set, decision owners, and the expected level of specification.

Ask:

```text
What problem and outcome are being defined?
For which version or time horizon?
Which users, business units, or markets are in scope?
Which inputs are evidence, wishes, current behavior, accepted decisions, or future candidates?
What must be decided before delivery can proceed?
What artifact set is proportionate to the product pressure?
```

Use [Artifact Selection and Readiness](references/artifact-selection-and-readiness.md).

**Completion criterion:** the product problem, version boundary, candidate scope, source set, decision owners, constraints, and unsupported assumptions are visible.

### Synthesize

Register sources, extract claims, classify their kind and confidence, group conflicts, and distinguish current fact from target intent.

Use [Source to Product Truth](references/source-to-product-truth.md) and the [Source Synthesis template](templates/source-synthesis.md).

**Completion criterion:** material claims have provenance; conflicting or unsupported claims are not silently merged; source inputs remain distinguishable from accepted product truth.

### Model

Model before screens:

```text
actors and responsibilities
business objects and relationships
end-to-end workflows and handoffs
business, approval, task, time, visibility, and archive states
business rules, validations, calculations, and invariants
permissions and data visibility
files, generated artifacts, notifications, logs, and retention needs
metrics, dimensions, time basis, and visibility rules
product quality attributes that must be measurable
```

Use [Product Modeling](references/product-modeling.md), [Workflow and Exception Modeling](references/workflow-and-exception-modeling.md), and [Rules, Permissions, Metrics, and Quality](references/rules-permissions-metrics-quality.md).

**Completion criterion:** the core product language, objects, lifecycle, role responsibilities, rule families, and metric definitions are explicit enough to expose contradictions and drive design and engineering handoff.

### Challenge

Attack the model before hardening it. Test the happy path, alternatives, exceptions, recovery, concurrent actions, delegation, expiry, cancellation, migration, privacy, and operational failure.

Use [Challenge and Decide](references/challenge-and-decide.md).

**Completion criterion:** every material conflict, gap, ambiguity, assumption, drift, edge case, and risk has an impact, recommendation, owner, and decision path or an explicit deferment.

### Decide

Prepare decision packets with a recommendation, alternatives, tradeoffs, impact, owner, and deadline. Promote durable accepted choices into Product Decision Records when they change scope, object meaning, workflow, state, role responsibility, permission boundary, rule, metric definition, acceptance, or roadmap promise.

Use the [Decision Packet template](templates/decision-packet.md) before the [Product Decision Record template](templates/product-decision-record.md).

**Completion criterion:** accepted decisions are distinguishable from recommendations, assumptions, unresolved questions, future candidates, current implementation, and superseded choices.

### Specify

Produce the smallest specification set that can drive alignment and delivery:

```text
product brief and/or scope baseline
product model and glossary
workflow, state machine, or rule catalog where complexity requires them
module PRD
permission matrix, metric dictionary, or quality requirements when cross-cutting
acceptance criteria and UAT scenarios
traceability links where risk, regulation, team count, or change pressure justifies them
```

Use [PRD and Acceptance](references/prd-and-acceptance.md), [Scope and Version Baselines](references/scope-and-version-baselines.md), and [Traceability and Change Impact](references/traceability-and-change-impact.md).

**Completion criterion:** the product target is coherent, observable, testable, versioned, traceable at the necessary depth, and honest about unresolved or not-yet-delivered behavior.

### Align and Handoff

Turn unresolved issues into a meeting-ready decision view, close decisions into the authoritative product artifacts, assess change impact, and hand accepted behavior to design, architecture, engineering, security, data, and QA without taking over their design authority.

Use [Alignment and Facilitation](references/alignment-and-facilitation.md) and [Product / Adjacent Boundaries](references/product-technical-boundary.md).

A Product Design Handoff carries accepted Requirement, Rule, and AC IDs plus user goals, product behavior, business objects, state obligations, permissions, exceptions, and acceptance expectations. `$interface-capability-planning` may map those obligations into IA, surfaces, regions, interaction-state ownership, and proof needs; it does not redefine the product rules. Layout, components, and frontend technology ownership do not flow back as product meaning unless product decision authority explicitly accepts a change.

**Completion criterion:** the decision meeting does not become a shadow source of truth; accepted changes have named follow-up artifacts; adjacent teams receive accepted behavior, open decisions, constraints, critical edge cases, and acceptance expectations.

## Output Contract

Return only the artifacts material to the request, selected from:

```text
framing summary
source register and synthesis
scope baseline and version split
product model, glossary, object catalog, workflow, or state model
conflict, gap, ambiguity, assumption, drift, edge-case, and risk analysis
decision packets or Product Decision Records
business rules, permissions, metrics, and quality requirements
module PRD and design handoff
acceptance criteria and UAT scenarios
requirements traceability and change-impact assessment
alignment meeting pack
handoff notes to design, architecture, engineering, security, data, QA, or documentation governance
```

Leave stakeholder approval, implementation status, test evidence, release evidence, and policy authority unproven until their owners supply them.
