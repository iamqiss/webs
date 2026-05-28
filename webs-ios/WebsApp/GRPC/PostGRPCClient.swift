import GRPC
import NIO

// PostGRPCClient — wraps the generated proto client for post
// All calls go through this layer; swap for mock in tests
struct PostGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
