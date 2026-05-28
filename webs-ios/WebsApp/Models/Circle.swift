import Foundation

// Circle — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Circle: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
