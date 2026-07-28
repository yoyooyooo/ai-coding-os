# Behavior Evidence and Failure Attribution

Skill behavior should be judged by what changes in fresh realistic tasks, not by prose quality, file count, or one successful conversation.

## Evidence identity

For a meaningful behavior observation, retain enough to distinguish:

```text
task and project context
model and relevant settings
available tools and permissions
Skill/context variant
expected property or decision
actual output or action
runtime or evaluator evidence when used
failure attribution and uncertainty
```

No central schema is required unless a real evaluation system consumes it.

## Fresh context

A Skill should carry enough information for a fresh capable Agent to recover the intended local model. Reusing a conversation that already contains the answer can hide missing routes or definitions.

## Comparison arms

Useful comparisons:

```text
current suite versus candidate
candidate versus minimal kernel
candidate versus no Skill
a short convention versus unconstrained invention
instruction change versus project affordance change
```

Use only the arms that can answer the current question.

## Avoid contamination

Do not let examples, hidden files, previous answers, or evaluator hints reveal the expected solution to one variant but not another. Keep related task families together when separating exploratory and held-out cases.

## Hierarchical evidence

A candidate normally needs to preserve:

```text
semantic correctness
routing and ownership
real task behavior
absence of major induced failure
context cost and discoverability
transfer to more than one narrow example
```

These are evidence concerns, not fixed release gates.

## Attribution before repair

A failure may come from the task prompt, project state, missing tool, model limitation, evaluator, or Skill. Fix the actual owner. Do not add instructions to compensate for a broken probe.

## Protected failures

Retain a historical failure only when it protects a durable semantic distinction or a recurring regression. A large static corpus of obsolete prompt wording can become maintenance noise.

## Related knowledge

- Use [Instruction admission and ablation](instruction-admission-and-ablation.md) for rule changes.
- Use [Portable conventions and defaults](portable-conventions-and-defaults.md) to evaluate deterministic projection.
- Use [Self-application and cargo cult](self-application-and-cargo-cult.md) to challenge evaluation theater.
- Return to the [Evolution map](../SKILL.md).
