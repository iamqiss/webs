import SwiftData
import Foundation

// StoryStore — SwiftData persistence for offline-first story data
@Model
final class StoryStore {
    var id: String = ""
    // TODO: persisted fields mirroring Story domain model
    init() {}
}
