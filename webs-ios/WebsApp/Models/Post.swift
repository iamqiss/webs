import Foundation

// Post — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Post: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
