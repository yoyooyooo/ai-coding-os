---
name: ai-coding-os-evolution
description: >-
  Re-baselines and evolves the AI Coding OS Skill Suite when Agent capabilities,
  real usage, or protected failures change. Use for capability-epoch review,
  cross-Skill simplification, fresh-context audits, instruction/context
  ablation, candidate Suite synthesis, compatibility decisions, release, or
  rollback.
disable-model-invocation: true
---

# AI Coding OS Evolution

The Suite must evolve with the Agent, but it must not circularly authorize its
own replacement.

```text
Preserve semantics; re-earn scaffolding.
Self-observing and self-revising, not self-authorizing.
```

A model release is a probe trigger, not a Suite change Authority.

## Ownership

```text
Owns:
  Agent Capability Profile and capability-epoch triggers
  Suite-level health, overlap, context cost, and marginal-utility review
  fresh-context and first-principles review design
  instruction admission, deletion, relocation, and ablation
  cross-Skill candidate synthesis and compatibility envelopes
  protected failure preservation and release recommendation
  canonical Suite versioning, staged adoption, rollback, and post-release intake

Adjacent owners:
  model-run behavior and held-out evidence -> $skill-evaluation-system
  individual Skill design quality -> the affected Skill owner
  shared machine contracts -> $ai-coding-os-suite-contracts
  documentation lifecycle and Current Homes -> $docs-governance
  domain semantics -> each semantic Skill and project Authority
```

It may propose changes to every Skill, including itself. A candidate has no
release Authority merely because the candidate or its author judges it better.

## Three Evolution Speeds

```text
Semantic Constitution
  slow: Authority, ownership, source/decision distinction, evidence bounds,
  no silent material assumption, current/target/future

Capability Scaffolding
  medium: fixed output templates, detailed steps, examples, reminders,
  static decision trees, compatibility guidance

Evaluation and Tooling
  fast: evals, rubrics, Harnesses, ablations, corpus, reports, release tooling
```

Do not delete a semantic invariant merely because a stronger model can usually
infer it. Do not retain capability scaffolding merely because an older model once
needed it.

## Evolution Coverage

Cover the applicable decisions; Agent count and orchestration remain dynamic.

| Decision | Completion criterion |
| --- | --- |
| Freeze | Current Suite, source hash, accepted release, target Agent Capability Profile, protected corpus, and release Authority are fixed. |
| Intake | Model/provider/tool changes and field observations become explicit capability hypotheses, not immediate edits. |
| Discover | Independent contexts review the Suite without sharing one contaminated narrative; historical failure reasons remain available to at least one review lane. |
| Attribute | Redundancy, overlap, failure, or cost is traced to semantics, scaffolding, routing, retrieval, tools, evaluation, or compatibility. |
| Synthesize | Candidate changes are bounded, owner-aware, source-complete, and preserve rejected-proposal knowledge. |
| Evaluate | Current, Candidate, Minimal Kernel, and No-Suite baselines pass through `$skill-evaluation-system` at the required levels. |
| Decide | Semantic owners accept domain changes; release Authority accepts the Suite; unsupported Agent profiles remain explicit. |
| Release | Manifest, audit, change report, model-run evidence, compatibility boundary, checkpoint, and rollback anchor are retained. |
| Learn | Field corrections enter the next Discovery pool without contaminating the previous sealed Test. |

## Fresh-Context Review Lanes

Use different information conditions rather than identical repeated opinions:

```text
Clean-room Review          current Suite and goals, no historical defense
Failure Archaeology        changelog, protected failures, human corrections
First-principles Rebuild   goals and constraints, not current directory shape
Capability Maximization    interfaces/tools/dynamic Harness/context reduction
Adversarial Review         attack candidate and search for old regressions
Project Simulation         apply to representative real repository tasks
```

The exact number of Agents and sequencing is selected for the current evolution
run; these lanes are coverage, not a fixed workflow.

## Instruction Admission

A hard instruction belongs in a main Skill only when it protects a stable
semantic invariant or a repeatedly observed protected failure and cannot be
better expressed by an interface, type, Tool, test, Reference, rubric, or
project-local Standard.

Disposition options:

```text
retain | narrow | move to Reference | interface | tool | rubric
compatibility overlay | delete
```

## Capability Profiles and Compatibility

Evaluate the actual Agent system, not the foundation model alone:

```text
model and version
reasoning/effort mode
context and Skill loading
available tools and permissions
Harness and memory
subagents / dynamic workflows
cost and latency envelope
target task classes
```

Optimize the canonical Suite for one declared primary baseline. Add a
Compatibility Overlay only when real supported usage earns it; do not mix
multiple capability eras into every core Skill.

## Read When Needed

- Profiles and epoch triggers: [Capability Profile and Epoch](references/capability-profile-and-epoch.md)
- Full lifecycle: [Suite Evolution Cycle](references/suite-evolution-cycle.md)
- Independent review design: [Fresh-context Review](references/fresh-context-review.md)
- Rule admission and context reduction: [Instruction Admission and Ablation](references/instruction-admission-and-ablation.md)
- Candidate scope and cross-owner synthesis: [Candidate Synthesis](references/candidate-synthesis.md)
- Historical failures that changes must continue to protect: [Protected Failure Corpus](references/protected-failure-corpus.md)
- Supported capability boundaries: [Compatibility and Support Envelope](references/compatibility-and-support-envelope.md)
- Adoption, rollback, and evidence: [Release and Rollback](references/release-and-rollback.md)
- Recursively reviewing this Skill: [Self-application](references/self-application.md)

## Output

Return an evolution proposal or release decision with the current and target
Capability Profiles, hypotheses, affected owners, protected invariants,
experimental evidence required, accepted/rejected changes, compatibility
boundary, claim ceiling, and rollback anchor. Do not claim a model-run result
that was not executed.
