import ComposableArchitecture
import SwiftUI

@Reducer
struct ProfileFeature {
    struct State: Equatable {}

    enum Action {
        case onAppear
    }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            return .none
        }
    }
}

struct ProfileView: View {
    let store: StoreOf<ProfileFeature>

    var body: some View {
        Text("Profile")
    }
}
