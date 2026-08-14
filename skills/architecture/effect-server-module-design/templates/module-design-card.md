# Effect Server Module Design Card

Use only the sections that can change the module shape. Keep unresolved authority explicit rather than filling it with assumptions.

## Current pressure

- requested change:
- why the current shape makes that change expensive, unsafe, or hard to discover:
- exact source/evidence inspected:

## Authority

- owning capability/module:
- accepted facts:
- final writer:
- governed use cases:
- forbidden or obsolete writers/surfaces:

## Consumers and admission

- current internal consumers:
- real cross-module/Host consumers:
- test/adoption consumers:
- `*.public.ts` earned: `yes | no | unresolved`
- package pressure: `none | candidate | accepted elsewhere`

## Boundary verdict

- current: `owner-private | module-public | host-bridge | package-candidate | mixed`
- target: `owner-private | module-public | host-bridge | package-candidate | mixed`
- decision gaps that can change the target:

## Effect v4 projection

- exact installed version evidence:
- execution shape: `plain TypeScript | Effect program`
- canonical capability contract: `none | ordinary Port | Effect Service`
- expected failure algebra:
- timeout/interruption/unknown-outcome semantics:
- Fake pressure:
- Live placement:
- Layer selection owner:
- resource/Scope owner:
- Host config/transport/credential/pool dependencies:

## Target tree

```text
<smallest concrete source tree>
```

For each proposed file, state the independent pressure that earns it.

## Delta

| Action                            | Current path | Target path | Reason |
| --------------------------------- | ------------ | ----------- | ------ |
| keep/move/rename/merge/remove/add |              |             |        |

## Import rules

| Importer                           | May import | Must not import |
| ---------------------------------- | ---------- | --------------- |
| module-private implementation      |            |                 |
| external module/Host               |            |                 |
| implementation-local test          |            |                 |
| contract/adoption/integration test |            |                 |

## Proof delta

- focused unit/contract tests:
- adoption/composition/integration tests:
- mechanical boundary check:
- project commands:
- dependency reality:
- strongest bounded conclusion:
- `not_proven`:
