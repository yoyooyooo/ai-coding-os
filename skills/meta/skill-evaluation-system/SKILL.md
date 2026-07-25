---
name: skill-evaluation-system
description: >-
  Evaluates and experimentally optimizes Agent Skills with model-run evidence.
  Use for eval-corpus design, rollout analysis, failure attribution,
  instruction/context ablation, candidate comparison, held-out gates,
  checkpoint selection, transfer evaluation, or field-experience intake.
disable-model-invocation: true
---

# Skill Evaluation System

Treat a Skill instruction as a behavioral hypothesis, not as self-validating
prose.

```text
Review proposes.
Rollout observes.
Failure attribution decides what should change.
Held-out gates bound adoption.
```

This Skill absorbs validation-gated skill optimization ideas without turning
product or architecture semantics into trainable benchmark targets.

## Ownership

```text
Owns:
  Evaluation Slice and Agent Capability Profile binding
  direct, routed, repository, long-horizon, and field eval design
  corpus families, split integrity, contamination control
  target-Agent rollout and trajectory capture
  failure attribution before Skill modification
  bounded candidate edits, ablations, baselines, and checkpoints
  hierarchical validation gates and transfer evaluation
  model-run Evidence and field-experience intake

Hands off:
  domain truth and invariant ownership -> the applicable semantic Skill/project Authority
  Suite version adoption and release -> $ai-coding-os-evolution
  proof-surface meaning -> the applicable Harness/Test owner
  Eval artifact placement and lifecycle -> $docs-governance
```

A failed rollout proves a mismatch. It does not automatically prove a Skill
defect.

## Evaluation Coverage

Cover the applicable decisions; do not force the full experimental loop on a
small static contract check.

| Decision | Completion criterion |
| --- | --- |
| Subject | Current Skill, candidate, target Agent profile, task class, Harness, and Oracle are fixed and source-hashed. |
| Corpus | Case families are classified into Discovery/Train, Selection, Sealed Test, and Transfer/Canary without semantic leakage. |
| Baseline | Current, Candidate, Minimal Kernel, and No-Skill baselines are chosen when they answer the question. |
| Rollout | Actual loaded Skill hash, target configuration, tools, trajectories, outputs, scores, costs, and failures are recorded. |
| Attribute | Skill, execution, routing, retrieval, tool, project-knowledge, semantic-owner, evaluator, model-limit, and noise causes are separated. |
| Update | Candidate changes are bounded by semantic change radius; protected invariants and failure cases cannot be edited away. |
| Gate | Evaluation integrity, mechanical integrity, constitutional invariants, protected regression, behavioral utility, efficiency, and transfer are evaluated in order of consequence. |
| Select | Best validation checkpoint, final explored checkpoint, rejected proposals, and rollback anchor remain distinguishable. |
| Report | Evidence states exactly what ran, what improved or regressed, what remained noise, and what was not proven. |

## Core Invariants

```text
train / selection / sealed-test / transfer are distinct
case-family leakage is contamination even when prompts differ
optimizer and candidate author do not see sealed answers
semantic invariants are hard gates, not weighted preferences
one score cannot hide authority, safety, or claim-boundary regressions
latest candidate != best checkpoint != release candidate
failure attribution precedes instruction admission
model self-confidence is not evaluation evidence
no held-out gate -> no autonomous adoption
```

## Skill-Aware Failure Attribution

Classify at least:

```text
skill-defect
execution-lapse
routing-defect
retrieval-defect
tool-interface-defect
project-knowledge-gap
semantic-owner-gap
evaluator-defect
model-capability-limit
stochastic-noise
```

Only a demonstrated Skill defect directly justifies a canonical Skill edit.

## Read When Needed

- Evaluation depth and claim ceilings: [Evaluation Ladder](references/evaluation-ladder.md)
- Split design and contamination: [Corpus and Split Integrity](references/corpus-and-split-integrity.md)
- Failure ownership: [Failure Attribution](references/failure-attribution.md)
- Candidate edits and change budgets: [Bounded Optimization](references/bounded-optimization.md)
- Acceptance policy: [Hierarchical Gates](references/hierarchical-gates.md)
- Instruction/context removal and cross-profile generalization: [Ablation and Transfer](references/ablation-and-transfer.md)
- Reproducible runtime results: [Model-run Evidence](references/model-run-evidence.md)
- Real-session learning: [Experience Intake](references/experience-intake.md)
- SkillOpt mechanisms adopted and bounded here: [SkillOpt-derived Principles](references/skillopt-derived-principles.md)

## Output

Return the evaluation decision, not a claim of universal Skill quality. Make the
subject, corpus split, target profile, baselines, attribution, gate results,
checkpoint, regressions, cost, contamination status, and claim ceiling explicit
at the depth required by the experiment.
