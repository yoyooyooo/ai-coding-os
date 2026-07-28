# Repository Topology

## Current shape

```text
<repository / workspace / apps / packages / crates / hosts>
```

## Boundary map

| Boundary | Role | Public surface | Owner / lifetime | Does not imply |
| --- | --- | --- | --- | --- |
| `<module/package/host/deployable>` | `<role>` | `<surface>` | `<owner>` | `<fact authority, trust, deployment, etc.>` |

## Dependency direction

```text
<allowed direction>
<forbidden deep or reverse imports>
```

## Runtime and deployment relationships

- Runnable hosts: `<hosts>`
- Independent deployables: `<deployables>`
- Datastores and writer scopes: `<mapping>`
- Generated or vendored boundaries: `<mapping>`

## Accepted future differences

Keep future targets visibly separate from current structure. Link the accepted decision or roadmap condition rather than editing the current diagram into the future.
