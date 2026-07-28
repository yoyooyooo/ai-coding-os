# Default Documentation Topology

This reference restores a deterministic cross-project default without requiring identical repositories. Apply it when durable documentation exists and the project has no coherent adopted alternative.

## Required surface when docs exist

```text
docs/
  README.md
```

`docs/README.md` is the documentation router. It links Current Homes and explains local names or deliberate deviations. It does not duplicate the content of those Homes.

If the repository has no durable documentation, do not create `docs/` only to satisfy the Suite.

## Default first-level homes

The following names are reserved defaults. Create a home when durable content of that role first appears; do not create empty folders for symmetry.

| Home | Owns | Must not own |
| --- | --- | --- |
| `docs/product/` | accepted outcomes, users, scope, product rules, quality, acceptance, capability definitions | implementation status, provider details, general architecture |
| `docs/ssot/` | shared product/domain language, objects, states, invariants, cross-capability semantic facts | every project decision, page-specific prose, implementation evidence |
| `docs/standards/` | rules and checks that currently bind work | aspirations with no current applicability or enforcement |
| `docs/architecture/` | current boundaries, fact authority, runtime, composition, repository/deployment shape | product behavior authority, task progress, future target presented as current |

These are the default core homes, not four mandatory empty directories.

## Scope-specific precedence

The core homes are not a universal hierarchy. Their authority depends on the question:

```text
product outcome, rule, scope, quality        -> product
shared term, object, state, invariant        -> ssot
binding engineering or policy rule          -> standards
current implementation boundary or runtime  -> architecture plus source reality
```

For the same scoped claim, an accepted Current Home outranks a derived explanation, point-in-time report, working note, or source input. Source and executed evidence may challenge a stale Home, but they do not silently accept new product meaning.

## Conditional first-level homes

Add a conditional home only when its distinction is durable and an existing home would create long-term ambiguity.

| Home | Pressure that earns it |
| --- | --- |
| `docs/adr/` | accepted technical decisions need append-only history and stable citation |
| `docs/roadmap/` | future sequence, prerequisites, and promotion conditions need a durable route |
| `docs/reports/` | point-in-time audits, experiments, migrations, delivery evidence, or runtime findings need retention |
| `docs/features/` | detailed user-facing capability requirements no longer fit a product-wide home; an existing `requirements/` is a valid local equivalent |
| `docs/design/` | information architecture, interaction states, interface obligations, or visual behavior form durable knowledge; an existing `interface-capabilities/` is a valid local equivalent |
| `docs/product-harness/` | reusable runnable scenarios, observations, and coverage routes need discovery |
| `docs/protocols/` | adopted API, event, file, or exchange contracts need an independent Current Home; an existing `api/` is a valid local equivalent |
| `docs/runbook/` | operational diagnosis, response, and recovery must be found quickly; an existing `operations/` is a valid local equivalent |
| `docs/security/` | threat, sensitive-data, trust, or security-control knowledge has distinct ownership/access |
| `docs/data/` | lineage, retention, migration, analytical contracts, or data quality have independent ownership |
| `docs/research/` | research input and candidate options must remain visibly separate from accepted knowledge; add `proposals/` only when proposal lifecycle itself is a durable route |
| `docs/evals/` | maintained behavioral cases have real runners, oracles, and consumers distinct from ordinary tests |

A repository may use `requirements`, `api`, `operations`, or another coherent local name. Map the local name once in `docs/README.md`; do not create a synonym home beside it.

## Root rule

```text
docs/<home>                         durable semantic role
docs/<home>/<optional-partition>    stable local routing partition
docs/<home>/<partition>/<detail>    only after the partition earns depth
```

Default maximum depth is:

```text
docs/<home>/<optional-partition>/file.md
```

Deeper nesting must solve a real ownership, security, retention, lifecycle, or repeated navigation problem.

## Avoid lifecycle and junk-drawer roots

Do not use top-level homes such as:

```text
docs/old
docs/archive
docs/tmp
docs/wip
docs/handoff
docs/phase-1
docs/mvp
docs/misc
docs/agent-notes
```

History, future, and working material should remain attached to the semantic owner or live in an explicit `reports/`, `research/`, or roadmap surface.

## SSoT position

`docs/ssot/` is the default Current Home for shared terms, objects, states, invariants, and cross-capability semantic facts within its declared scope. It is not the answer to every question and it is not a single global file.

Product decisions may change SSoT. Standards may constrain it. Protocols own wire representation. Source owns implementation reality. Executed evidence owns bounded observation.

## Existing project override

Preserve a coherent existing topology. Rename only when synonym homes, authority ambiguity, or discovery cost is materially harmful. A local project may keep several roles in one `docs/README.md` or one small document while the content remains small.

## Examples and templates

- [Documentation tree example](documentation-tree-example.md)
- [Documentation router template](../templates/docs-README.md)
- [Home router template](../templates/home-README.md)
- [Standards router template](../templates/standards-README.md)

## Related knowledge

- Use [Document naming and local routing](document-naming-and-local-routing.md) for file names and README contracts.
- Use [Default project Standard surfaces](default-project-standard-surfaces.md) for reserved files under `docs/standards/`.
- Use [Earned shape and identifiers](earned-shape-and-identifiers.md) before adding partitions or registries.
- Use [Current Home and knowledge roles](current-home-and-knowledge-roles.md) when placement and authority disagree.
- Return to the [Docs Governance map](../SKILL.md).
