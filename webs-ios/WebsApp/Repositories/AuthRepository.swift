import Foundation

// AuthRepository — single source of truth
// Reads from SwiftData cache, syncs from gRPC, writes back locally
struct AuthRepository {
    // TODO: inject AuthGRPCClient + SwiftData context
    // TODO: implement fetch, stream, mutate methods
}
