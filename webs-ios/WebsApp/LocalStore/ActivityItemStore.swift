import SwiftData
import Foundation

// ActivityItemStore — SwiftData persistence for offline-first activityitem data
@Model
final class ActivityItemStore {
    var id: String = ""
    // TODO: persisted fields mirroring ActivityItem domain model
    init() {}
}
