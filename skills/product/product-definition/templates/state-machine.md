# State Machine Template

```markdown
---
doc_type: state-machine
status: <repository-defined status>
object:
owner:
version_horizon:
source_inputs: []
decisions: []
---

# <Object> Lifecycle

## 1. Object definition and lifecycle boundary

## 2. State list

| State | Meaning | Entry condition | Allowed actions | Exit condition | Terminal? | Reversible? | Visibility / editability consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3. Transition table

| Transition ID | From | Action / event | Actor / system | Preconditions | To | Side effects | Guards | Logs / notifications | Failure behavior |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 4. Separate state dimensions not modeled here

- Approval state:
- Task / assignment state:
- Time / SLA state:
- Visibility / publication state:
- Archive / retention state:
- Integration / sync state:
- Display-only state:

## 5. Derived states

## 6. Invalid transitions

| From | Attempted action | Why invalid | Expected user/system result |
| --- | --- | --- | --- |

## 7. Reopen, rollback, and compensating actions

## 8. Concurrency and stale-state behavior

## 9. Migration from legacy states

## 10. Acceptance coverage

## 11. Open decisions
```
