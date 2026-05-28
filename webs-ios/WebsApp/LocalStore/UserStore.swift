import SwiftData
import Foundation

// UserStore — SwiftData persistence for offline-first user data
@Model
final class UserStore {
    var id: String = ""
    // TODO: persisted fields mirroring User domain model
    init() {}
}
