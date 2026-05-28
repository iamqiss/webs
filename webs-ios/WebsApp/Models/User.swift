import Foundation

// User — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct User: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
