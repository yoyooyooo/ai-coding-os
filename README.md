![](https://github.com/yoyooyooo/ai-coding-os/raw/main/assets/banner.png)

**English** | [中文](README.zh-CN.md)

# AI Coding OS

AI Coding OS is a portable Skill Suite for project-level knowledge, standards,
Authority, architecture, product definition, and bounded proof. It helps Agents
find the owner of a question and preserve durable project semantics without
prescribing one reading, planning, ticketing, or execution workflow.

Use the user-invoked `$ai-coding-os` when ownership is ambiguous or a concern
crosses decision surfaces. Clear concerns go directly to the owning specialist.

## Minimal Knowledge Kernel

```text
Project Authority First
Question-scoped Ownership
One Scoped Meaning, One Current Home
Binding Constraint Is Not Semantic Ownership
Evidence Bounds Claims
Route Is an Edge; Change Creates an Impact Obligation
```

The portable canonical form is carried by `$ai-coding-os-suite-contracts` so it
survives independent or flat installation; this README is the public projection.

The Suite assumes an Agent can choose strategy, infer ordinary reversible details
from applicable project Authority and local patterns, isolate a genuinely
undecidable claim, and continue unaffected work. It does not encode the Agent's
reasoning or implementation order.

`Pass` and decision tables express coverage, not reasoning order. Only an owner
with a real state machine, transaction, migration, safety protocol, or external
protocol may require ordering. Trackers, ticketing Skills, experimental methods,
and release processes own their workflow state outside the core Suite.

## Core Skill Suite

| Group | Skill | Decision surface |
| --- | --- | --- |
| `router/` | `$ai-coding-os` | User-invoked knowledge-owner map |
| `contracts/` | `$ai-coding-os-suite-contracts` | Portable knowledge kernel, Proof Surface, Evidence Envelope, eval and Harness schemas |
| `governance/` | `$docs-governance` | Documentation Authority, Routes, Earned Shape, lifecycle, cleanup, audit |
| `product/` | `$product-definition` | Product framing, source synthesis, business model, decisions, requirements, acceptance |
| `architecture/` | `$evolvable-application-architecture` | Fact authority, transactions, modules, ports, composition, migration |
| `architecture/` | `$frontend-architecture` | Frontend state, feature topology, projections, Query/store/realtime |
| `architecture/` | `$effect-best-practices` | Effect Service/Layer/Scope/runtime, failures, resources, version mapping |
| `capability/` | `$interface-capability-planning` | User work, IA, surfaces, interaction states, frontend ownership, proof needs |
| `harness/` | `$product-harness-system` | Shared Harness vocabulary, coverage, trace, claim ceilings, lifecycle |
| `harness/` | `$headless-product-harness` | Headless commands, fixture/replay, DB/restart, boundary proof |
| `harness/` | `$ui-product-harness` | Interface-headless, render focus, browser-visible proof |
| `harness/` | `$frontend-test-system` | Concrete frontend test-lane and runner selection |
| `preset/` | `$evolvable-application-preset` | Discovery and selective adoption of reusable project defaults |
| `tooling/` | `$effect-api-app-kit` | Atomic generation from a settled Effect API Change Spec |

Every core Skill remains installable independently. Relative links stay inside
one Skill; cross-Skill relationships use `$skill-name` rather than repository
paths. The grouped folders are source-maintenance organization, not runtime
topology.

## Project Knowledge Network

Project documentation is a multi-entry network. An Agent may begin from a
question, code area, term, ADR, schema, test, Harness result, source file,
repository entry, or docs index and follow only relevant links.

```text
Product / Requirements       what should the system do
SSoT                         what shared terms, objects, states, and invariants mean
Standards                    which current rules and quality gates apply
ADR / Product decisions      why a choice was accepted
Architecture                 current topology, ownership, and accepted seams
Protocols / API              what an interface accepts
Source / schema / migrations what implementation structure and static properties exist
Tests / runtime / release    what behavior was observed on a bounded path
Harness / Evidence           which bounded claim has been exercised
Selected execution method    work decomposition, dependencies, status, completion
```

`AGENTS.md` exposes stable project constraints and available knowledge surfaces.
`docs/README.md` may index by question, Authority, code area, or artifact. Neither
is a mandatory traversal root or a copy of current truth.

Portable Skill output paths are candidate defaults. Existing project Homes win;
an external Skill must not create a second glossary, ADR collection, standard,
or execution ledger for a meaning the project already owns.

## Proof And Evidence

The shared Proof Surface separates:

```text
surface_kind       what observation surface was exercised
dependency_reality none / fixture / fake / replay / real_local / real_external
environment_class  isolated / local process / local stack / staging / production
proof_focus        owner-local property such as render_wiring or persistence_restart
```

`none` is reserved for pure static proof and cannot be combined with another
dependency reality.

The optional Evidence Envelope carries bounded evidence only when a real machine
consumer, durable citation, or repeated cross-owner handoff earns a shared
shape. Version 2 is direction-neutral: it preserves source, claim ceiling,
observations, supported interpretation, unproven neighbors, Evidence refs, and
an optional Proof Surface without importing workflow or document lifecycle.

```text
Harness pass != execution completion
execution status != product or document acceptance
accepted target != verified implementation
observed behavior != accepted future intent
```

Source can establish current implementation structure and static properties.
Runtime, reachability, deployment, and environment claims require executed or
observed Evidence; neither source nor Evidence decides accepted product intent.

## Use

Ambiguous or cross-cutting ownership:

```text
Use $ai-coding-os to identify the smallest set of project knowledge owners for
this concern. Do not choose a workflow or create durable state.
```

Documentation convergence:

```text
Use $docs-governance to converge Authority, multi-entry Routes, Earned Shape,
lifecycle, source alignment, and audit findings.
```

Product definition:

```text
Use $product-definition to synthesize sources, model product meaning, challenge
conflicts, record accepted decisions, and produce proportionate acceptance.
```

Application architecture:

```text
Use $evolvable-application-architecture to review fact writers, transactions,
module boundaries, capabilities, composition, migration, and claim ceilings.
```

Interface and proof:

```text
Use $interface-capability-planning for user work, surfaces, states, frontend
ownership, and proof needs. Use the applicable Harness or test owner for the
smallest honest observation surface.
```

Preset and generation:

```text
Use $evolvable-application-preset to discover and selectively adopt compatible
project defaults. Renderer output remains a candidate until project owners
merge selected content into Current Homes. Use $effect-api-app-kit only after
architecture and Effect version decisions are settled.
```

## Core Distribution

The canonical core source is [`skills/**`](skills/README.md). Build a
deterministic core-only grouped-source ZIP, audit JSON, and sidecar manifest:

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run bundle:skills
```

The bundle contains the core Skill Suite and excludes co-located experiments,
CLI packages, project docs, and repository release scripts. It is self-contained:
`skills/VERSION` supplies the Core version, `skills/requirements-audit.txt`
pins audit dependencies, bundle-local audit and builder tools run after
extraction, and `source_tree_sha256` binds the passed audit to the
exact packaged `skills/**` tree. The builder emits a canonical audit, manifest,
change report, and composition review together; machine-absolute paths and
compiler-dependent template-typecheck status are excluded from canonical
provenance so identical source is reproducible across paths. Per-Skill SHA-256
values identify unversioned Skill source.

## Co-located Experiment: Goal Proof

Goal Proof is an early, user-invoked experiment for Goal Pack state, proof steps,
append-only evidence, and completion review. Its long-term usefulness is not yet
established. It is not a core Skill, Router branch, knowledge-network default,
or core bundle member.

- Experiment boundary and Skill: [`experiments/goal-proof/`](experiments/goal-proof/README.md)
- Experimental CLI package: [`packages/cli/`](packages/cli/README.md)
- Historical dogfood: [`experiments/goal-proof/dogfood/`](experiments/goal-proof/dogfood/README.md)

The npm package remains `goal-proof` while the experiment is evaluated:

```bash
npm install -g goal-proof@^0.2.0
goal-proof --help
```

## Repository Layout

```text
skills/                              core AI Coding OS grouped Skill source
  router/ contracts/ governance/ product/
  architecture/ capability/ harness/ preset/ tooling/
experiments/goal-proof/              independent early workflow experiment
packages/cli/                         experimental Goal Proof CLI
scripts/                              repository release support
docs/                                 current project knowledge and standards network
assets/                               README media
```

## Repository Checks

```bash
bun run check:core
bun run check:goal-proof-experiment
bun run check
```

- `check:core`: core Suite audit plus Docs Governance audit.
- `check:goal-proof-experiment`: experimental Skill self-check plus CLI build,
  typecheck, and tests.
- `check`: aggregate repository gate; it does not imply that Goal Proof belongs
to the core Suite.

## Release

`bun run bundle:skills` creates the versioned core Skill bundle without publishing. Core Suite versioning is independent from the CLI package version.

The tag-oriented local release helper only versions and tags the experimental
`goal-proof` CLI package. Actual npm publishing is a separately configured
release step and is not claimed by this repository:

```bash
bun run release:check patch
bun run release patch
```

The npm tarball contains `dist/`, package READMEs, `LICENSE`, and package
metadata. It does not distribute the core Skill Suite.

## License

MIT
