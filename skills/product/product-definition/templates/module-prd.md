# Module PRD Template

Use only sections that materially improve the specification. Use the repository's lifecycle vocabulary.

```markdown
---
doc_type: module-prd
status: <repository-defined status>
module:
owner:
business_owner:
version_horizon:
effective_version:
source_inputs: []
decisions: []
related_model: []
related_workflows: []
related_rules: []
related_metrics: []
---

# <Module / Capability> PRD

## 1. Background, problem, and outcome

### Current situation

### Product goal

### Success condition

### Non-goals

## 2. Scope

### In scope

### Out of scope

### Future candidates

### Current behavior retained or retired

## 3. Users, roles, and scenarios

| Actor | Goal | Scenario | Responsibility | Permission summary |
| --- | --- | --- | --- | --- |

## 4. Business objects and relationships

## 5. End-to-end workflow

### Happy path

### Alternate paths

### Exception, recovery, and termination paths

## 6. State machine and transition rules

| Transition ID | Current state | Action / event | Actor | Preconditions | Target state | Side effects | Reversible? | Failure behavior |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 7. Product requirements

| Requirement ID | Actor / trigger | Required product behavior | Conditions / scope | Observable result | Related rule / state / metric |
| --- | --- | --- | --- | --- | --- |

## 8. Fields and validation

| Field | Business meaning | Type / unit | Required when | Editable when | Visible to | Default / source | Validation / cross-field rule | Sensitivity / retention |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 9. Business rules and calculations

## 10. Permissions and data visibility

## 11. Notifications and system side effects

| Trigger | Recipient / target | Channel / artifact | Content requirement | Timing | Failure behavior | Retry / resend | Log requirement |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Files, generated artifacts, versions, logs, and retention

## 13. Interaction states for design

- Normal:
- Empty:
- Loading / processing:
- Validation failure:
- System failure:
- Partial success:
- Read-only / locked:
- No permission:
- Expired / stale:
- Concurrent update / conflict:

## 14. Metrics and reporting definitions

## 15. Product quality attributes

## 16. Acceptance criteria

## 17. UAT scenarios

## 18. Dependencies, assumptions, and open decisions

## 19. Traceability

## 20. Change log
```
