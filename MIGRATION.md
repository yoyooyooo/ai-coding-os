# AI Coding OS 0.6 Migration

> Historical pre-convergence migration note. It does not describe the current content-only network of eight core Skills plus one supporting projection Skill, which no longer includes Preset, App Kit, Contracts, versioned migration, or release machinery.

`0.6.0-experimental.1` is a breaking Skill-topology cleanup. It ships no aliases
or per-Eval migration ledger.

| Previous name | Current route |
| --- | --- |
| `$interface-capability-planning` | `$product-definition` → Interface Capability Handoff |
| `$headless-product-harness` | `$product-harness-system` → headless branch |
| `$ui-product-harness` | `$product-harness-system` → UI/browser branch |
| `$frontend-test-system` | `$product-harness-system` → frontend-test branch |

Preset profile renames:

```text
headless-product-harness -> headless-proof
ui-product-harness       -> ui-proof
```

Preset and App Kit are now user-invoked tools. In Pi, invoke them explicitly as
`/skill:evolvable-application-preset` or `/skill:effect-api-app-kit` after the
user requests adoption/materialization and the semantic inputs are settled.

Consumers that persist old Skill or profile names must update those references.
Unchanged prompt examples and internal case IDs are not compatibility contracts.
