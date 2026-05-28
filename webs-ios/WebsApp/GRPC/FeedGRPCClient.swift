import GRPC
import NIO

// FeedGRPCClient — wraps the generated proto client for feed
// All calls go through this layer; swap for mock in tests
struct FeedGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
