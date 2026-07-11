---
name: evolvable-application-architecture
description: >-
  Designs and audits evolvable application architecture for systems with durable
  business facts, transactions, external capabilities, distributed workflows,
  plugins, agents or LLMs, realtime projections, or forward migrations. Use for
  authority and fact ownership, modular monoliths, hexagonal ports and adapters,
  use-case boundaries, idempotency, outbox and replay, composition roots,
  data/API migration, architecture evidence, or deciding how much architecture
  a small application actually needs. Lead cross-stack reviews spanning backend,
  frontend, and Effect while delegating technology-specific detail to specialist
  skills when available.
metadata:
  version: "1.0.0"
---

# Evolvable Application Architecture

Use an **authority-first hexagon**: accepted product facts live behind explicit
use cases; external powers cross capability ports; composition chooses concrete
implementations; evidence bounds every claim. Scale the architecture to the
real pressure instead of applying the maximum pattern set by default.

## Ownership Contract

```text
Owns: fact authority, consistency domains, dependency direction, module
boundaries, use-case and transaction shape, capability ports, candidate
materialization, composition profiles, forward migration, replaceability, and
evidence ceilings.

Delegates: detailed frontend topology/state/realtime -> frontend-architecture;
Effect Service/Layer/Scope/API/runtime judgment -> effect-best-practices;
managed Effect HttpApi generation -> effect-api-app-kit after architecture
choices are settled.

Does not own: project product truth, framework syntax, vendor selection, UI
visual design, or unapproved security, privacy, retention, destructive-data, or
public-contract decisions.
```

Read [Skill Family Coordination](references/skill-family-coordination.md) when
more than one architecture skill applies.

## Workflow

1. **Select mode and pressure.** Choose quick assessment, focused review, full
   audit, target design, or migration plan; assign the relevant vertical slice a
   pressure profile from P0-P4. Complete when scope, non-goals, and claim ceiling
   are explicit.
2. **Read project authority.** Read instructions, SSoT, ADRs, schemas, public
   contracts, tests, and deployment entry points. Complete when project facts
   are separated from generic defaults.
3. **Trace reality.** Trace one real command from intent to committed fact and
   projection. When external, inferred, imported, or nondeterministic input
   exists, also trace one observation/candidate to its decision. Complete when
   every writer, transaction, external call, and post-commit carrier is named.
4. **Map six lenses.** Record authority, dependency direction,
   time/consistency, topology, lifecycle, and evidence. Complete when each
   important fact has one final materialization authority within a declared
   consistency domain and authority epoch.
5. **Classify boundaries.** Separate authority cells, internal typed
   collaboration, input adapters, output capability ports, and projections.
   Complete when no adapter or composition root can silently create product
   truth.
6. **Design the smallest sufficient seam.** Apply only the patterns required by
   the selected pressure profile. Complete when the design states what is
   deliberately *not* introduced.
7. **Migrate vertically and prove.** Route one slice through the new seam, attach
   deletion gates to every bridge, and match evidence to the claim. Complete
   when observed facts, inference, proposal, verification, `not_proven`, and
   `not_claimed` are distinct.

Make safe, doctrine-determined choices directly. Reserve human decisions for
fact ownership, permissions, privacy/retention, destructive migration, public
compatibility, or product semantics that the repository does not settle.

## Core Invariants

```text
canonical accepted fact
  -> one final materialization authority
     within a declared consistency domain and authority epoch

authoritative intent -> Command -> authorize/validate -> transition -> commit
non-authoritative output -> Candidate -> govern/decide -> materialize -> commit

business authority cell != adapter
internal typed collaboration != generic capability port
external call outside database transaction
accepted fact + canonical event/audit/outbox inside one transaction
composition root selects implementations; it does not own product transitions
internal APIs may break; durable accepted facts receive deliberate migration
realtime follows commit and supports dedupe, gap recovery, and backfill
replaceability requires conformance evidence, not merely an interface
```

Multiple proposers, replicas, reviewers, or candidate sources are compatible
with one final materialization authority. For federation, CRDTs, leader epochs,
and sagas, read
[Consistency and Authority Topologies](references/consistency-and-authority-topologies.md).

## Progressive Disclosure

| Need | Read |
|---|---|
| Baseline and abstraction restraint | [Core Doctrine](references/core-doctrine.md) |
| How much architecture this slice needs | [Pressure Profiles](references/pressure-profiles.md) |
| Fact ownership and private modules | [Authority Model](references/authority-model.md) |
| Federation, CRDT, saga, or multi-writer claims | [Consistency and Authority Topologies](references/consistency-and-authority-topologies.md) |
| Commands, observations, candidates, and outcomes | [Use-Case Kernel](references/use-case-kernel.md) |
| External providers, gateways, devices, or plugins | [Capability Ports](references/capability-ports.md) |
| God objects, global state, and modular monoliths | [Evolutionary Modularity](references/evolutionary-modularity.md) |
| Transactions, repositories, events, and outbox | [Persistence and Events](references/persistence-and-events.md) |
| Profiles, registries, assembly, and lifecycle | [Composition Roots](references/composition-roots.md) |
| Breaking changes and bridge deletion | [Forward Evolution](references/forward-evolution.md) |
| Claim ceilings, conformance, replay, and load proof | [Evidence Harness](references/evidence-harness.md) |
| Existing repository review | [Audit Playbook](references/audit-playbook.md) |
| Agents, LLMs, tools, memory, and A2A | [Agentic Systems Profile](references/scenario-agentic-systems.md) |
| Payments, approvals, IoT, data, collaboration | [Scenario Mappings](references/scenario-mappings.md) |
| Rust | [Rust Adapter](references/adapter-rust.md) |
| Server-side TypeScript | [TypeScript Backend Adapter](references/adapter-typescript-backend.md) |
| Frontend baseline / handoff | [Frontend Adapter](references/adapter-frontend.md) |
| Another ecosystem | [Adapter Authoring Template](references/adapter-authoring-template.md) |

## Output Contract

Always state:

```text
mode; pressure_profile; sources_read; vertical_slice; observed_vs_inferred;
critical_authorities; current_pressure; proposed_seam; evidence_ceiling;
not_proven; not_claimed.
```

Then scale the rest to the mode:

| Mode | Additional output |
|---|---|
| quick-assessment | main risk; minimum correction; deliberately_not_needed |
| focused-boundary-review | traced boundary; findings; target contract; proof |
| full-audit | six-lens map; severity findings; target boundaries; migration waves; deletion gates |
| target-design | authority cells; commands/candidates; transactions; ports; composition; topology |
| migration-plan | compatibility classes; vertical waves; bridge ledger; cutover and rollback limits |

Prefer an executable sequence and explicit non-goals over a perfect end-state
diagram.
