---
name: ai-coding-os-suite-contracts
description: >-
  AI Coding OS portable knowledge kernel and shared machine contracts for
  Proof Surface and the optional claim-bounded Evidence Envelope, eval assets,
  architecture vocabulary, filename patterns, guarded terms, and Harness
  schemas. Use when a Suite Skill
  needs one portable contract or must identify
  its semantic owner; project-specific decisions stay with project authority
  and the owning specialist.
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
  the minimal cross-Skill knowledge kernel and optional handoff guidance
  portable catalog of owner-declared architecture/source vocabulary and filename defaults
  guarded naming terms
  portable Proof Surface, Harness Descriptor / Result, Evidence Envelope, and eval schemas

Hands off:
  routing branches and lead selection -> `$ai-coding-os`
  specialist semantics -> the owner named by each contract entry
  project vocabulary and architecture decisions -> project authority
  product truth and implementation state -> their project owners
  execution strategy and completion control -> the selected execution method
```

Project `AGENTS.md` constrains Agent conduct; applicable project Product, SSoT,
Standards, ADRs, contracts, source, and Evidence answer their own questions.

## Contract Coverage

Cover the applicable rows in any order; this is not a reasoning or execution sequence.

| Decision | Completion criterion |
| --- | --- |
| Selection | The requesting Skill, project authority, and only the needed coordination, naming, or Harness contract are identified. |
| Application | Contract vocabulary is interpreted through its declared owner; project overrides and unresolved limits stay explicit. |
| Handoff | Continuation names `$skill-name` and a bounded project artifact or decision contract, never a sibling filesystem path. |

## Read When Needed

| Need | Local reference |
| --- | --- |
| Minimal knowledge kernel and optional handoff guidance | [Skill Coordination](references/skill-coordination.md) |
| Owner-declared architecture/source vocabulary | [Semantic Vocabulary](references/semantic-vocabulary.yaml) |
| Bounded Semantic Flatness patterns | [Filename Patterns](references/filename-patterns.yaml) |
| Ambiguous naming terms requiring clarification | [Guarded Terms](references/guarded-terms.yaml) |
| Proof axes and Harness schemas | [Harness Contracts](references/harness/README.md) |
| Cross-owner evidence handoff under real reuse pressure | [Evidence Envelope](references/evidence/evidence-envelope.md) |
| Eval asset shape | [Skill Eval Contract](references/evals/README.md) |
| v1-to-v2 compatibility | [Suite Contracts v2 Migration](references/migrations/v2-proof-evidence.md) |

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
