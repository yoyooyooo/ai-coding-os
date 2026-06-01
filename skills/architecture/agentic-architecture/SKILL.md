---
name: agentic-architecture
description: >-
  Defines and audits architecture for AI-agent-era systems: authority
  boundaries, capability ports/adapters, command/projection split,
  evidence/harness gates, composition roots, replaceable providers/runtimes,
  memory/search engine boundaries, plugin boundaries, and anti-corruption
  between agents, tools, transports, and domain facts. Use when designing,
  reviewing, refactoring, or standardizing agentic systems, provider/runtime
  integrations, memory systems, plugin surfaces, SSoT/ADR architecture
  principles, replaceability, composability, or AI-agent execution constraints.
---

# Agentic Architecture

Use this skill as the baseline architecture lens for systems where AI agents,
LLM providers, external runtimes, tools, plugins, memory engines, transports,
or harnesses can influence product behavior.

This skill defines cross-domain doctrine. It should guide frontend, backend,
runtime, memory, harness, Effect, and docs-governance skills, but it must not
absorb their concrete domain rules.

## Collaboration Contract

```text
Owns: authority boundaries, capability port doctrine, adapter candidate
boundaries, command/projection split, composition-root rules, replaceability
rules, agent freedom limits, evidence gate expectations, and architecture audit
lens.
Does not own: project-specific product truth, concrete frontend layout,
framework APIs, Effect Service/Layer details, SQL migrations, concrete harness
commands, Goal Pack state, docs layer lifecycle, or downstream runtime
distribution.
Inputs: user intent, existing SSoT/ADR/standards, code boundary signals,
provider/runtime/memory/tool surfaces, desired replaceability, verification
path, and claim boundary.
Outputs: authority map, port/adapter split, command/projection split,
composition-root placement, agent-freedom boundary, evidence gate, drift list,
blocked decisions, and handoff to domain-specific skills.
Handoff: frontend details -> frontend-architecture; Effect runtime details ->
effect-best-practices; docs placement -> docs-governance; Goal Pack execution
-> goal-proof; shared harness architecture -> product-harness-system; headless
proof -> headless-product-harness; UI proof -> ui-product-harness; interface
contracts -> interface-capability-planning.
Stop: continuing would change product truth, security/private-data posture,
public API/schema/protocol authority, permission model, destructive behavior,
claim ceiling, or a project authority that the agent cannot honestly infer.
```

## Quick Start

1. Classify the task: `new-system`, `capability-slice`,
   `provider-integration`, `runtime-adapter`, `memory-system`,
   `plugin-boundary`, `composition-root`, `harness-readiness`, or `audit`.
2. Read the minimum needed reference:
   - Baseline principles: [Core Doctrine](references/core-doctrine.md).
   - Fact ownership and stop lines: [Authority Model](references/authority-model.md).
   - Ports, adapters, providers, plugins: [Capability Ports](references/capability-ports.md).
   - Binary/server/worker/profile wiring: [Composition Roots](references/composition-roots.md).
   - Proof, claim ceiling, diagnostics: [Evidence Harness](references/evidence-harness.md).
   - Existing repo review: [Audit Checklist](references/audit-checklist.md).
3. Read project `AGENTS.md`, SSoT, standards, ADRs, tests, and package scripts
   as the repo-specific adapter. This skill owns generic doctrine, not project
   facts.
4. When a domain-specific skill clearly owns the concrete rules, use this skill
   first only to settle authority, boundary, replaceability, and evidence shape,
   then hand off.

## Core Model

```text
Product / Domain Truth
  -> Application Service / Policy Decision
  -> Capability Port
  -> Capability Adapter
  -> Composition Root / Deployment Profile
  -> Surface / Agent / Runtime / Tool / Harness
```

Dependency direction points inward. External systems, agents, runtime threads,
tools, plugins, caches, indexes, logs, and transports may propose or observe
state. They do not own accepted business facts unless the project explicitly
declares them as authority.

## Default Architecture Policy

1. Name the product truth before naming the integration.
2. Make every cross-boundary capability a narrow typed port before choosing an
   adapter, SDK, provider, plugin, or runtime.
3. Treat external output as a candidate until an application service validates,
   authorizes, deduplicates, persists, audits, and projects it.
4. Split commands from projections. A command says what should happen; a
   projection says what has been accepted or observed.
5. Keep one core across profiles. Local, cloud, desktop, relay, test, fake, and
   real-runtime profiles change wiring, not domain authority.
6. Put wiring in composition roots. Binaries, servers, workers, CLIs, and
   deployment profiles assemble ports/adapters/config/observability; they do
   not own business rules.
7. Use evidence gates as architecture. Tests, smoke commands, harnesses,
   diagnostics, and `not_claimed` are part of the boundary, not a reporting
   afterthought.
8. Let agents explore freely inside typed constraints. An agent can propose,
   route, plan, call tools, and request actions; it cannot bypass authority to
   create accepted facts.

## Forbidden Defaults

Do not introduce:

```text
plugin-owned domain facts
plugin-owned event spine writes
plugin-owned permission grants
provider-owned memory truth
runtime-thread-owned business completion
transport-owned product state
cache/index/log as source of truth
composition root with business rules
generic platform layer before a real pressure point exists
```

Do not claim replaceability merely because an interface exists. Replaceability
requires narrow output, stable error semantics, fallback or migration behavior,
no authority leakage, and proof that the core does not depend on adapter-private
meaning.

## Routing

- Use this skill before `frontend-architecture` when frontend work touches
  product truth, command/projection semantics, API client authority,
  realtime/event ingestion, provider/runtime output, or harness claim ceilings.
- Use this skill before `effect-best-practices` when the question is which
  capability should be modeled as a Service/Layer and which layer owns the
  fact. Use Effect-specific guidance for concrete API and runtime details.
- Use this skill before harness skills when a proof path might be confused with
  product truth or when the claim ceiling is unclear.
- Use this skill before docs governance only for architecture authority and
  ownership. Use `docs-governance` for document layer placement and cleanup.

## Audit Output

```text
classification:
references_read:
authority_map:
commands_vs_projections:
ports_and_adapters:
composition_root:
agent_freedom_boundary:
replaceability:
evidence_gate:
fits:
drift:
blockers:
auto_fix_candidates:
domain_skill_handoffs:
human_decisions:
verification:
not_claimed:
```
