import Foundation

// Spin — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Spin: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
