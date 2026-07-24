# Agent Entry and Preset Adoption

## AGENTS.md purpose

`AGENTS.md` is the tool-neutral operational entry for Agents. It tells an Agent
what to read, which current commands exist, which language policy applies, and
where project authority lives. It is not the location for the full architecture
or Skill Suite.

Recommended maximum responsibility:

```text
project/Preset adoption statement
repository-local authority precedence
Read First links
small stable working rules
resolved commands
language policy
thin Skill routing pointer
local exceptions/restricted paths
```

## Ownership

```text
$docs-governance
  owns generic placement, thinness, lifecycle, conflict, and nested-entry rules

$evolvable-application-preset
  owns the architecture-specific template/managed section and merge logic

project
  owns the merged final file and current command/path values

$ai-coding-os
  consumes the entry and routes knowledge; it does not write project authority
```

## New repository

Create only the minimum useful entry and docs router. Do not fabricate authority
maps or module facts that do not exist. Use explicit placeholders such as
`not-yet-established` where required.

## Existing repository

```text
inspect existing AGENTS.md and host-specific instruction files
-> identify canonical tool-neutral entry
-> classify the requested surface as adopt / merge / keep-project / skip / conflict
-> preserve project-specific instructions
-> add or update only the compatible managed Preset section
-> link host-specific files back to canonical entry when useful
-> audit the changed surface
```

Do not overwrite an existing entry wholesale or require full Preset adoption.

## Preset adoption

Depending on the discovered slice, the Preset may contribute:

```text
AGENTS.md managed section
docs/standards/architecture-profile.yaml
docs/standards/source-topology-and-naming.md
docs/standards/naming-vocabulary.yaml
docs/ssot/product-language.md
docs/ssot/authority-map.md
docs/architecture/repository-topology.md
docs/adr/<adoption>.md
```

Templates and candidates are not current project authority. After selective adoption, project files are
a resolved snapshot. Record:

```yaml
schema_version: 1
preset:
  id: evolvable-application
  version: <version>
  mode: resolved-snapshot
profiles:
  - <resolved-profile>
```

## Upgrade

An upgrade stages or displays a semantic diff only for candidate-managed
surfaces. Preserve local extensions and deviations; unrelated project files are
never candidate deletions. Do not make a project dynamically inherit the latest
installed Preset.

## Nested AGENTS.md admission

Create a nested entry only when local differences are durable:

```text
different commands
host-specific lifecycle
security or write restrictions
framework-reserved paths
distinct verification surface
```

Nested files link to root and describe deltas. They do not repeat global Skill
routing, language policy, or full standards.
