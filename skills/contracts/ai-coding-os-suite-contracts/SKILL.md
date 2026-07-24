---
name: ai-coding-os-suite-contracts
description: >-
  Canonical shared contracts for the AI Coding OS Skill Suite. Use when an
  AI Coding OS skill needs cross-skill precedence and handoff shape, shared
  architecture vocabulary and filename patterns, guarded terms,
  or Harness Descriptor/Result schemas. Do not use for project-specific
  contracts, routing decisions, or implementation work.
---

# AI Coding OS Suite Contracts

Provide the portable contracts shared by the AI Coding OS Skill Suite:

> **The Skill name identifies the suite; local references carry the contract;
> project authority still wins.**

This Skill is an independently installable support surface. It must remain
usable when all Skill directories are flattened into one runtime collection.

## Ownership

```text
Owns:
  cross-Skill precedence and handoff shape
  portable registry of owner-declared architecture vocabulary and filename defaults
  guarded naming terms
  portable Harness Descriptor / Result vocabulary and schemas

Does not own:
  routing branches or lead selection
  specialist semantics named by each registry entry
  project-specific vocabulary or architecture decisions
  product truth or implementation state
  execution strategy or completion control
```

Use `$ai-coding-os` for routing, the owning specialist for a domain decision,
and project AGENTS/docs for adopted repository authority.

## Contract Use Pass

| Step | Completion criterion |
| --- | --- |
| Select | The requesting Skill, project authority, and only the needed coordination, naming, or Harness contract are identified. |
| Apply | Contract vocabulary is interpreted through its declared owner; project overrides and unresolved limits stay explicit. |
| Hand off | Continuation names `$skill-name` and a bounded project artifact or decision contract, never a sibling filesystem path. |

## Read When Needed

| Need | Local reference |
| --- | --- |
| Precedence and handoff shape | [Skill Coordination](references/skill-coordination.md) |
| Architecture responsibility vocabulary | [Semantic Vocabulary](references/semantic-vocabulary.yaml) |
| Bounded Semantic Flatness patterns | [Filename Patterns](references/filename-patterns.yaml) |
| Ambiguous naming terms requiring clarification | [Guarded Terms](references/guarded-terms.yaml) |
| Harness vocabulary and schemas | [Harness Contracts](references/harness/README.md) |

## Portability Contract

- Relative links stay inside this Skill directory.
- Cross-Skill relationships use `$skill-name`.
- Grouped repository paths are source-maintenance details, not runtime
  dependencies.
- Consumers may install this Skill beside hundreds of unrelated Skills without
  losing its AI Coding OS ownership from the name.

## Output

Return only the requested contract material, its owning `$skill-name`, any
project override, and the unresolved boundary. Do not emit a complete Suite
inventory unless the user explicitly asks for discovery.
