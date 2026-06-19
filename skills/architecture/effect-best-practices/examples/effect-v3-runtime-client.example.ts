import { Context, Effect, Layer, ManagedRuntime } from "effect-v3";

export type Projection = {
  readonly id: string;
  readonly title: string;
};

export class ClientError extends Error {
  readonly _tag = "ClientError";
  constructor(readonly cause: unknown) {
    super("Client capability failed");
  }
}

export type Transport = {
  readonly fetchProjection: (id: string) => Promise<unknown>;
};

export class ProjectionGateway extends Context.Tag("ProjectionGateway")<
  ProjectionGateway,
  {
    readonly fetch: (
      id: string
    ) => Effect.Effect<Projection, ClientError>;
  }
>() {}

const decodeProjection = (value: unknown): Projection => value as Projection;

const makeProjectionGatewayLive = (transport: Transport) =>
  Layer.succeed(ProjectionGateway, {
    fetch: (id) =>
      Effect.tryPromise({
        try: () => transport.fetchProjection(id),
        catch: (cause) => new ClientError(cause)
      }).pipe(Effect.map(decodeProjection))
  });

const fetchProjection = (id: string) =>
  Effect.gen(function* () {
    const gateway = yield* ProjectionGateway;
    return yield* gateway.fetch(id);
  });

export function createV3Client(transport: Transport) {
  const runtime = ManagedRuntime.make(makeProjectionGatewayLive(transport));
  return {
    fetchProjection: (id: string) => runtime.runPromise(fetchProjection(id)),
    close: () => runtime.dispose()
  };
}
