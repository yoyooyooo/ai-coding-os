# Repository Agent Entry

`AGENTS.md` is the default stable repository entry for Agents when the project needs durable local instructions. It is a map of project-specific constraints and commands, not a second product or architecture authority.

## Default role

A thin repository entry may contain:

```text
project authority routes
resolved commands and verification slots
stable local constraints
language policy
restricted, sensitive, generated, or vendored paths
intentional deviations from portable defaults
important host or workspace entry points
```

It should link to `docs/README.md` when durable project documentation exists.

## Must not become

```text
a full product SSoT
a complete architecture description
a copy of every Standard
a task queue or execution status page
a full Skill catalog
a private tool configuration dump
```

Move durable detail to the owning surface and leave a route.

## Three independent discovery surfaces

```text
Skill map        which portable owner can help with the concern
Repository entry project-local commands, constraints, and routes
Docs router      links among durable project knowledge Homes
```

They may link to one another but do not form a mandatory traversal sequence.

## Local and nested entries

A nested `AGENTS.md` is justified when a subtree has real local differences in:

```text
commands or toolchain
language or runtime
security or generated paths
public/private dependency rules
host lifecycle
testing or build behavior
```

A nested entry should state only the delta and link upward. Do not copy the root entry into every package.

## Command resolution

Use actual runnable commands rather than abstract advice. Resolve package-manager and workspace details locally:

```text
Install: <actual command>
Type/static check: <actual command>
Affected verification: <actual command>
Full verification: <actual command>
Architecture/boundary check: <actual command if present>
```

The command roles are defined by `$product-harness-system`; this file owns only the project mapping.

## Language policy

The portable Skill package is English. Project narrative language is decided by the project. Keep canonical paths, commands, symbols, protocol names, and machine fields stable even when narrative prose uses another language.

## Project override

A repository may use another host-recognized entry file. Preserve it when Agents can discover it reliably and it carries the same role. Avoid parallel entry files with conflicting instructions.

## Template

Use the [minimal AGENTS.md template](../templates/AGENTS.md) selectively.

## Related knowledge

- Use `$product-harness-system` and its Default project verification interface for command slots.
- Use [Multi-entry discovery](multi-entry-discovery.md) for routes from source and errors.
- Use [Default documentation topology](default-documentation-topology.md) for `docs/README.md` and homes.
- Return to the [Docs Governance map](../SKILL.md).
