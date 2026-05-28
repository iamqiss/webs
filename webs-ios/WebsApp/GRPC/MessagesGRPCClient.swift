import GRPC
import NIO

// MessagesGRPCClient — wraps the generated proto client for messages
// All calls go through this layer; swap for mock in tests
struct MessagesGRPCClient {
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}
