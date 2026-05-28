import Foundation

// ProfileRepository — single source of truth
// Reads from SwiftData cache, syncs from gRPC, writes back locally
struct ProfileRepository {
    // TODO: inject ProfileGRPCClient + SwiftData context
    // TODO: implement fetch, stream, mutate methods
}
