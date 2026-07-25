# Suite Contract Snapshot

This directory is the immutable-at-render-time copy consumed by the Preset.
The canonical sources live in `$ai-coding-os-suite-contracts`; the Preset does
not resolve sibling Skill paths at runtime. Suite audit verifies byte parity.

The filename patterns are explicitly TypeScript/TSX projections. Generic
`application-core`, `monorepo-core`, and `rust` profiles do not select them.
