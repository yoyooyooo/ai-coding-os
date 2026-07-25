# Harness Trace Contract

Trace helps future Agents answer:

```text
Which Product AC/UAT or capability is this Harness for?
Which formal entry does it drive?
Which property can it observe?
Which Proof Surface did it use?
Which stronger or adjacent claims remain unproven?
```

## Minimal trace

```yaml
capability: order.checkout
product_refs:
  - AC-071
scenario: order.checkout.retry
proof_surface:
  surface_kind: headless
  dependency_reality:
    - fake
    - real_local
  environment_class: local_stack
  proof_focus:
    - idempotent_retry
entry: order.submit.use-case
command: pnpm verify order.checkout.retry
```

User-facing capabilities may additionally link an InterfaceCapability and a UI
route or surface.

## Coverage

A coverage matrix is optional. Use it when several capabilities and observation
surfaces must remain discoverable across time:

```yaml
- capability: order.checkout
  headless: accepted
  interface_headless: accepted
  render: candidate
  browser: candidate
  external_runtime: gap
```

Coverage status describes surface availability or lifecycle, not a passing
result. Dependency reality and environment belong to the Descriptor/Result.
`planned` or `candidate` means a route exists, not that behavior is proven.

## Method independence

A tracker, spec, CI report, release process, or other selected execution method
may reference Harness IDs. The Harness contract remains independent of that
method. When a real machine consumer or durable repeated handoff needs a shared
shape, use the direction-neutral `$ai-coding-os-suite-contracts` Evidence
Envelope; otherwise reference the Harness Result directly. Never add
workflow-specific fields to every Harness descriptor.
