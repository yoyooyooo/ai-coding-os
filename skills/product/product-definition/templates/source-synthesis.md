# Source Synthesis Template

Use when product truth must be built from several documents, stakeholder inputs, prototypes, analytics, current behavior, or code snapshots.

```markdown
---
doc_type: source-synthesis
status: <repository-defined status>
owner:
product_question:
version_horizon:
---

# Source Synthesis: <Product Question>

## 1. Source register

| Source ID | Name / location | Kind | Owner / authority | Version / date | Effective scope | Validity | Confidence | Sensitivity | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 2. Claim register

| Claim ID | Source ID | Atomic claim | Claim kind | Horizon | Confidence | Product impact | Conflict group | Decision needed | Recommended treatment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Claim kinds:

`scope | actor | object | workflow | state | rule | permission | metric | quality | roadmap | implementation | observed-behavior`

Use `implementation` for static implementation facts such as a source path,
module, route declaration, schema, migration, or database table that exists.
Reserve `observed-behavior` for behavior supported by bounded execution or
observation; source presence alone does not qualify.

Recommended treatment:

`promote-after-confirmation | current-fact-only | problem-evidence | decision-packet | out-of-scope | future-candidate | supersede | verify | retire`

## 3. Conflict groups

### <Conflict group ID>: <Topic>

- Claims involved:
- Neutral conflict statement:
- Affected version / users / objects / workflow:
- Recommendation:
- Decision owner:
- Needed by:
- Follow-up artifacts:

## 4. Unsupported assumptions

| Assumption ID | Assumption | Why needed | Owner | Expiry / decision point | Safe fallback | Status |
| --- | --- | --- | --- | --- | --- | --- |

## 5. Promotion summary

| Product artifact | Claims promoted | Decisions required | Status |
| --- | --- | --- | --- |
```
