# ADR: Core Knowledge Network And Goal Proof Experiment Boundary

## Status

Accepted

Supersedes the Goal Proof membership and Router decisions in [2026-05-28 AI Coding OS Naming And Boundary](2026-05-28-ai-coding-os-naming-and-boundary.md). The AI Coding OS and `goal-proof` names remain unchanged.

## Context

AI Coding OS had converged on strong decision-surface ownership, but several public surfaces still linearized the system:

- Router procedures and takeover recipes resembled a central workflow.
- `AGENTS.md`, Preset and docs routers generated `Read First` sequences.
- Docs Governance described one `AGENTS -> docs -> layer` traversal.
- Goal Proof and four internal phase Skills remained in the core roster and Evidence schema.
- Core bundle and audit included the Goal CLI despite its uncertain experimental value.

The intended product is a project-level knowledge, standards, Authority, architecture, product and proof-semantics network. Workflow selection, ticket decomposition, dependency graphs, assignment and completion can be owned by independent Skills or external systems.

## Decision

Adopt these boundaries:

1. Core AI Coding OS source remains under `skills/**` and contains only knowledge, governance, product, architecture, interface, proof, Preset and deterministic generation owners.
2. A Route is a discoverable edge, not a mandatory sequence. Repository entries and docs indexes expose multiple starting surfaces.
3. Owner-local Pass sections describe coverage and completion criteria. Only real state machines, transactions, migrations, safety protocols and external protocols may prescribe order.
4. Trackers, ticketing Skills, release processes and experimental methods remain outside the core Router roster and own their own execution lifecycle.
5. Goal Proof becomes a user-invoked co-located experiment under `experiments/goal-proof/**`. Its four phase Skills collapse into one independently installable Skill with conditional references.
6. The Goal Proof CLI remains under `packages/cli/**` and continues using the `goal-proof` npm name while the experiment is evaluated.
7. Core Evidence Envelope v2 is optional and direction-neutral. It carries only a bounded source reference, claim ceiling, observations, support, unproven neighbors, Evidence refs, and optional Proof Surface; workflow-specific states and completion semantics stay with the external owner. Legacy directional v1 is reader-only compatibility.
8. Core Suite audit, manifest and ZIP exclude experiments, CLI packages, project docs and release scripts. Goal Proof has an independent self-check and CLI test gate.
9. Historical Goal evidence moves with the experiment and remains append-only; old paths inside evidence records remain historical facts.
10. Cross-Skill doctrine converges on six non-procedural principles: Project Authority First, Question-scoped Ownership, One Scoped Meaning/One Current Home, Binding Constraint Is Not Semantic Ownership, Evidence Bounds Claims, and Route/Impact Obligation.
11. Host instructions constrain Agent conduct but do not become a global semantic authority; no numbered file precedence applies across claim types.
12. Source establishes implementation structure and static properties; runtime, reachability, deployment, and environment behavior require executed or observed Evidence.
13. Handoff shapes, Router YAML, decision queues, global Authority maps, and Artifact Graph metadata are optional and require a real consumer or durable pressure. A scoped technical fact-writer map may live under Architecture when real writer/transaction decisions earn it.
14. Preset adoption is incremental by default for existing repositories; broad render does not earn empty Docs layers or a second product-language Home.
15. Specialist uncertainty blocks only the affected claim or mutation when Evidence can be preserved; unaffected work continues. Architecture decides ordinary final-writer and consistency boundaries inside accepted Product/SSoT/binding constraints.
16. InterfaceCapability status describes definition lifecycle only. Product/design acceptance, implementation proof, Harness result, and regression state remain separate.
17. Preset `render` emits `candidate-snapshot` content with proposed ADRs and candidate Standards; it never self-asserts accepted/current Authority. Technical fact writer maps belong under Architecture, not SSoT.
18. Pure static proof uses `dependency_reality: [none]`; Harness v2 rejects legacy/canonical double-writing and known conflicting aliases. Effect Kit P3 emits Descriptor v2 only from a project-provided Harness binding; command success and schema validity do not prove declared coverage.
19. Core ZIP is self-contained through `skills/VERSION`, bundle-local links/tools, and an audit `source_tree_sha256` that must match the packaged tree. Canonical release audit normalizes machine-local path/compiler diagnostics and is emitted as a real sidecar so release artifacts are cross-path deterministic.
20. Preset profile provenance keeps user requests, system defaults, transitive dependencies, and resolved closure separate. Language-neutral topology/verification profiles do not silently adopt TypeScript filename contracts.

## Alternatives

### Keep Goal Proof as an optional core Router branch

Rejected. Optional activation prevented automatic use but did not remove context load, roster membership, core schema coupling, bundle inclusion or the impression that AI Coding OS had a preferred execution method.

### Put one `CONTEXT.md` beside every source module

Rejected as a default. Local files improve incidental discovery but tend to mix Product, SSoT, Architecture, ADR, Contract and execution narratives. Multi-entry Routes and code-area projections solve discovery without a parallel documentation taxonomy.

### Require planning-first traversal through `AGENTS.md` and `docs/README.md`

Rejected. It replaces one workflow with another. Agents may enter from any relevant question, code area, term, artifact, source or Evidence surface.

### Add a central graph or Authority Registry

Deferred until stable machine routing, cross-repository identity or audit pressure earns it. Markdown routes and semantic paths are sufficient for the current claim.

## Consequences

- Core Skill count decreases from 19 to 14.
- `$ai-coding-os` no longer routes Goal Proof or other external execution methods.
- Goal Proof becomes user-invoked and self-contained; the retired public phase names are not core triggers.
- Preset output uses `Knowledge Surfaces`, `Discovery Surfaces` and `Routes` instead of ordered `Read First` sections.
- Docs Governance checks declared route integrity without enforcing a reading order or default decision queue.
- Preset source-naming output references project SSoT product language instead of copying its meaning, validation follows declared managed surfaces rather than a complete docs tree, and rendered files remain candidates until project-owner adoption.
- Definition acceptance, implementation structure, observed behavior, Harness proof, and execution completion remain distinct claims.
- Core release audit is rejected when its source-tree hash differs from the packaged `skills/**`.
- Root repository checks distinguish core and experiment claims.
- Installing from the core Suite ZIP cannot accidentally install Goal Proof.
- The npm package still publishes the experiment CLI and is not the distribution channel for core Skills.

## Evidence

- Core SSoT: [../ssot/README.md](../ssot/README.md)
- Core architecture: [../architecture/repository-layer-breakdown.md](../architecture/repository-layer-breakdown.md)
- Core source standard: [../standards/skill-source-layout.md](../standards/skill-source-layout.md)
- Experiment boundary: [../../experiments/goal-proof/README.md](../../experiments/goal-proof/README.md)
- Verification:
  - `bun run check:core`
  - `bun run check:goal-proof-experiment`
  - `bun run check`
  - `bun run bundle:skills`
