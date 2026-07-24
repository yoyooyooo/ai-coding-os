---
name: evolvable-application-architecture
description: >-
  Authority-first application architecture for durable facts, transactions,
  external capabilities, modular monoliths, migrations, repository topology,
  and semantic source naming. Use when deciding or auditing fact ownership,
  use-case and port boundaries, consistency, composition roots,
  module/package/deployable promotion, MVP takeover, or replaceability. Use
  $frontend-architecture and $effect-best-practices for their implementation
  surfaces.
---

# Evolvable Application Architecture

Use an **authority-first hexagon**: accepted facts live behind explicit use
cases; external powers cross application-owned capability ports; composition
chooses implementations; evidence bounds claims.

Default references:

```text
Monorepo-first, doctrine-neutral
Bounded Semantic Flatness
folders own; filenames explain; packages enforce; apps run
```

Project authority may resolve different structures while preserving the same
semantic boundaries.

## Ownership

```text
Owns:
  fact authority and consistency domains
  private capability modules and dependency direction
  use-case, transaction, idempotency, event, and outbox shape
  capability ports, observations/candidates, receipts, and materialization
  composition roots and resource-host boundaries
  repository/package/deployable/authority/data distinctions
  source topology and shared semantic naming
  forward migration, bridge fencing, deletion gates, replaceability
  architecture claim ceilings

Adjacent owners:
  frontend state/topology/realtime -> $frontend-architecture
  Effect Service/Layer/Scope/API/runtime -> $effect-best-practices
  managed Effect API generation -> $effect-api-app-kit
  docs placement and lifecycle -> $docs-governance
```

The project owns product truth, public compatibility, security, privacy,
retention, and destructive decisions.

## Architecture Pass

| Step | Completion criterion |
| --- | --- |
| Ground | Relevant `AGENTS.md`, SSoT, Standards, ADRs, contracts, source, lockfile, tests, and deployable roots are identified; Suite defaults are separated from project facts. |
| Trace | One real intent is followed through authorization, transition, commit, projection, and reconciliation; external inputs include observation/candidate and materialization. |
| Map | Every fact writer, transaction, external effect, resource owner, post-commit carrier, and evidence surface in the slice is named. |
| Classify | Lifecycle stage, P0-P4 pressure, and repository/package/deployable/authority/data boundaries are explicit. |
| Design | The smallest sufficient authority, use-case, port, composition, and consistency seams are chosen; deliberately absent mechanisms are recorded. |
| Place | Private module, semantic filenames, public/wiring surfaces, and any justified promotion are mapped to source. |
| Evolve | One vertical slice can migrate through the seam; temporary bridges have fencing and deletion conditions. |
| Prove | Executed or planned proof matches the claim; observations, inferences, `not_proven`, and `not_claimed` are distinct. |

Escalate when repository authority cannot settle product semantics, final
writers, permissions, privacy/retention, destructive migration, public
compatibility, or irreversible external effects.

## Invariants

```text
canonical accepted fact
  -> one final materialization authority
     within a declared consistency domain and authority epoch

authoritative intent -> Command -> authorize/validate -> transition -> commit
non-authoritative output -> Observation/Candidate -> decide -> materialize -> commit

business authority cell != adapter
internal typed collaboration != generic capability port
external call outside database transaction
accepted fact + canonical event/audit/outbox inside one transaction
composition root selects implementations; product transitions stay in use cases
realtime follows commit and carries dedupe, gap-recovery, and backfill semantics
replaceability requires conformance evidence, not an interface alone

repository boundary != package boundary != deployable boundary
package sharing does not grant fact-writing authority
lexical dot-prefix != module/package/process boundary
```

## Source Topology

```text
repo/
  apps/                 runnable hosts
  packages/             admitted compile/reuse boundaries
  tooling/              checks and repository automation
  docs/                 project authority chain
  specs/                active implementation artifacts when adopted

apps/api/src/
  host/                 config, runtime, resources, composition, shutdown
  modules/<capability>  private authority/capability modules
  workflows/<name>      cross-module orchestration through public surfaces
```

Start with a private module. Inside it, prefer semantic flat files over
technical-layer directory chains. Promote a lexical cluster when ownership,
dependency, lifecycle, compile, trust, or deployment pressure makes the new
boundary enforceable.

```text
<subject>.public.ts   ordinary collaboration surface
<subject>.wiring.ts   host-only construction surface
```

Suite-level machine-readable vocabulary, filename patterns, and guarded terms
are provided by `$ai-coding-os-suite-contracts`. Use
`$evolvable-application-preset` only when those defaults should be resolved into
project-owned Standards.

## Read When Needed

| Condition | Reference |
| --- | --- |
| Establishing the baseline | [Core Doctrine](references/core-doctrine.md) |
| Sizing mechanisms to pressure | [Pressure Profiles](references/pressure-profiles.md) |
| Assigning fact ownership | [Authority Model](references/authority-model.md) |
| Deciding Monorepo and boundary promotion | [Repository Topology and Packaging](references/repository-topology-and-packaging.md) |
| Naming files or admitting subdirectories | [Source Topology and Semantic Naming](references/source-topology-and-semantic-naming.md) |
| Taking over an MVP | [MVP Takeover](references/mvp-takeover.md) |
| Governing generated code changes | [AI Coding Change Protocol](references/ai-coding-change-protocol.md) |
| Designing commands and materialization | [Use-Case Kernel](references/use-case-kernel.md) |
| Isolating providers, devices, or plugins | [Capability Ports](references/capability-ports.md) |
| Handling federation, CRDT, saga, or leader epochs | [Consistency and Authority Topologies](references/consistency-and-authority-topologies.md) |
| Repairing modularity | [Evolutionary Modularity](references/evolutionary-modularity.md) |
| Designing persistence and outbox | [Persistence and Events](references/persistence-and-events.md) |
| Building composition roots | [Composition Roots](references/composition-roots.md) |
| Migrating public or durable state | [Forward Evolution](references/forward-evolution.md) |
| Choosing architecture evidence | [Evidence Harness](references/evidence-harness.md) |
| Auditing an existing repository | [Audit Playbook](references/audit-playbook.md) |
| Architecting LLM/agent products | [Agentic Systems Profile](references/scenario-agentic-systems.md) |
| Mapping common domains | [Scenario Mappings](references/scenario-mappings.md) |
| Implementing in Rust | [Rust Adapter](references/adapter-rust.md) |
| Implementing a TypeScript backend | [TypeScript Backend Adapter](references/adapter-typescript-backend.md) |
| Handing off to frontend architecture | [Frontend Adapter](references/adapter-frontend.md) |
| Adding another ecosystem | [Adapter Authoring Template](references/adapter-authoring-template.md) |

## Output

Always return:

```text
mode
lifecycle_stage
pressure_profile
sources_read
vertical_slice
observed_vs_inferred
critical_authorities
current_pressure
proposed_seam
source_topology_effect
verification_surface
not_proven
not_claimed
```

Add mode-specific detail only when it changes the decision: findings and target
contract for reviews; six-lens map for audits; authority/port/composition map for
designs; bridge ledger for migrations; characterization and first production
slice for MVP takeover.
