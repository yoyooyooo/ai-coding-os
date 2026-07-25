# Architecture Extension Contract

An architecture Skill contributes owner-scoped node kinds, rules, projections,
and proof expectations.

Each extension should state:

```text
semantic concepts it owns
questions that trigger it
owner-qualified node kinds
rule contract fields and escalation boundaries
mapping to source/runtime constructs
hazards where ecosystem concepts resemble but do not equal core semantics
proof surfaces and claim ceilings
```

It must not:

```text
redefine product meaning
rename another owner's concept without qualification
turn a language primitive into business Authority
require central ADIR persistence
make its ecosystem projection the generic core
```

Typical composition:

```text
EAA      fact authority / use case / port / migration
Frontend state owner / projection / reconciliation
Effect   Service / Layer / Runtime / Scope
Rust     module / crate / trait / task lifecycle projection of settled EAA semantics
```
