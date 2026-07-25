# Acceptance Criteria Template

## Behavior format

```markdown
### AC-<module>-<number>: <Title>

**Covers:** @REQ-<id>, @RULE-<id>, @PDR-<id> <!-- include only applicable references -->

Given <precondition>
And <additional context>
When <actor action or system event>
Then <observable product result>
And <state, data, permission, notification, file, log, or metric consequence>
```

## Optional criteria table

| AC ID | Requirement / rule / state | Given | When | Then | Negative / boundary case | Evidence method | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Checklist

```text
Can business, QA, or an agreed proof method observe the result?
Does it name the relevant actor, state, scope, and condition?
Does it include permission or data-visibility consequences when relevant?
Does it include side effects such as notifications, logs, files, metrics, or generated objects?
Does it define partial failure or recovery when that matters?
Does it cover a meaningful boundary or invalid action where risk justifies it?
Does it avoid implementation-only detail unless the detail is a binding product constraint?
Is it linked to a requirement, rule, state, metric, or decision when traceability is needed?
```
