# Dependency Realities

Name the dependency reality honestly. A green test with a fake is evidence about a different world than a run against the real provider.

## Stable labels

### Fixture

Static input or output data. It does not execute the dependency's behavior.

### Fake

A deterministic behavioral replacement implemented for testing or local use. It may model the contract but not the real provider's timing, limits, faults, or quirks.

### Replay

Recorded interaction played back. It preserves selected real examples but not current provider state, concurrency, credentials, rate limits, or novel inputs.

### Local-real

A real dependency type running in a controlled local environment, such as PostgreSQL, Redis, or a local browser. Configuration and scale still differ from external reality.

### External-real

The actual provider or production-like external system. Results remain bounded by account, region, time, dataset, network, and exercised path.

## Do not use silent fallback

If a live dependency is unavailable, do not silently switch to a fake and report success. Make the reality visible in command output and test naming.

## Contract and provider evidence

A fake can support application logic and failure-path tests. A conformance suite can compare implementations. Only external-real observation can directly support claims about the provider, and even then only within the tested conditions.

## Data and privacy

External-real tests may touch real accounts, costs, sensitive data, rate limits, or irreversible effects. Use dedicated environments, least privilege, explicit opt-in, cleanup, and operation identity.

## Mixed reality

A scenario may use real database + fake payment + replayed model output. Report each material dependency rather than labeling the entire run "integration".

## Related knowledge

- Use [Choosing an observation surface](choosing-observation-surface.md) to select the minimum reality.
- Use [Command and probe design](command-and-probe-design.md) to expose the reality in output.
- Use [Observation limits](observation-limits.md) for claim boundaries.
- Use `$evolvable-application-architecture` for Port semantics and provider boundaries.
- Return to the [Harness map](../SKILL.md).
