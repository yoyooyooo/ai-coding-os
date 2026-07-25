# Product / Adjacent Boundaries

Product definition sets target behavior, product constraints, and the acceptance surface. It does not own every artifact needed to design, build, prove, release, or operate the system.

## Boundary table

| Question | Product definition owns | Adjacent owner owns |
| --- | --- | --- |
| What problem and outcome matter? | product brief, evidence synthesis, outcome and scope | business strategy and accountable outcome ownership |
| What should users and systems be able to do? | workflow, PRD, rules, acceptance | interaction design and implementation |
| What does an object or state mean? | product model and lifecycle SSoT | schema, enum, state-machine code |
| Who is responsible and who may act or see data? | responsibility and product permission requirement | identity, authorization, and policy implementation |
| What data must exist and why? | product fields, semantics, validation, sensitivity, retention need | schema, API, storage, migration, encryption mechanism |
| What metric should mean? | formula, grain, time, filters, visibility | data pipeline, query, dashboard implementation |
| What quality constraint is required? | measurable target, context, priority, verification expectation | technical design, capacity plan, monitoring, proof |
| What should the interaction cover? | scenarios, flow, states, constraints, content requirements | information architecture, interaction details, visual design |
| Why was a product behavior chosen? | Product Decision Record | ADR for technical mechanism |
| Is it implemented and safe to release? | expected acceptance surface | code, tests, security evidence, UAT evidence, release decision |

## Design handoff

Provide design with:

```text
users, goals, and scenarios
workflow and state inventory
business objects and key data
permissions and content visibility
validation, errors, empty states, partial success, and recovery
accessibility, localization, and quality constraints
critical acceptance criteria
open decisions and prohibited assumptions
```

Do not prescribe visual layout unless it is a binding product constraint.

When `$interface-capability-planning` is installed, hand off accepted Product Requirement, Rule, and AC IDs with these obligations. InterfaceCapability maps them into IA, surfaces, regions, interaction-state ownership, and proof needs. It does not redefine product rules; Product Design Handoff does not own concrete frontend state, cache, router, render, component, or test-lane choices.

## Architecture and engineering handoff

Provide:

```text
accepted product behavior and version scope
product objects, relationships, lifecycle, invariants, and rule precedence
permission and sensitivity requirements
files, notifications, logs, metrics, and quality targets
open decisions and safe temporary assumptions
critical edge cases and acceptance criteria
migration or deprecation expectations
areas where feasibility may require a new product decision
```

## Security, privacy, legal, and compliance handoff

Product definition identifies sensitive data, user expectations, policy-dependent decisions, retention needs, access boundaries, and high-risk workflows. Domain authorities decide binding controls and interpretations; technical owners implement and prove them.

## QA and business acceptance handoff

Provide:

```text
requirements and acceptance criteria
state and rule coverage priorities
permission combinations
end-to-end UAT scenarios
seed-data needs
expected files, notifications, metrics, and logs
known assumptions and excluded future scope
```

## Implementation drift labels

```text
product target not implemented
implementation exceeds accepted scope
implementation contradicts product target
legacy behavior retained temporarily
technical constraint requires product decision
product specification lacks detail for implementation
current behavior is unverified
acceptance exists but delivery evidence is missing
```

Never use an accepted PRD as proof that implementation or release is complete.
