import Foundation

// Conversation — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Conversation: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
