---
name: agentic-architecture
description: >-
  Designs and audits evolvable software architecture for systems whose product
  semantics, runtimes, providers, agents, plugins, storage, or deployment shape
  may change. Use for authority ownership, hexagonal capability ports, modular
  monoliths, application facades, transaction and event boundaries, composition
  roots, replaceability, forward-only migrations, or architecture evidence.
  Also use as the lead skill for cross-stack reviews spanning backend,
  frontend, and Effect; defer isolated frontend topology to frontend-architecture,
  Effect API/runtime judgment to effect-best-practices, and executable Effect
  HttpApi scaffolding or verification to effect-api-app-kit.
---

# Agentic Architecture

Preserve the ability to change product semantics without turning every earlier
implementation into a permanent compatibility burden. Apply the language-neutral
doctrine first; load a language or surface adapter only after identifying the
actual pressure.

## Ownership Contract

```text
Owns: fact authority, dependency direction, module boundaries, capability ports,
use-case/transaction shape, candidate materialization, composition profiles,
forward migration, replaceability, and evidence ceilings.
Delegates: frontend topology/state/realtime details -> frontend-architecture;
Effect Service/Layer/Scope/API details -> effect-best-practices; managed Effect
HttpApi project generation -> effect-api-app-kit after architecture decisions.
Does not own: project product truth, framework syntax, vendor selection, UI
visual design, or unapproved security/data-retention decisions.
```

Read [Skill Family Coordination](references/skill-family-coordination.md) when
more than one architecture skill applies.

## Workflow

1. Read project instructions, SSoT, ADRs, schemas, tests, deployment entry points,
   and current vertical slices. Project authority overrides generic defaults.
2. Classify the pressure: authority, dependency, state, transaction, external
   capability, composition, migration, lifecycle, or evidence.
3. Trace one real slice from intent through accepted fact and projection. Do not
   infer architecture from folders or interfaces alone.
4. Map six lenses: authority, direction, time/consistency, topology, lifecycle,
   and evidence.
5. Separate business authority cells from replaceable capability adapters. Add
   abstraction only for real replacement, risk, ownership, deployment, or proof
   pressure.
6. Design the smallest seam, migrate vertically, and give every temporary bridge
   an owner, expiry/review date, and deletion proof.
7. Separate observed facts, inference, proposed design, verification, and
   `not_claimed`.

## Core Invariants

```text
one durable fact -> one authority
external output -> candidate -> decision -> materialization -> commit -> projection
business module != adapter; command != query/projection
external call outside transaction; accepted fact + event/outbox inside transaction
composition root selects implementations; core does not enumerate vendors
internal APIs may break; durable facts receive deliberate forward migration
realtime follows commit and supports dedupe, gap recovery, and backfill
replaceability requires conformance evidence, not merely an interface
```

## Progressive Disclosure

| Need | Read |
|---|---|
| Baseline and abstraction restraint | [Core Doctrine](references/core-doctrine.md) |
| Fact ownership and private modules | [Authority Model](references/authority-model.md) |
| God objects and global state | [Evolutionary Modularity](references/evolutionary-modularity.md) |
| Providers, runtimes, memory, plugins | [Capability Ports](references/capability-ports.md) |
| Commands, candidates, context, outcomes | [Use-Case Kernel](references/use-case-kernel.md) |
| Transactions, repositories, events/outbox | [Persistence and Events](references/persistence-and-events.md) |
| Profiles, registries, assembly | [Composition Roots](references/composition-roots.md) |
| Breaking changes and bridge deletion | [Forward Evolution](references/forward-evolution.md) |
| Claim ceilings, conformance, replay | [Evidence Harness](references/evidence-harness.md) |
| Existing repository review | [Audit Playbook](references/audit-playbook.md) |
| Rust | [Rust Adapter](references/adapter-rust.md) |
| Server-side TypeScript | [TypeScript Backend Adapter](references/adapter-typescript-backend.md) |
| Frontend baseline / handoff | [Frontend Adapter](references/adapter-frontend.md) |
| Another ecosystem | [Adapter Authoring Template](references/adapter-authoring-template.md) |

## Required Output

```text
mode; authorities_read; vertical_slice; six_lens_map; current_pressure;
findings_by_severity; target_boundaries; authority_cells; capability_ports;
command_query_materialization; transaction_and_event_boundaries;
composition_profiles; migration_waves; bridge_deletion_gates; evidence_plan;
human_decisions; auto_fix_candidates; not_claimed.
```

Prefer an executable migration sequence over a perfect end-state diagram.
