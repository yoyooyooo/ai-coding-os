---
name: evolvable-application-preset
description: >-
  Evolvable Application Preset discovery and selective adoption. Use when
  settled technical choices need a new or existing repository to adopt the
  smallest compatible AGENTS.md, Standards, vocabulary, topology, authority,
  Harness, or architecture-check surface while preserving project authority.
---

# Evolvable Application Preset

Turn reusable doctrine into a reviewable candidate that project owners may adopt:

> **Skills store knowledge. Presets store defaults. Project docs store adopted
> rules and current facts.**

Use `$docs-governance` only when the repository's canonical entry or docs homes
are missing or disputed. This Preset discovers existing authority first and
contributes only the smallest useful missing or compatible slice.

## Adoption Model

The Agent owns discovery, selection, conflict judgment, and adoption. Scripts
are optional deterministic primitives, not a project workflow or a substitute
for repository evidence.

```text
inputs: settled technical choices + repository evidence
coverage: current surfaces + smallest profile closure + conflicts
surface decisions: adopt | merge | keep-project | skip | conflict
claim: only explicitly adopted and verified project surfaces
```

Keep `preset-input.yaml` and `project-overlay.yaml` optional; use them when a
repeatable render, diff, fixture, or upgrade candidate benefits. Treat settled
technology decisions as constraints on profile discovery.

## Ownership

```text
Owns:
  profile composition and dependency discovery
  reusable project defaults
  greenfield and incremental adoption guidance
  thin AGENTS.md overlay
  earned-shape-aware candidate docs templates
  language-neutral vocabulary plus selected ecosystem naming projections
  staged render/diff/upgrade tooling
  golden rendered examples

Project owns:
  product terms and product decisions
  fact authority
  actual apps/packages/modules
  public contracts
  local security constraints and exceptions
  final resolved files

Adjacent Suite owners, when installed:
  application architecture semantics -> `$evolvable-application-architecture`
  cross-owner architecture decisions, ADIR, health, and diff -> `$architecture-decision-system`
  frontend projection -> `$frontend-architecture`
  Effect constraints -> `$effect-best-practices`
  Rust projection -> `$evolvable-application-architecture` Rust reference
  deterministic code generation after decisions settle -> `$effect-api-app-kit`
  documentation authority and placement conflicts -> `$docs-governance`
```

## Authority Model

```text
Preset source
  -> rendered `candidate-snapshot`
  -> semantic owners explicitly merge selected content into project Current Homes
```

A repeatable render records Preset ID, version, `candidate-snapshot` mode, and
selected profiles. `application-core` is language-neutral; repository, TypeScript, Rust, Frontend, Effect, and verification concerns remain separately selectable. Generated AGENTS, Standards, ADRs, SSoT, and Architecture
files remain proposed and must not self-assert accepted/current status. A direct
incremental adoption may update only one existing project surface without
creating a parallel snapshot artifact. Legacy `resolved-snapshot` remains
readable, but new renders are candidates. A newer Preset changes nothing until
an explicit upgrade stages and the project adopts a semantic diff.

The renderer consumes a fixed contract snapshot bundled inside this Skill.
`$ai-coding-os-suite-contracts` owns the source semantics, but the executable
never resolves a sibling Skill path; Suite audit checks snapshot parity.
Docs layer placement, partition admission, and identity admission remain owned
by `$docs-governance`; the Preset supplies candidate defaults with explicit
provenance, while project owners create the adopted result.

## Profile Discovery

Treat local `profiles/*/profile.yaml` files as the profile catalog. Start from
settled user-visible technology or proof needs, follow `requires` to the
smallest closure, and reject conflicting profiles. Dependencies complete a
selection while leaving technology decisions settled. Resolved artifacts record
requested profiles, resolved closure, and dependency-added profiles; adopted
vocabulary, filename patterns, guarded terms, AGENTS rules, and optional
verification files come only from that closure.

The renderer records a broad candidate closure, not an incremental surface
selector. `requested`, `defaults_added`, `dependency_added`, and `resolved` stay
separate so a system default is never presented as user intent. Existing
projects may adopt one compatible surface directly without rendering the
complete candidate.


## Language and Repository Profiles

```text
application-core  authority-first semantics and pressure-driven boundary promotion
monorepo-core     optional workspace topology; never implied by a language
typescript-node   TypeScript filename/import projection; requires application-core
rust              Rust module/crate/trait/lifecycle projection; requires application-core
react / effect    compose on the TypeScript projection
```

Selecting TypeScript does not select a monorepo. Selecting Rust does not imply
Tokio, Axum, SQLx, a multi-crate workspace, or a microservice. Profiles expose
candidate constraints; repository evidence and settled technical choices decide
the concrete shape.

## Adoption Coverage

Cover applicable rows in the order suggested by current evidence. The table is
not a repository reading or implementation sequence.

| Decision | Completion criterion |
| --- | --- |
| Context | Settled technical choices, repository instructions, existing AGENTS/docs, manifests, package/lock evidence, commands, and framework-reserved paths are known. |
| Surface discovery | Each relevant surface is classified as absent, compatible, locally authoritative, conflicting, or not applicable. |
| Profile mapping | The smallest profile dependency closure and concrete files/sections that could help are named; a full renderer candidate is optional. |
| Surface decision | Each surface receives `adopt`, `merge`, `keep-project`, `skip`, or `conflict`, with project authority winning unresolved conflicts. |
| Materialization | The Agent edits directly, uses a local template, or invokes a deterministic script only where that reduces risk or repetition. |
| Verification | Direct adoption checks only the changed surfaces; a rendered candidate uses the scoped `diff`/`validate` primitives and does not imply unselected profile behavior. |
| Completion | Stop when the requested initialization/alignment claim is supported; another slice may be adopted later without completing the whole Preset. |

Keep the surface map inline unless persistence materially improves review or
repeatability:

```text
surface | current authority | Preset contribution | action | verification
```

### Adoption Shapes

- **New project:** a broad first slice is allowed when target homes are absent
  and the technical choices are settled.
- **Existing project:** prefer incremental compatible slices; never require a
  full re-render before adopting one useful standard or AGENTS section.
- **Upgrade:** stage only affected managed surfaces and review a scoped semantic
  diff; unchanged project-owned files are not candidate deletions.

## Project Output

A broad candidate may contribute one marker-bounded `AGENTS.md` section,
project-owned Standards and ADR surfaces, and selected verification or checker
surfaces. SSoT candidates appear only for explicit product-language material.
Architecture candidates appear for fact-writer or topology material, and
technical writer maps use `docs/architecture/fact-authority-map.md`; an empty
Product, SSoT, Architecture, or Harness layer is not generated. Profiles
define the technical closure; exact files are inspected in the candidate or
golden fixture. Incremental adoption may target any one compatible surface and
is the default for existing repositories.

This is a menu, not a mandatory docs tree. Projects may omit unused layers,
keep layers flat, and admit child partitions or identities only under
`$docs-governance`. Product meaning remains in its project SSoT; generated
source-naming vocabulary references that Home instead of copying its meaning.
Unknown authority remains `not-yet-established`; templates preserve that gap
instead of inventing current facts.

Read the [commerce-platform example](examples/commerce-platform/README.md) only
when a repeatable broad render or fixture comparison is needed.

## AGENTS.md

`agent-entry` is added as an explicit recorded default. It creates or updates
one marked section that points to project authority, resolved commands,
vocabulary, and the optional thin `$ai-coding-os` entry. Project-owned sections
remain untouched. Nested entries
are generated only for real local differences.

## Optional Deterministic Primitives

Use these when they shorten a discovered slice; they do not define project
exploration or adoption order:

```bash
python3 scripts/preset.py inspect --repo <repo>
python3 scripts/preset.py render --input <preset-input.yaml> --overlay <project-overlay.yaml> --out <dir>
python3 scripts/preset.py validate --repo <rendered-or-project-dir>
python3 scripts/preset.py diff --repo <repo> --input <preset-input.yaml> --overlay <project-overlay.yaml>
python3 scripts/preset.py upgrade --repo <repo> --input <preset-input.yaml> --overlay <project-overlay.yaml>
```

`inspect` reports existing surfaces, managed-section presence, adopted profiles,
locks, dependency versions, apps/packages, and commands; the Agent chooses the
action. For an existing repository, direct adoption after `inspect` is the
normal path. `render` is an explicit broad candidate or reproducible fixture;
it is not a prerequisite for one-surface adoption. `diff` and `upgrade` compare
only candidate-managed files. `upgrade` writes under
`.evolvable-preset/upgrade-candidate/`; the Agent still decides which compatible
surfaces the project adopts.


## Cross-Language Profile Boundary

`application-core` carries reusable authority, use-case, capability, composition, evolution, and evidence defaults. `monorepo-core` adds only workspace repository topology. `typescript-node` selects TypeScript naming and import projections. `rust` selects Rust module, crate, trait, async-lifecycle, public-API, and proof guidance without inheriting TypeScript filenames or Monorepo topology. A project may combine `rust` with `monorepo-core` when a Cargo workspace has earned that shape, but neither profile implies the other.
