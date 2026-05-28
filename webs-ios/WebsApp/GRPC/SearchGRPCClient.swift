import GRPC
import NIO

// SearchGRPCClient — wraps the generated proto client for search
// All calls go through this layer; swap for mock in tests
struct SearchGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
