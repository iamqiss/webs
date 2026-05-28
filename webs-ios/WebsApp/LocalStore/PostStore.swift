import SwiftData
import Foundation

// PostStore — SwiftData persistence for offline-first post data
@Model
final class PostStore {
    var id: String = ""
    // TODO: persisted fields mirroring Post domain model
    init() {}
}
