# Verification Policy

## Command Routes

| Role | Project command | Notes |
| --- | --- | --- |
| Install | `<command>` | non-interactive, lockfile-respecting |
| Format/lint | `<command>` | |
| Static/type check | `<command>` | |
| Unit/integration tests | `<command>` | |
| Architecture/boundary check | `<command or absent>` | |
| Affected verification | `<command>` | explain graph/selection basis |
| Full verification | `<command>` | does not imply product or external-provider proof |

## Dependency Reality Vocabulary

```text
fixture        static example data
fake           executable substitute with simplified behavior
replay         recorded behavior or events
local-real     real dependency in a controlled local environment
external-real  actual external provider or production-like service
```

## Claim Boundary

For each material verification surface, state:

```text
what property it observes
which dependency realities it uses
which environment and input path it exercises
what conclusion it supports
what remains not proven
```

## Stable Failure Interface

Commands should be non-interactive, return meaningful exit codes, preserve the first useful error, and provide enough context to reproduce or narrow failure.

## Destructive Operations

A destructive or externally visible command should expose inspection or dry-run when practical, require explicit apply, and state recovery or irreversibility.
