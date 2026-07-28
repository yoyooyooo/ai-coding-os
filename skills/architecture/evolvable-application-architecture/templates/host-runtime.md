# <Host> Runtime

## Entry and purpose

- Entry command: `<command>`
- Product/operational responsibility: `<responsibility>`

## Composition

- Configuration decoding: `<location>`
- Live capabilities and providers: `<mapping>`
- Runtime/resource construction: `<location>`

## Owned lifetimes

| Resource or child work | Owner | Lifetime | Stop / finalization |
| --- | --- | --- | --- |
| `<resource>` | `<owner>` | `<request/tab/process/etc.>` | `<path>` |

## Failure and recovery

- Expected failures: `<semantics>`
- Interruption/cancellation: `<semantics>`
- Timeout and unknown external outcome: `<semantics>`
- Restart/replay/reconciliation: `<path>`

## Observability and verification

- Health/diagnostic surface: `<route>`
- Smallest reproduction command: `<command>`
- Strongest supported claim: `<claim>`
- Not proven: `<limits>`
