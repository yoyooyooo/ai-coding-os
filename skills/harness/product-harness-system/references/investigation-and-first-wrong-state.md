# Investigation and the First Wrong State

> **Find the First Wrong State.** Preserve the original symptom, then follow the causal chain to the earliest owner that diverges from its contract or invariant.

Investigation turns a symptom into a sequence of falsifiable observations. Editing before preserving the failure destroys evidence and encourages coincidence-driven fixes.

## Capture first

```text
exact reproduction command or user path
input and operation identity
environment and dependency reality
version/commit/configuration
full error, stack, Cause, trace, console, or network record
exit status and timing
state before and after where safe
```

## Separate observation from hypothesis

```text
Observation  directly seen
Hypothesis   explanation still open to falsification
Finding      supported explanation that changes the repair
Decision     accepted action and owner
```

## Read the error

Use the complete error, stack, cause, location, and lower-level reason before changing code. Do not replace system evidence with a guessed rewrite.

## Binary reduction

Cut the search space by input, commit range, call stack, service chain, browser step, concurrency set, or dependency reality.

## First wrong state

Follow the causal path until the earliest violated contract or state:

```text
intent -> decode -> policy -> capability -> persistence -> event/projection -> surface
```

The final exception may be several boundaries after the cause.

## Do not blame the platform first

Providers, runtimes, and frameworks have defects, but application misuse and wrong assumptions are usually more likely. Prove the local call contract before escalating.

## Preserve the lesson

After repair:

```text
replay the original failure
search for sibling conditions
place the defense in the lowest reliable owner
remove diagnostic noise that no longer helps
retain the minimum evidence or knowledge future work needs
```

## Related knowledge

- Use [Regression placement](regression-placement.md) for the permanent defense.
- Use [Command and probe design](command-and-probe-design.md) to turn the failure into one command.
- Use [Feedback horizon](feedback-horizon.md) to constrain the repair step.
- Use `$evolvable-application-architecture` for causal architecture boundaries.
- Return to the [Harness map](../SKILL.md).
