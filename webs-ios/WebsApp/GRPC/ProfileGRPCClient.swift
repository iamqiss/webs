import GRPC
import NIO

// ProfileGRPCClient — wraps the generated proto client for profile
// All calls go through this layer; swap for mock in tests
struct ProfileGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
