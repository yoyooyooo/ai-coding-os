import { Context, Effect, Layer, ManagedRuntime } from "effect";

export type ChannelProjection = {
  readonly channelId: string;
  readonly title: string;
  readonly messages: ReadonlyArray<{
    readonly id: string;
    readonly body: string;
  }>;
};

export type SendMessageInput = {
  readonly channelId: string;
  readonly body: string;
  readonly clientMutationId: string;
};

export type SendMessageResult = {
  readonly messageId: string;
  readonly clientMutationId: string;
};

export class ChannelError extends Error {
  readonly _tag = "ChannelError";

  constructor(readonly cause: unknown) {
    super("Channel capability failed");
  }
}

export type ChannelTransport = {
  readonly fetchProjection: (channelId: string) => Promise<unknown>;
  readonly sendMessage: (input: SendMessageInput) => Promise<unknown>;
};

export type ChannelClient = {
  readonly fetchProjection: (channelId: string) => Promise<ChannelProjection>;
  readonly sendMessage: (input: SendMessageInput) => Promise<SendMessageResult>;
};

export type ProductClient = {
  readonly channel: ChannelClient;
  readonly close: () => Promise<void>;
};

export class ChannelGateway extends Context.Service<
  ChannelGateway,
  {
    readonly fetchProjection: (
      channelId: string
    ) => Effect.Effect<ChannelProjection, ChannelError>;
    readonly sendMessage: (
      input: SendMessageInput
    ) => Effect.Effect<SendMessageResult, ChannelError>;
  }
>()("ChannelGateway") {}

const decodeProjection = (value: unknown): ChannelProjection => value as ChannelProjection;
const decodeSendResult = (value: unknown): SendMessageResult => value as SendMessageResult;

export const makeChannelGatewayLive = (transport: ChannelTransport) =>
  Layer.succeed(ChannelGateway)({
    fetchProjection: (channelId) =>
      Effect.tryPromise({
        try: () => transport.fetchProjection(channelId),
        catch: (cause) => new ChannelError(cause)
      }).pipe(Effect.map(decodeProjection)),
    sendMessage: (input) =>
      Effect.tryPromise({
        try: () => transport.sendMessage(input),
        catch: (cause) => new ChannelError(cause)
      }).pipe(Effect.map(decodeSendResult))
  });

const fetchChannelProjectionEffect = (channelId: string) =>
  Effect.gen(function* () {
    const gateway = yield* ChannelGateway;
    return yield* gateway.fetchProjection(channelId);
  });

const sendChannelMessageEffect = (input: SendMessageInput) =>
  Effect.gen(function* () {
    const gateway = yield* ChannelGateway;
    return yield* gateway.sendMessage(input);
  });

export function createLiveProductClient(transport: ChannelTransport): ProductClient {
  const runtime = ManagedRuntime.make(makeChannelGatewayLive(transport));

  return {
    channel: {
      fetchProjection: (channelId) =>
        runtime.runPromise(fetchChannelProjectionEffect(channelId)),
      sendMessage: (input) => runtime.runPromise(sendChannelMessageEffect(input))
    },
    close: () => runtime.dispose()
  };
}

export function createFakeProductClient(projection: ChannelProjection): ProductClient {
  return {
    channel: {
      fetchProjection: async () => projection,
      sendMessage: async (input) => ({
        messageId: "fake-message",
        clientMutationId: input.clientMutationId
      })
    },
    close: async () => {}
  };
}
