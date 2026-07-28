# HttpApi Integration

Use Effect HttpApi or an equivalent Effect-native HTTP surface when typed contracts, errors, middleware, and runtime composition materially improve the backend boundary.

## Boundary roles

```text
HTTP contract      transport shape, status, headers, path/query/body schema
handler            decode/map/call use case/map outcome
use case            product authorization, policy, fact transition
Port/Service        external capability contract
host composition    live Layers, server, resources, shutdown
```

The HTTP contract does not own product meaning merely because it is typed.

## Decode at the boundary

Validate all untrusted transport input. Convert to application Command or query types. Keep framework request/response objects out of the application core.

## Error mapping

Map application outcomes to HTTP deliberately:

```text
validation rejection -> 4xx with stable detail
not authorized        -> 401/403 according to actual semantics
conflict/stale version -> 409 or project contract
not found             -> 404 when existence disclosure is allowed
pending/unknown       -> explicit accepted/pending contract, not generic 500
internal defect       -> bounded server error with diagnostic Cause retained
```

## Middleware and context

Authentication, trace context, rate limit, and request metadata may enter through middleware. Convert them to an explicit application context rather than exposing framework locals deep in use cases.

## Runtime ownership

The HTTP host owns the live server, Runtime/Layer graph, database pool, clients, and shutdown. Handlers use the prepared environment; they do not construct live Layers.

## Version grounding

HttpApi APIs have changed across Effect versions. Confirm the local package version, declarations, and official docs before copying examples.

## Related knowledge

- Use [Version grounding](version-grounding.md) for concrete APIs.
- Use [Service, Layer, and Runtime](service-layer-runtime.md) for host construction.
- Use `$evolvable-application-architecture` for use cases, Ports, and fact authority.
- Use `$product-harness-system` for HTTP integration and real dependency observation.
- Return to the [Effect map](../SKILL.md).
