import Foundation

// MessageRepository — single source of truth
// Reads from SwiftData cache, syncs from gRPC, writes back locally
struct MessageRepository {
    // TODO: inject MessageGRPCClient + SwiftData context
    // TODO: implement fetch, stream, mutate methods
}
