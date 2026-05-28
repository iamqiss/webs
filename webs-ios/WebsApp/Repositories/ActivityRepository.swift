import Foundation

// ActivityRepository — single source of truth
// Reads from SwiftData cache, syncs from gRPC, writes back locally
struct ActivityRepository {
    // TODO: inject ActivityGRPCClient + SwiftData context
    // TODO: implement fetch, stream, mutate methods
}
