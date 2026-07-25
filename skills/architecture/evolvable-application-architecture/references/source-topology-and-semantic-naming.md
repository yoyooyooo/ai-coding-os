# Source Topology and Semantic Naming

The generic architecture owns semantic roles and boundary strength, not one
language's filenames.

## Promotion Ladder

```text
local lexical grouping
  -> private semantic module
  -> enforceable compilation/public-API boundary
  -> independently runnable host
  -> independently deployed/trust/fault boundary
```

Promote when ownership, dependency direction, public compatibility, resource
lifecycle, compilation, trust, fault isolation, release, or deployment pressure
becomes durable. File count and symmetry are review signals, not admission rules.

## Naming Contract

Names should reveal:

```text
product subject
operation or facet
semantic responsibility
implementation/provider/host qualifier when necessary
```

Avoid generic buckets such as `service`, `manager`, `common`, `core`, `utils`,
and `types` when a governed responsibility can be named.

## Ecosystem Projections

```text
TypeScript
  semantic dot filenames, private directory/module, package export, app entry
  are available conventions; see the TypeScript projection and Preset profile

Rust
  module tree, restricted visibility, facade/re-export, crate, and binary are
  the normal boundary surfaces; do not imitate TypeScript dot filenames

Other ecosystems
  use their idiomatic module/public API/build/deployable constructs while
  preserving the same authority and dependency decisions
```

A filename, directory, package, or crate never grants fact Authority by itself.
Machine-readable filename patterns apply only when a selected ecosystem profile
owns them.
