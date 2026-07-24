![](https://github.com/yoyooyooo/ai-coding-os/raw/main/assets/banner.png)

**English** | [中文](README.zh-CN.md)

# AI Coding OS

AI Coding OS is a grouped methodology and Skill Suite for repository/workspace
work. It provides a thin user router, project documentation authority,
evolvable application architecture, interface capability planning, Product
Harnesses, an optional Goal Pack method, reusable Presets, and deterministic
generation tools.

Use the user-invoked `$ai-coding-os` for ambiguous or cross-cutting work. Clear
requests go directly to the specialist that owns the decision surface.

## Core Principles

```text
project authority first
one primary owner per decision surface
proof surface matches the claim
observed / supports / not_proven stay distinct
Preset produces a resolved snapshot
cross-Skill dependencies use `$skill-name`, not install paths
structured artifacts earn their lifetime
```

This is not a formal proof system and does not prescribe one execution flow.
Architecture and governance constrain durable semantics; each task selects its
implementation strategy from project authority, risk, and available evidence.

## Skill Suite

| Group | Skill | Role |
| --- | --- | --- |
| `router/` | `$ai-coding-os` | User-invoked router selecting Lead and Supporting Skills |
| `contracts/` | `$ai-coding-os-suite-contracts` | Independently installable cross-Skill coordination, shared vocabulary, and Harness schemas |
| `goal/` | `$goal-proof` | Explicitly selected Goal Pack, proof-step, evidence, and completion method |
| `goal/` | `$goal-contracts` | Create or repair `goal.yaml` |
| `goal/` | `$finding-proof-step` | Find the next falsifiable `proof_step` |
| `goal/` | `$proof-step-implementation` | Execute, verify, append evidence, reduce progress |
| `goal/` | `$write-work-plans` | Write `plans/<work_id>.md` for selected high-risk work |
| `governance/` | `$docs-governance` | Docs layers, AGENTS.md, authority placement, cleanup, audit |
| `architecture/` | `$evolvable-application-architecture` | Authority, transactions, ports, composition, Monorepo/source topology, migration |
| `architecture/` | `$frontend-architecture` | Frontend state authority, feature topology, host composition, realtime reconciliation |
| `architecture/` | `$effect-best-practices` | Effect Service/Layer/Scope/runtime, failures, resources, version mapping |
| `capability/` | `$interface-capability-planning` | UI/IA capability, surfaces, state/data ownership, proof handoff |
| `harness/` | `$product-harness-system` | Shared Harness vocabulary, descriptors/results, coverage, claim ceilings, lifecycle |
| `harness/` | `$headless-product-harness` | Capability commands, fixture/replay, DB/restart, boundary proof |
| `harness/` | `$ui-product-harness` | Interface-headless, render-wiring, browser-visible proof |
| `harness/` | `$frontend-test-system` | Concrete frontend test-lane and runner selection |
| `preset/` | `$evolvable-application-preset` | Agent-guided discovery and selective adoption of project-owned AGENTS/docs/check defaults |
| `tooling/` | `$effect-api-app-kit` | Atomically generate an Effect API capability slice from a settled Change Spec |

## Goal Proof State Transition

`$goal-proof` is an optional durable execution method selected explicitly by
the user or repository. Once selected, it advances through intent-to-evidence
state transitions:

```text
human intent -> goal contract -> proof_step -> evidence -> next_action
```

The formal method name is Goal Proof System. The formal CLI is `goal-proof`.

## Core Vocabulary

| Term | Meaning |
| --- | --- |
| Goal Pack | Durable completion unit for one long-running goal |
| Goal Contract | `goal.yaml`; goal authorization, boundaries, completion criteria, claim limit |
| Proof Step | `progress.yaml.proof_step`; current falsifiable movement from state A to state B |
| Proof Path | Runnable or inspectable path that can support or falsify the proof step |
| Work Item | Bounded unit inside `progress.yaml.work_items`, usually `W###` |
| Evidence Record | Append-only JSONL entry in `evidence.jsonl`, usually `E###` |
| Completion Review | Final review evidence that maps evidence back to `completion.required_evidence` |
| Claim Limit | What the current goal or proof may and may not claim |
| Gap | Uncovered claim area, missing evidence, unresolved decision, or human-intervention point |
| Goal Thread | Shared `relations.thread_id` label across related Goal Packs |
| Goal Relation | Typed metadata link from one Goal Pack to another |
| Derived Graph View | CLI-rendered view from relations; not stored planning state |

## Goal Proof System

Goal Proof System is the Suite's optional long-running goal carrier.

```text
human intent
  -> goal.yaml goal contract
  -> progress.yaml proof_step
  -> evidence.jsonl evidence
  -> apply progress
  -> next_action: proof_step | continue | needs_plan | blocked | review | done | needs_human
```

A Goal Pack is ready when the goal contract is stable and the next
`proof_step` is authorized to produce or inspect `completion.required_evidence`
inside `claim_limit`. It is not ready merely because a work item list exists.

Work items and checks are execution details, not required top-level concepts in
the goal loop.
Use `plans/<work_id>.md` only when a selected work item is high risk and needs a
reviewed execution plan before implementation. It is not a second task system.

Completion requires a review evidence record with `completion_satisfied: true`
and `claim_evidence` mapping each completion claim to evidence.
Cross-method Evidence Envelope Discipline is owned by SSoT / Goal Proof.
`changed surfaces` and `not_proven` are narrative envelope concepts here, not
formal v2 schema fields unless templates and checkers are explicitly upgraded.

## Goal Pack Files

```text
docs/goal-proof/
  README.md
  inbox/
  sources/
  goals/<goal-id>/
    goal.yaml
    progress.yaml
    evidence.jsonl
    plans/<work_id>.md  # only when needs_plan
    interface-capabilities.yaml  # optional UI/interface trace companion
    product-harness.yaml  # optional harness proof companion
    notes/
```

`goal.yaml` owns objective, authority refs, engineering guidance, completion,
claim limit, stop rules, and agent authority. `progress.yaml` owns runtime
state, active work item, proof step, blockers, last check, and next action.
`evidence.jsonl` is append-only evidence. `notes/` stores long context only.

## Interface Capability And Harness

UI and harness skills let agents validate product capability from both
directions:

```text
Product Capability
  -> InterfaceCapability
  -> InterfaceSurface / Region
  -> Interaction State Contract
  -> Frontend State/Data Ownership
  -> Harness Scenario
  -> Headless Proof and/or UI Proof
  -> Evidence
  -> Claim / Gap
```

When the final UI is not fixed, agents can still use harness routes, harness
components, interface-headless tests, or browser-visible candidate paths to
prove local behavior. When the production interface stabilizes, reusable proof
paths can become regression coverage.

Durable placement:

- Workspace interface trace: `docs/interface-capabilities/**`
- Workspace harness contract: `docs/product-harness/**`
- Goal-local interface companion: `docs/goal-proof/goals/<goal-id>/interface-capabilities.yaml`
- Goal-local harness companion: `docs/goal-proof/goals/<goal-id>/product-harness.yaml`

## Install

Install the CLI:

```bash
npm install -g goal-proof
goal-proof --help
```

Install all AI Coding OS skills:

```bash
npx skills add https://github.com/yoyooyooo/ai-coding-os -g --agent '*' --skill '*' --full-depth -y
```

Codex-only:

```bash
npx skills add https://github.com/yoyooyooo/ai-coding-os -g --agent codex --skill '*' --full-depth -y
```

The repository and skill suite name is AI Coding OS. The CLI and npm package
remain `goal-proof`. Installers may flatten or rearrange Skill directories:
relative links stay inside each Skill, while cross-Skill dependencies resolve by
`$skill-name`. The independently discoverable shared-contract entry is
`$ai-coding-os-suite-contracts`, not a grouped repository path.

## Use

Normal workspace work:

```text
Use $ai-coding-os:
I want to govern / plan / implement / audit ...
Context: ...
Boundaries: ...
Acceptance: ...
```

Long-running goal:

```text
Use $goal-proof:
Goal: ...
Context: ...
Boundaries: ...
Acceptance: ...
Stop conditions: ...
```

UI capability planning:

```text
Use $interface-capability-planning:
Split product intent into InterfaceCapability, surface, interaction state,
frontend state/data ownership, and harness needs.
```

UI proof:

```text
Use $ui-product-harness:
Plan interface-headless, render wiring, browser-visible proof, evidence, gaps,
and claim_ceiling for this InterfaceCapability.
```

Headless proof:

```text
Use $headless-product-harness:
Design the smallest proof command, fixture/replay path, headless command output
envelope, and the `not_proven` gaps for this capability.
```

Docs governance:

```text
Use $docs-governance:
Check docs layers, authority placement, README routes, obsolete planning docs,
and audit.
```

This repository's docs layer rules live in `docs/standards/docs-governance.md`;
public skill source layout and trigger-name rules live in
`docs/standards/skill-source-layout.md`.

Architecture baseline:

```text
Use $evolvable-application-architecture:
Review authority, transactions, Capability Ports / Adapters, composition roots,
source topology, migrations, replaceability, and claim ceilings.
```

Project Preset:

```text
Use $evolvable-application-preset:
Start from settled technical choices and existing project authority, discover the smallest profile closure, and incrementally adopt compatible AGENTS/docs/check surfaces; rendering is optional.
```

Effect API scaffold:

```text
Use $effect-api-app-kit:
Plan, apply, and verify one atomic capability slice from a settled Change Spec.
```

## CLI Quick Inspect

```bash
goal-proof summary .
goal-proof list . --completion todo
goal-proof inspect <goal-pack> --json
goal-proof work list <goal-pack>
goal-proof evidence list <goal-pack> --limit 5
goal-proof relations goals . --thread <thread-id> --completion todo --json
goal-proof relations work . --thread <thread-id> --completion todo --json
goal-proof relations check . --thread <thread-id>
goal-proof relations graph . --thread <thread-id>
goal-proof work brief <goal-pack>
goal-proof check <goal-pack>
```

Relations commands inspect cross-pack continuity and discover thread-member
candidates. They do not create a queue, worklist, scheduler, thread lifecycle,
stored graph, or execution order. `relations.thread_id` is a label only.

## CLI Reference

```bash
goal-proof --help
goal-proof <command> --help
goal-proof inspect <goal-pack> [--json]
goal-proof summary [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--depth repo|groups|items] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof list [project-root|goals-dir] [--completion all|todo|done] [--status <status>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work list <goal-pack> [--completion all|todo|done] [--status queued|active|blocked|done] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof work brief <goal-pack> [--work <id>] [--json]
goal-proof work activate <goal-pack> --work <id> [--dry-run]
goal-proof evidence list <goal-pack> [--limit N] [--work <id>] [--type discovery|decision|implementation|coordination|review|planning] [--result done|blocked] [--decision <value>] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--completion-satisfied true|false] [--changed-file <glob>] [--command-status pass|fail] [--contains <text>] [--include fields] [--show-empty] [--json]
goal-proof evidence show <goal-pack> --index N [--json]
goal-proof evidence add <goal-pack> (--file evidence-record.json | --json '<json>' | --stdin) [--apply] [--check] [--dry-run]
goal-proof relations list [project-root|goals-dir] [--thread <id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations goals [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status forming|ready|running|blocked|done|retired] [--next-action proof_step|continue|needs_plan|blocked|review|done|needs_human] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations work [project-root|goals-dir] [--thread <id>] [--completion all|todo|done] [--status queued|active|blocked|done] [--goal-completion all|todo|done] [--goal-status forming|ready|running|blocked|done|retired] [--goal <goal-id>] [--limit N] [--include fields] [--show-empty] [--json]
goal-proof relations check [project-root|goals-dir] [--thread <id>] [--json]
goal-proof relations graph [project-root|goals-dir] [--thread <id>] [--json]
goal-proof apply <goal-pack> [--dry-run]
goal-proof check <goal-pack>
```

Typical loop:

```text
check -> inspect -> work brief -> work -> evidence add -> apply -> check
```

Use a bare goal id when running inside a project with
`docs/goal-proof/goals/<goal-id>`, or pass the goal folder.

## Repository Layout

```text
packages/cli/                         TypeScript CLI, built with Bun
skills/router/                        OS entry and user intent routing
skills/goal/                          Goal Pack method and execution phases
skills/governance/                    Docs layer governance
skills/architecture/                  application / frontend / Effect doctrine
skills/capability/                    Interface capability planning
skills/harness/                       shared, headless, UI, frontend-test guidance
skills/preset/                        resolved project defaults
skills/tooling/                       executable profiles and source audit
skills/contracts/                     independently installable AI Coding OS Suite contracts
skills/examples/                      owner-local examples index
skills/README.md                      grouped source index
docs/                                 Workspace documentation and Goal Pack examples
assets/                               README media
```

## Release

Publishing is tag-driven through GitHub Actions and npm Trusted Publishing.

```bash
bun run release:check patch
bun run release patch
# or
bun run release 0.2.0
```

`bun run release:check` validates release readiness without changing files.
`bun run release` creates a temporary local release branch, updates package
versions, commits, tags `vX.Y.Z`, pushes only the tag to the configured public
GitHub release remote, then returns to the original branch. GitHub Actions
publishes the npm package from the tag. Local AGS remotes may be used for LAN
sync, but they are not the release trigger.

The npm tarball contains only `dist/`, `README.md`, `README.zh-CN.md`,
`LICENSE`, and package metadata.

## Development

```bash
bun install
python3 -m pip install -r requirements-dev.txt
bun run build
bun run typecheck
bun run test
bun run check
python3 skills/tooling/suite_audit.py --suite skills
python3 skills/governance/docs-governance/scripts/run_docs_audit.py --repo .
```

The CLI source is TypeScript. `bun build` emits npm package artifacts under
`packages/cli/dist/`.

## License

MIT
