# Workflow Specification Template

```markdown
---
doc_type: workflow-specification
status: <repository-defined status>
workflow_id:
owner:
version_horizon:
primary_object:
source_inputs: []
decisions: []
---

# <Workflow ID>: <Workflow Name>

## 1. Business purpose and outcome

## 2. Trigger and completion

- Trigger:
- Preconditions:
- Successful outcome:
- Cancellation / termination outcome:

## 3. Actors and systems

| Actor / system | Responsibility in this workflow | Handoff authority |
| --- | --- | --- |

## 4. Happy path

| Step | Actor / system | Action or event | Object / state before | Rule / decision | Object / state after | Side effects | Observable evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Alternate paths

### ALT-01: <Name>

- Entry condition:
- Steps:
- Outcome:

## 6. Exception and recovery paths

| Exception ID | Trigger / failure | User-visible behavior | Recovery / retry | Ownership | State result | Escalation |
| --- | --- | --- | --- | --- | --- | --- |

## 7. Termination, cancellation, withdrawal, and reopen

## 8. Handoffs and time constraints

| Handoff | Sender | Receiver | Artifact / object | Acknowledgement | Due / calendar | Rejection / no-response behavior | Escalation |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 9. Concurrency, duplicate action, and stale-data behavior

## 10. Permissions and visibility by step

## 11. Generated objects, files, notifications, metrics, and logs

## 12. Migration or legacy behavior

## 13. Acceptance hooks

## 14. Open decisions
```
