# RACI and Permission Matrix Template

RACI clarifies accountability. Permission requirements clarify what the product allows. Keep them related but separate.

```markdown
---
doc_type: responsibility-permission-matrix
status: <repository-defined status>
owner:
version_horizon:
source_inputs: []
decisions: []
---

# Responsibility and Permission Model: <Product / Domain>

## 1. Actor definitions

| Actor / role | Business definition | Responsibility | Decision authority | Assignment behavior | Delegation / recusal | Data-scope basis |
| --- | --- | --- | --- | --- | --- | --- |

## 2. RACI matrix

| Activity / outcome | Actor A | Actor B | Actor C | Notes |
| --- | --- | --- | --- | --- |

Values: `R = Responsible | A = Accountable | C = Consulted | I = Informed`

## 3. Permission matrix

| Permission ID | Object / field / artifact | Operation | Actor / role | Data scope | Required relationship | Allowed states | Sensitivity rule | Delegation / recusal | Result when denied | Source / decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Operations may include:

`view | create | edit | submit | approve | reject | assign | transfer | cancel | reopen | publish | export | download | delete | administer`

## 4. Field-level visibility or masking

| Object / field | Visible to | Editable by | Masking / redaction | Export / notification rule | Retention consequence |
| --- | --- | --- | --- | --- | --- |

## 5. Separation-of-duty and conflict constraints

## 6. Access lifecycle

- When access begins:
- When access ends:
- Effect of reassignment or role removal:
- Administrator override rule:
- Temporary or external access:

## 7. Channel consistency

Confirm the same product boundary applies to UI, direct URL, API, export, file download, notification, and background action.

## 8. Open decisions and acceptance coverage
```
