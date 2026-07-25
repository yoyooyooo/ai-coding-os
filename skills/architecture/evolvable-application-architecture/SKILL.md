---
name: evolvable-application-architecture
description: >-
  Authority-first application architecture for durable facts and change. Use
  when deciding or auditing fact ownership, transactions and use cases,
  capability ports, consistency, composition roots, repository/package/deployable
  boundaries, source topology and naming, forward migration, MVP takeover, or
  replaceability. Frontend and Effect details stay with $frontend-architecture
  and $effect-best-practices.
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

Adjacent Suite owners, when installed:
  product framing, decisions, requirements, and acceptance -> $product-definition
  frontend state/topology/realtime -> $frontend-architecture
  Effect Service/Layer/Scope/API/runtime -> $effect-best-practices
  managed Effect API generation after decisions settle -> $effect-api-app-kit
  proof architecture -> $product-harness-system
```

The project owns product truth, public compatibility, security, privacy,
retention, and destructive decisions.

## Architecture Coverage

Cover applicable decisions in the order exposed by the current architecture pressure; this is not a project workflow.

| Decision | Completion criterion |
| --- | --- |
| Ground | Relevant `AGENTS.md`, SSoT, Standards, ADRs, contracts, source, lockfile, tests, and deployable roots are identified; Suite defaults are separated from project facts. |
| Trace | One real intent is followed through authorization, transition, commit, projection, and reconciliation; external inputs include observation/candidate and materialization. |
| Map | Every fact writer, transaction, external effect, resource owner, post-commit carrier, and evidence surface in the slice is named. |
| Classify | Lifecycle stage, P0-P4 pressure, and repository/package/deployable/authority/data boundaries are explicit. |
| Design | The smallest sufficient authority, use-case, port, composition, and consistency seams are chosen; deliberately absent mechanisms are recorded. |
| Place | Private module, semantic filenames, public/wiring surfaces, and any justified promotion are mapped to source. |
| Evolve | One vertical slice can migrate through the seam; temporary bridges have fencing and deletion conditions. |
| Prove | Executed or planned proof matches the claim; observations, inferences, `not_proven`, and `not_claimed` are distinct. |

Within accepted Product/SSoT, binding constraints, and current source patterns,
choose the smallest final writer and consistency domain as an architecture
decision. Escalate only when materially different choices would change product
semantics, permissions or trust boundaries, irreversible durable data, public
compatibility, binding policy, destructive migration, or irreversible external
effects. If one writer slice remains undecidable, isolate it and continue the
unaffected authority, topology, migration, and proof mapping.

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

Start with a private, semantically flat module. Promote a lexical cluster only
when ownership, dependency, lifecycle, compile, trust, or deployment pressure
makes the boundary enforceable.

Suite-level machine-readable vocabulary and filename patterns come from
`$ai-coding-os-suite-contracts`; `$evolvable-application-preset` resolves
selected defaults into project-owned Standards.

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

Every response includes only the decision-bearing core:

```text
conclusion
core_reasoning
fact_authority_and_ownership_boundary
not_proven
smallest_verification_path
```

Add lifecycle/pressure classification, source topology, diagrams, full module or
port maps, migration plans, bridge ledgers, large risk tables, or persistent
artifacts only when they materially change the answer or the user requests the
corresponding review, audit, design, migration, or takeover branch.
