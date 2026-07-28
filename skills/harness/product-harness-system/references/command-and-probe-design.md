# Command and Probe Design

A command is an operational entry; a probe is a focused falsifiable observation. Both should reduce uncertainty rather than hide it behind tooling.

## Stable command shape

A useful command declares:

```text
purpose and property
inputs and defaults
scope and dependency reality
side effects
exit status
output location
cleanup and timeout
```

## Read-only first

For migrations, audits, provider checks, and repository rewrites:

```text
inspect or scan
plan/report candidates
dry-run with sample diff
explicit apply
verification
```

These are safety affordances, not a mandatory Agent workflow. A one-shot safe command may combine them when the semantics remain visible.

## Idempotency

Repeated execution should either produce the same result or explain why repetition is unsafe. Destructive operations need operation identity, preconditions, and recovery.

## Exit codes

Use stable non-zero exits for failed properties or command errors. Do not encode failure only in human prose while returning success.

## Output

Prefer text that humans and Agents can inspect. Structured JSON is conditional when a machine consumer exists. Include the first useful error and preserve detailed diagnostics.

## Probe design

A probe should state:

```text
empirical unknown
conditions and environment
observable result
what outcome would falsify the hypothesis
claim limit
whether the probe should be retained
```

A probe that cannot change a decision is noise.

## Safety

Use least privilege, sandbox/workspace bounds, dedicated external accounts, explicit confirmation for irreversible actions, and cleanup. Prompt instructions do not override tool permissions.

## Related knowledge

- Use [Default project verification interface](default-project-verification-interface.md) for command slots.
- Use [Dependency realities](dependency-realities.md) to label the environment.
- Use [Investigation and the first wrong state](investigation-and-first-wrong-state.md) for diagnostic probes.
- Use [Observation limits](observation-limits.md) for conclusions.
- Return to the [Harness map](../SKILL.md).
