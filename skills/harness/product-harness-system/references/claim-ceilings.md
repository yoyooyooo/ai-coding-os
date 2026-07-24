# Harness Claim Ceilings

A harness supports conclusions only up to the surface it exercised. A claim
ceiling describes evidence capability; it does not force an Agent through a
fixed ladder.

## Common surfaces

```text
headless
  policy, use case, adapter, materialization, persistence, replay, runtime

interface-headless
  client/query/store/realtime/router/view-model behavior without full render

render
  component wiring and visible states in a render environment

browser
  bounded user-visible path, navigation/reload/focus/network/console observations

external-runtime
  explicitly opted-in real provider/device/runtime behavior
```

Additional qualifiers may be written plainly:

```text
headless + replay + postgres + restart + fake provider
browser + real local backend + fake payment provider
```

Do not require a full multidimensional schema unless project tooling needs one.

## Reporting

A useful result states:

```text
surface exercised
observed facts
supported bounded conclusions
not_proven adjacent properties
real/fake/replay environment distinctions
```

Examples:

```text
headless reducer test
  does not prove browser reachability

browser with mocked backend
  does not prove backend fact materialization

local production-near stack
  does not prove production auth, public deployment, or real-provider exactly-once
```
