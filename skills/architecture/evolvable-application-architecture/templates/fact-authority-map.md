# Fact Authority Map

> Keep this scoped. One row may represent a fact family or consistency domain, not every database column.

| Fact / scope | Final materialization authority | Governed entry | Proposal / observation sources | Transaction / concurrency boundary | Forbidden or legacy writers |
| --- | --- | --- | --- | --- | --- |
| `<fact>` | `<owner>` | `<command/use case>` | `<UI draft, import, provider, event, model output>` | `<boundary>` | `<writers>` |

## Important semantics

- A proposal, provider result, realtime frame, or model output is not accepted fact by itself.
- Shared storage or a shared package does not grant writer authority.
- Unknown external outcome requires operation identity and reconciliation before retry.

## Current exceptions or movement

- `<temporary bridge, fencing rule, divergence observation, and deletion condition>`
