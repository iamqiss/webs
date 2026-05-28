import Foundation

// ActivityItem — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct ActivityItem: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
