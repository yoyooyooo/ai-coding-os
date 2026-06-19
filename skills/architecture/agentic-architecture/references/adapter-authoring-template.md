# Adapter Authoring Template

Use this template to add a language, framework, or deployment adapter without
polluting the generic doctrine.

## Scope

State:

```text
applies_to:
loads_after:
does_not_change:
```

An adapter may translate generic concepts into idioms. It must not redefine
fact authority, candidate/materialization semantics, evidence honesty, or the
forward-migration policy.

## Required Sections

### Idiom Mapping

Map:

```text
authority cell
capability port
adapter
composition root
command/query API
transaction/unit of work
typed change set and outcome
boundary/dependency enforcement
test and fixture support
```

### Language or Framework Hazards

List concrete ways the ecosystem can collapse boundaries: global state,
reflection/service locators, public mutable objects, generated SDK types,
implicit transactions, framework request objects, magic decorators, shared
singletons, or build-time dependency leakage.

### Recommended Shape

Give one small idiomatic example. Explain why the shape protects authority and
replaceability rather than presenting syntax as doctrine.

### Composition and Lifecycle

Identify the executable/bootstrap location, resource ownership, adapter
registration, configuration, credentials, cancellation, and shutdown model.

### Mechanical Proof

Name ecosystem-specific ways to enforce dependency direction, public API shape,
transaction behavior, adapter conformance, and restart/replay behavior.

## Quality Gate

A scenario adapter is useful only when it:

- removes ambiguity left by the generic skill;
- contains ecosystem-specific checks or patterns;
- remains optional through progressive disclosure;
- avoids time-sensitive framework trivia unless version context is explicit;
- does not duplicate the complete core doctrine;
- includes common failure modes, not just an ideal directory tree.

## Skill-Family Boundary

When the ecosystem deserves a standalone specialization rather than a scenario
reference, define its ownership and handoff contract. Keep universal authority,
transaction, migration, and evidence doctrine in `agentic-architecture`; let the
specialization own only domain- or technology-specific decisions. Add cross-skill
selection evals so the new skill does not become a duplicate trigger.
