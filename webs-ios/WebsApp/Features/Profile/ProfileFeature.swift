import SwiftUI
import ComposableArchitecture

// Profile — Own and other user profiles — Webs + Spins tabs

// MARK: - Reducer

@Reducer
struct ProfileFeature {
    @ObservableState
    struct State: Equatable {
        // TODO: state
    }

    enum Action {
        // TODO: actions
    }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            // TODO: logic
            return .none
        }
    }
}

// MARK: - View

struct ProfileView: View {
    let store: StoreOf<ProfileFeature>

    var body: some View {
        // TODO: build view
        Text("Profile")
    }
}
