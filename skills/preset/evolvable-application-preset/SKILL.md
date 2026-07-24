---
name: evolvable-application-preset
description: >-
  Agent-guided Evolvable Application Preset discovery and selective adoption.
  Use after technical choices are settled to initialize or incrementally align
  AGENTS.md, project Standards, vocabulary, topology and authority slots,
  Harness discovery, or architecture checks without mechanically replacing
  existing project authority.
---

# Evolvable Application Preset

Turn reusable doctrine into a project-owned resolved snapshot:

> **Skills store knowledge. Presets store defaults. Project docs store adopted
> rules and current facts.**

Use `$docs-governance` only when the repository's canonical entry or docs homes
are missing or disputed. This Preset discovers existing authority first and
contributes only the smallest useful missing or compatible slice.

## Default Operating Mode

The Agent owns discovery, selection, conflict judgment, and adoption. Scripts
are optional deterministic primitives, not a mandatory workflow or a substitute
for repository reading.

```text
settled technical choices + repository evidence
  -> discover current adoption state
  -> map the smallest applicable profile closure
  -> classify each target surface
  -> adopt / merge / keep-project / skip / conflict
  -> verify only the resulting claim
```

Do not require `preset-input.yaml` or `project-overlay.yaml` unless a repeatable
render, diff, fixture, or upgrade candidate benefits from them. Do not reopen
settled technology decisions merely because a profile exists.

## Ownership

```text
Owns:
  profile composition and dependency discovery
  reusable project defaults
  greenfield and incremental adoption guidance
  thin AGENTS.md overlay
  resolved docs templates
  vocabulary and filename baseline
  staged render/diff/upgrade tooling
  golden rendered examples

Project owns:
  product terms and facts
  fact authority
  actual apps/packages/modules
  public contracts
  local security constraints and exceptions
  final resolved files
```

## Authority Model

```text
Preset source
  -> rendered snapshot
  -> project AGENTS.md and docs/** become current authority
```

Each adoption records Preset ID, version, `resolved-snapshot` mode, and selected
profiles. A newer Preset changes nothing until an explicit upgrade stages and
adopts a semantic diff.

The renderer consumes a fixed contract snapshot bundled inside this Skill.
`$ai-coding-os-suite-contracts` owns the source semantics, but the executable
never resolves a sibling Skill path; Suite audit checks snapshot parity.

## Profiles

```text
agent-entry                 implicit thin AGENTS.md managed section
monorepo-core               apps/packages/tooling/docs semantics
typescript-node             requires monorepo-core
react                       requires monorepo-core
effect                      requires typescript-node
effect-httpapi-v3           requires effect; installed v3 policy
effect-httpapi-v4           requires effect; installed v4 policy
verification-core           Harness Descriptor/Result and commands
headless-product-harness    requires verification-core
ui-product-harness          requires verification-core
```

Profiles are a discovery menu. Select the user-visible technology or proof
needs first, then follow local `profiles/*/profile.yaml` requirements to the
smallest closure; dependency profiles are not a request to re-decide technology.
Mutually conflicting profiles must be rejected, for example
`effect-httpapi-v3` and `effect-httpapi-v4` together.

The deterministic renderer is a broad candidate primitive. Its profile list
records the selected closure and gates verification/check outputs, but it is not
an incremental surface selector. For existing projects, the Agent may directly
adopt one surface without rendering the complete candidate.

## Agent Discovery Loop

| Step | Completion criterion |
| --- | --- |
| Ground | Settled technical choices, repository instructions, existing AGENTS/docs, manifests, package/lock evidence, commands, and framework-reserved paths are known. |
| Discover | Each relevant surface is classified as absent, compatible, locally authoritative, conflicting, or not applicable. |
| Map | The smallest profile dependency closure and concrete files/sections that could help are named; a full renderer candidate is optional. |
| Slice | Each surface receives `adopt`, `merge`, `keep-project`, `skip`, or `conflict`, with project authority winning unresolved conflicts. |
| Materialize | The Agent edits directly, uses a local template, or invokes a deterministic script only where that reduces risk or repetition. |
| Verify | Direct adoption checks only the changed surfaces; a rendered candidate uses the scoped `diff`/`validate` primitives and does not imply unselected profile behavior. |
| Continue | Stop when the requested initialization/alignment claim is supported; another slice may be adopted later without completing the whole Preset. |

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

A broad rendered candidate can include the following project-owned surfaces;
profile selection records the selected doctrine and gates optional verification
outputs, while incremental adoption can target any one surface directly:

```text
AGENTS.md
docs/README.md
docs/product/README.md
docs/ssot/README.md
docs/ssot/product-language.md
docs/ssot/authority-map.md
docs/standards/README.md
docs/standards/architecture-profile.yaml
docs/standards/source-topology-and-naming.md
docs/standards/naming-vocabulary.yaml
docs/architecture/README.md
docs/architecture/repository-topology.md
docs/adr/README.md
docs/adr/_template.md
docs/adr/0001-adopt-evolvable-application-preset.md
```

Verification profiles may add:

```text
docs/standards/verification-policy.md
docs/product-harness/README.md
docs/product-harness/coverage.yaml
tooling/architecture_check.py
```

Unknown authority remains `not-yet-established`; templates never invent current
facts.

## AGENTS.md

`agent-entry` is enabled by default. It creates or updates one marked section
that points to project authority, resolved commands, vocabulary, and the thin
`$ai-coding-os` entry. Project-owned sections remain untouched. Nested entries
are generated only for real local differences.

## Optional Deterministic Primitives

Use these when they shorten a discovered slice; they do not define the required
Agent workflow:

```bash
python3 scripts/preset.py inspect --repo <repo>
python3 scripts/preset.py render --input <preset-input.yaml> --overlay <project-overlay.yaml> --out <dir>
python3 scripts/preset.py validate --repo <rendered-or-project-dir>
python3 scripts/preset.py diff --repo <repo> --input <preset-input.yaml> --overlay <project-overlay.yaml>
python3 scripts/preset.py upgrade --repo <repo> --input <preset-input.yaml> --overlay <project-overlay.yaml>
```

`inspect` reports existing surfaces, managed-section presence, adopted profiles,
locks, dependency versions, apps/packages, and commands; it does not choose an
action. `render` is useful for a broad candidate or reproducible fixture. `diff` and
`upgrade` compare only candidate-managed files. `upgrade` writes under
`.evolvable-preset/upgrade-candidate/`; the Agent still decides which compatible
surfaces the project adopts.

## Example

`examples/commerce-platform/` contains optional renderer inputs and the
canonical `expected/` fixture. Read it when repeatable broad rendering is useful;
it is not the required shape for incremental adoption.
