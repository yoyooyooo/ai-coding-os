# Agent Entry and Preset Adoption

## Three Discovery Surfaces

```text
Skill Router       -> which specialist knowledge owns the current concern
Repository Entry   -> stable project constraints, commands, and available routes
Docs Router        -> links among project documentation Authorities
```

These surfaces may point to one another but form no required traversal order.
`AGENTS.md` owns only the Repository Entry role. A Skill Router never becomes
project Authority; a Docs Router never becomes a second copy of current truth.

## Repository Entry

A thin `AGENTS.md` or host-equivalent may contain:

```text
project adoption statement
repository-local Authority links
available discovery surfaces
small stable working rules
resolved commands
language policy
local restrictions and exceptions
```

It is not the Home for Product, SSoT, Standards, Architecture, contracts,
execution state, full Skill registries, or private tool configuration.

A useful project-level statement is:

```text
Project authorities and evidence surfaces are indexed by docs/README.md when it
exists. Agents may enter from the current question, code area, artifact, or
owner and follow only relevant Authority, Evidence, and source links.
```

This advertises the knowledge network without prescribing a reading workflow.

## Ownership

```text
$docs-governance
  entry thinness, placement, lifecycle, route integrity, nested-entry admission

$evolvable-application-preset or another specialist
  one explicitly declared managed section and its merge/render logic

project
  final AGENTS.md, current paths, commands, and constraints; semantic Authority remains in its question-scoped Home

$ai-coding-os
  knowledge-owner selection for ambiguous or cross-cutting intent
```

The project owns the final file. No generator replaces the whole entry.

## Multi-entry Discovery

An Agent may begin from any relevant surface:

```text
current question
source or package path
canonical term
product or architecture artifact
ADR, schema, test, Harness result, report
repository entry or docs router
```

Resolve only the neighborhood needed for the claim. A source change may reach
Architecture, SSoT, Product, contracts, or Evidence directly; a docs cleanup may
begin at the conflicting files. Missing optional layers and entries are normal.

Portable Skill output paths are defaults. Existing project Authority wins, and
an equivalent current Home prevents creation of a parallel artifact.

## Existing Repository

Classify each proposed Preset surface independently:

```text
adopt | merge | keep-project | skip | conflict
```

Inspect current files and Authority, preserve project-specific instructions,
and update only compatible managed content. The classification set is coverage,
not a required project workflow.

## Managed Sections

A managed section is safe only when:

- one stable begin marker and one stable end marker exist;
- replacement is confined to bytes between the markers;
- repeated rendering is idempotent;
- drift is visible as a diff before adoption;
- removing the section leaves surrounding human content intact;
- content outside the section is preserved.

Malformed or repeated markers are a conflict and block automated replacement.

## Preset Adoption

A Preset contributes a `candidate-snapshot` or one proposed managed section. It
does not create dynamic inheritance or self-assert adoption. Only content merged
by the applicable project owner becomes current Authority; the Preset remains a
reusable source. Legacy resolved snapshots remain readable during migration.

Generated entries expose applicable knowledge surfaces without requiring every
Product, SSoT, Standards, Architecture, ADR, Roadmap, or proof layer. A missing
optional entry is a review signal only when a declared route depends on it.

## Nested AGENTS.md

Create a nested entry only for a durable local delta such as different commands,
host lifecycle, security/write restrictions, framework-reserved paths, or a
distinct verification surface. It links to repository Authority and describes
only the local delta.

Classify topology from workspace declarations, manifests, commands, and actual
ownership rather than directory names alone:

```text
single-project
workspace-monorepo
aggregate-root
nested-independent-project
unknown
```
