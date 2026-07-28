# Default Architecture Knowledge Shape

Use these project-owned paths when architecture meaning is durable and the repository has no coherent adopted alternative. Create only the files that answer recurring questions.

## Required router when the Home exists

```text
docs/architecture/README.md
```

The router describes the current architecture scope and links to the few surfaces that explain it. It is not a second architecture specification.

## Reserved default filenames

| Path | Use when |
| --- | --- |
| `docs/architecture/fact-authority-map.md` | readers need to find accepted fact writers, consistency scopes, candidate/observation paths, and forbidden legacy writers |
| `docs/architecture/repository-topology.md` | module, package, host, deployable, datastore, and public-boundary relationships are not obvious from the tree alone |
| `docs/architecture/<host>-runtime.md` | a host has non-trivial composition, resources, background work, shutdown, or external-effect recovery |
| `docs/architecture/integration-boundaries.md` | several external capabilities, protocols, trust boundaries, or provider substitutions need one current route |

The exact content may remain in `README.md` while the project is small. Split only when direct linking, update cadence, or ownership pressure earns it.

## Fact authority map content

Prefer a compact table or diagram that answers:

```text
fact or consistency scope
final materialization authority
governed use case or command entry
other proposal/observation sources
transaction or concurrency boundary
forbidden or legacy writers
migration/fencing condition when applicable
```

A package, database table, or service name does not become the authority merely because it appears in the map.

## Repository topology content

Describe relationships that the file tree cannot safely imply:

```text
repository/workspace
packages or crates and public surfaces
runnable hosts and resource owners
deployables and failure/trust boundaries
datastores and writer scopes
source-generated or vendored boundaries
```

Keep current structure separate from accepted future targets.

## Runtime content

For a non-trivial host, make discoverable:

```text
entry command
configuration decoding
live capability selection
resource construction and lifetime
background task supervision
shutdown and cancellation
health/diagnostic surfaces
unknown-outcome and restart recovery
```

## Templates

- [Fact authority map](../templates/fact-authority-map.md)
- [Repository topology](../templates/repository-topology.md)
- [Host runtime](../templates/host-runtime.md)

## Project override

Preserve a coherent local name such as `system/`, `runtime/`, or `technical-design/`. Map it once in `docs/README.md` or `docs/architecture/README.md`; do not create a duplicate portable tree.

## Related knowledge

- Use [Agent-legible change surface](agent-legible-change-surface.md) to decide what a fresh Agent must recover.
- Use [Fact authority and candidate boundaries](fact-authority-and-candidate-boundaries.md) for writer semantics.
- Use [Default repository profile](default-repository-profile.md) for source projection.
- Use `$docs-governance` for Home admission, naming, and freshness.
- Return to the [EAA map](../SKILL.md).
