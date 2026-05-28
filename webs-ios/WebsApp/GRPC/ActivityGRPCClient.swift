import GRPC
import NIO

// ActivityGRPCClient — wraps the generated proto client for activity
// All calls go through this layer; swap for mock in tests
struct ActivityGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
