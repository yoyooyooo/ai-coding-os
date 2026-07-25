# Business Rule Catalog Template

```markdown
---
doc_type: business-rule-catalog
status: <repository-defined status>
owner:
version_horizon:
source_inputs: []
decisions: []
---

# Business Rule Catalog: <Product / Domain>

## 1. Rule precedence

Describe which policy, version, market, object state, or specific rule wins when several rules apply.

## 2. Rule catalog

| Rule ID | Family | Plain-language statement | Trigger / scope | Inputs | Output / effect | Exceptions | Precedence | Owner | Source / decision | Effective version | Acceptance reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rule families:

`eligibility | validation | invariant | calculation | classification | routing | time | numbering | side-effect | retention`

## 3. Enumeration catalog

| Enum / value | Business label | Definition | Selection / derivation rule | Active status | Legacy mapping | Workflow / metric impact | Localization notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 4. Calculations and rounding

| Calculation ID | Formula | Population / inputs | Units | Rounding | Time / currency basis | Exceptions | Metric / field affected |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Date, calendar, and timezone rules

## 6. Numbering and identity rules

## 7. Notification and generated-object rules

## 8. Retention, deletion, and version rules

## 9. Conflicts and open decisions

## 10. Change log
```
