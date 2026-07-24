# AI Coding OS Skill Coordination

## Shared Doctrine

```text
$ai-coding-os selects the relevant knowledge.
Specialist skills own distinct decision surfaces.
Presets and generators instantiate settled decisions.
Project AGENTS.md and docs/** own resolved repository authority.
The active agent or selected execution method decides how work proceeds.
```

## Authority Resolution

Authority is claim-scoped; there is no universal total order that makes source
code override every document or every document override executable reality.
Resolve the claim in this order:

```text
1. host instructions and repository AGENTS.md
2. adopted project authority for the claim:
   current facts        -> docs/ssot/**
   executable rules     -> docs/standards/**
   accepted tradeoffs   -> docs/adr/**
   wire compatibility   -> project protocol/schema contract
3. executable reality for implementation claims:
   source, lockfiles, tests, and command evidence
4. unadopted Preset source or candidate, then specialist doctrine
5. router recommendation
```

An adopted Preset output is no longer a separate Preset authority: it is a
project-owned file resolved through its docs layer. If project authority and
executable reality disagree, surface stale or broken authority explicitly;
do not silently choose one. `$ai-coding-os-suite-contracts` is a portable
contract source, not project authority.

## Collaboration Rules

1. Select the lead by the highest semantic authority affected, not file count.
2. Add a supporting skill only for a decision surface the lead does not own.
3. Express handoffs with `$skill-name` and an artifact or decision contract.
4. Keep shared engineering doctrine self-contained; a skill remains usable when
   adjacent skills are unavailable.
5. Let project authority override Suite defaults and record intentional
   deviations in the project.
6. Keep planning strategy, retry policy, model selection, and completion control
   with the active execution context rather than a doctrine skill.

## Handoff Shape

```text
from: $skill-name
owned_decision: <what is settled>
artifact_or_contract: <project artifact, schema ID, or concise object; never a sibling Skill path>
open_surface: <what remains undecided>
to: $skill-name
claim_boundary: <what the handoff does and does not establish>
```

The routing map itself has one operational owner: `$ai-coding-os`.
Cross-Skill continuation uses `$skill-name`; a static roster or grouped
repository path is never part of the handoff contract.
