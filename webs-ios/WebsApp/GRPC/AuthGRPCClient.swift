import GRPC
import NIO

// AuthGRPCClient — wraps the generated proto client for auth
// All calls go through this layer; swap for mock in tests
struct AuthGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
