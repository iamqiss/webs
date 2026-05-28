import Foundation

// Message — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Message: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
