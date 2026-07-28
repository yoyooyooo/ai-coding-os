# Instruction Admission and Ablation

> **One Failure, One Lowest Reliable Owner.** Put the lesson into the lowest layer that can prevent or expose the failure reliably before adding another durable instruction.

A new instruction is a hypothesis: adding this text will reliably improve behavior enough to justify its context and maintenance cost.

## Admission test

Before adding a rule, ask:

```text
what recurring failure does it address?
was the failure caused by missing instruction, wrong routing, missing project knowledge, or missing mechanical affordance?
does the rule change an independent decision?
can a type, test, command, tool, or source boundary prevent it more reliably?
can a short example or portable default solve the ambiguity?
what undesirable behavior could the rule induce?
```

One execution mistake does not automatically earn a permanent rule.

## Instruction shape

Prefer:

```text
meaning and boundary
triggering pressure
counterexample or contrast
local autonomy
adjacent owner
```

Avoid:

```text
long choreography
repeated warnings
artifacts required only to prove compliance
fixed agent roles or handoffs
private vocabulary that the project must translate into first
```

## Ablation

Remove or narrow a rule and compare behavior in fresh contexts. Useful comparisons include:

```text
current Skill
candidate Skill
minimal semantic kernel
no Skill / direct project context
candidate plus improved project affordance
```

The goal is causal understanding, not a universal benchmark ritual.

## Failure attribution

When behavior regresses, determine whether the cause is:

```text
semantic instruction defect
routing/context defect
project affordance defect
evaluator or probe defect
model variance or one-off execution
unsupported task/tool/environment
```

Do not restore a rule until its causal value is plausible.

## Context cost

A correct rule can still be harmful when it makes the relevant knowledge harder to find, causes over-structuring, or pushes important project facts out of context.

## Related knowledge

- Use [Behavior evidence and failure attribution](behavior-evidence-and-failure-attribution.md) for comparison evidence.
- Use [Knowledge portfolio](knowledge-portfolio.md) to choose a better owner.
- Use [Portable conventions and defaults](portable-conventions-and-defaults.md) when the problem is repeated invention rather than semantic confusion.
- Return to the [Evolution map](../SKILL.md).
