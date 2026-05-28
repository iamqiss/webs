import Foundation

// Story — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct Story: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
