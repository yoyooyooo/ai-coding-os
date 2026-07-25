# Design Handoff Template

This template supplies product-complete input to design without prescribing the final interaction or visual solution.

```markdown
---
doc_type: design-handoff
status: <repository-defined status>
owner:
design_owner:
module_or_workflow:
version_horizon:
related_prd: []
product_requirement_refs: []
product_rule_refs: []
acceptance_criteria_refs: []
related_workflows: []
open_decisions: []
---

# Design Handoff: <Capability / Workflow>

This artifact defines accepted product obligations for design and interface planning. It does not choose IA, layout, components, frontend state owners, or proof tooling. A downstream InterfaceCapability references the Product Requirement, Rule, and AC IDs above rather than restating their semantics.

## 1. User goals and scenarios

## 2. Product flow

## 3. Page, surface, or interaction inventory

| Surface | User goal | Entry points | Primary actions | Object / state | Permission constraints |
| --- | --- | --- | --- | --- | --- |

## 4. State-complete interaction requirements

| State | Trigger | Required information | Allowed actions | Product consequence | Recovery / next step |
| --- | --- | --- | --- | --- | --- |

Include relevant normal, empty, loading, validation, failure, partial-success, read-only, no-permission, expired, stale, and conflict states.

## 5. Content and data requirements

## 6. Validation, warnings, confirmations, and destructive actions

## 7. Permissions, masking, and sensitive-data behavior

## 8. Files, notifications, generated artifacts, and logs

## 9. Accessibility, localization, device, and quality constraints

## 10. Design freedoms and product constraints

### Binding product constraints

### Areas intentionally left to design

## 11. Acceptance criteria relevant to design

## 12. InterfaceCapability handoff boundary

- Accepted product obligations and source IDs:
- Product states and exceptions the interface must represent:
- Product permissions and visibility obligations:
- Acceptance expectations needing proof:
- IA, surface, region, interaction-state ownership, and proof mapping left downstream:

## 13. Open decisions and handoff questions
```
