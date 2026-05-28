import GRPC
import NIO

// SpinsGRPCClient — wraps the generated proto client for spins
// All calls go through this layer; swap for mock in tests
struct SpinsGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
