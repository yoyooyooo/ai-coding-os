# Schema And Terminology Migration

Use this reference when a goal changes core method vocabulary, schema fields, or
public command language.

Treat active surfaces as part of the migration. Scan and update the surfaces an
agent may actually read or expose:

```text
SKILL.md
references/**
templates/**
agents/**
evals/**
README / package README
CLI help and flags
tests and fixtures
active Goal Pack goal contract/state/evidence records
```

If the completion review claims no old term or field remains, the check must prove a
negative. Use an inverted no-match command or an explicit allowlist. A plain
search that returns matches is not evidence that the surface is clean.

If a field rename affects public surfaces, decide one outcome and make it
visible in evidence records:

- rename the surface;
- keep a documented compatibility alias;
- leave it out of the claim and evidence add the remaining gap.

## Goal Pack Home Migration

The writer default is `.goal-proof/goals/<goal-id>/`. CLI 0.2.x retains a
finite reader compatibility lookup for `docs/goal-proof/goals/<goal-id>/` so an
existing pack can be inspected without a destructive move. New project adapters,
CLI help, references, templates, and tests use the hidden-root path.

A migration must state whether it:

- retains legacy packs in place for read-only compatibility;
- moves a project-declared home under its own retention policy;
- updates the project execution-method declaration; or
- ends the compatibility window in a later CLI major/minor decision.

Historical `evidence.jsonl` records are append-only regardless of home.

Common checks:

```bash
! rg -n "old_term|legacy_field" <active-surface>
rg -n "intentional_alias|docs/goal-proof/goals" <documented-compatibility-surface>
```
