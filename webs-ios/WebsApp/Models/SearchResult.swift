import Foundation

// SearchResult — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct SearchResult: Identifiable, Equatable, Codable {
    let id: String
    // TODO: fields
}
