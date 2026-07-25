# Docs Layer Model

This reference defines project-agnostic top-level `docs/*` layers. A project may omit layers it does not need. If a layer exists, keep its semantic owner and authority boundary explicit.

## Root Rule

```text
docs/<layer> = durable document type / authority role
docs/<layer>/<partition> = optional project-specific routing partition
docs/<layer>/<partition>/<details> = free-form only after the partition earns it
```

Top-level layers are stable semantic boundaries. Their internal taxonomy follows Earned Shape; see [Earned Shape](elastic-shape-and-identity.md). Layers, routers, source anchors, and direct artifact links form a multi-entry network rather than one reading tree.

## Canonical Vocabulary

Use one canonical name for each top-level role. Avoid singular/plural twins and synonym folders for the same authority.

```text
Core:       product, ssot, standards, adr, architecture, roadmap
Candidate/history: proposals, research, reports
Product:    features, design, interface-capabilities, product-harness
Contracts:  protocols, api, security, data
Operations: runbook, evals, releases
```

This vocabulary is a menu, not an initialization list. A repository can stay flat, use a different declared home, or omit every unused layer.

## Requirements and Product Decisions

Requirements, features, and product decisions use the repository-selected authority home. That may be `docs/features/**`, `docs/requirements/**`, `docs/product/requirements/**`, or an external product system. Docs Governance does not create a mandatory requirements layer or `docs/decisions/pdr`.

The governance contract is invariant across homes:

- one formal current Home for each requirement or decision;
- source material remains source-input or historical-evidence;
- accepted requirements and decisions do not claim implementation completion;
- external systems are linked through a route or an explicitly labeled snapshot.

## Layer Admission

Create a direct child under `docs/` only when all are true:

- it names a durable document role rather than a phase, team, owner, tool, temporary inbox, or personal habit;
- its highest authority differs from existing layers;
- a future reader can choose it without knowing the current roadmap;
- the layer can state `Owns`, `Must Not Own`, entry points, and conflict behavior;
- placing the content inside an existing layer would create durable ambiguity.

File count alone does not earn a top-level layer. Domain-specific complexity belongs inside an existing layer.

## Discouraged Top-level Names

```text
docs/next
docs/tmp
docs/wip
docs/handoff
docs/phase-1
docs/mvp
docs/my-plan
docs/agent-notes
docs/old
docs/archive
```

Route temporary or historical material by semantic role and lifecycle, not by age or project phase.

## Layer Responsibilities

| Layer | Owns | Must not own |
|---|---|---|
| `product` | durable positioning, users, value, principles, non-goals | implementation progress, detailed contracts |
| `features` | detailed user-facing requirements and acceptance scope when the repo needs a dedicated layer | cross-feature shared truth, code completion claims |
| `ssot` | current shared objects, terms, invariants, states, business/domain facts | future complete models, page-specific interaction prose |
| `standards` | enforceable rules, commands, checks, authoring or engineering discipline | aspirations with no current applicability |
| `adr` | accepted technical tradeoffs and consequences | product/business decisions unless the repository deliberately broadens ADR scope |
| `architecture` | current topology, boundaries, accepted seams, deployment shape | product behavior authority, task progress |
| `protocols` / `api` | adopted exchange contracts and usage contracts | roadmap intent, implementation checklist |
| `design` | information architecture, interaction, visual and component behavior | domain truth and backend implementation detail |
| `roadmap` | sequence, prerequisites, gates, capability routes | copied tracker status, shadow SSoT/ADR/Architecture |
| `reports` | durable audit, delivery, experiment, migration, or validation evidence | current authority merely because a report is recent |
| `runbook` | operational procedures and recovery actions | product meaning and design intent |
| `security` | security posture, threat model, sensitive-data rules | general feature scope without security ownership |
| `data` | data model, lineage, retention mechanics, migrations | product priority or user journey |

## SSoT Position

SSoT is the canonical Current Home for shared terms, business objects, states,
invariants, and cross-module semantic facts within their declared scope. It is
not the globally highest file or the answer to every claim. Product decisions
may create an obligation to update shared meaning; Standards or accountable
policy may constrain it; protocols own wire representations; source records
implementation; executed Evidence owns bounded runtime observations.

When SSoT and implementation differ, classify drift instead of silently treating
either as the other's replacement.

## Question-scoped Authority

A global conflict list is misleading. For the current question, identify the
primary semantic owner, applicable binding constraints, and relevant Evidence.
These roles relate without forming a mandatory traversal order.

| Question | Primary semantic owner | Distinct constraints or Evidence |
| --- | --- | --- |
| What should the product or system do? | accepted product/business decision or baselined requirement | binding policy, shared SSoT constraints, delivery Evidence |
| What does a shared term, state, or invariant mean? | SSoT or accepted semantic decision | Product change input, protocols, implementation drift |
| Which rule currently binds work? | adopted Standard or accountable policy owner | enforcement and runtime Evidence |
| Why was a choice made? | product/business decision record or technical ADR | later implementation and outcome Evidence |
| What does an interface accept? | adopted protocol/OpenAPI/schema | contract tests and implementation |
| What implementation exists? | source, schema, migration, lockfile, generated artifact | runtime reachability remains unproven |
| What behavior was observed? | executed tests, Harness, runtime, release, or operational Evidence | accepted intent and whole-capability completion remain separate |
| What is in progress or complete? | repository-selected execution method | release Evidence without Product or Docs promotion |

A newly accepted decision that changes another Current Home creates an impact
obligation: update the affected Home, record temporary drift, lower the related
claim, or state why the impact is not applicable. The affected owners choose the
implementation order.

Each repository may record genuine local exceptions in `docs/README.md` without
creating duplicate Authority.

## Layer README Contract

A durable top-level layer README should state:

- `Owns`;
- `Must Not Own`;
- current Routes or entry surfaces;
- conflict behavior when the layer is authority-heavy;
- promotion/demotion or retention rules when relevant.

A child partition README is a local router. It normally states scope, contents, relevant routes, and genuine local exceptions. It inherits authority from its parent and should not restate a competing global contract.

## Host Language

Follow the nearest repository language policy for narrative prose. Keep machine-facing fields, commands, paths, schemas, code symbols, canonical status values, and portable templates stable when English improves interoperability.
