# Harness Trace Contract

Trace exists to help future Agents answer:

```text
Which product capability is this Harness for?
Which formal entry does it drive?
Which state or output can it observe?
Which environment/fake/replay does it use?
Which stronger surfaces remain unproven?
```

## Minimal trace

```yaml
capability: order.checkout
scenario: order.checkout.retry
surface: headless
entry: order.submit.use-case
command: pnpm verify order.checkout.retry
```

User-facing capabilities may additionally link an InterfaceCapability and a UI
route/surface.

## Coverage

A coverage matrix is optional. Use it when several capabilities and surfaces
must remain discoverable across time:

```yaml
- capability: order.checkout
  headless: accepted
  interface_headless: accepted
  browser: candidate
  external_runtime: gap
```

`planned` or `candidate` means a route exists, not that behavior is proven.

## Method independence

A tracker, spec, CI report, or explicitly adopted Goal Pack may reference Harness
IDs. The Harness contract remains independent of that method. Do not make Goal
Pack fields part of every Harness descriptor.
