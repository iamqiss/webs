import SwiftUI
import ComposableArchitecture

// EditProfile — Edit display name, bio, avatar, banner

// MARK: - Reducer

@Reducer
struct EditProfileFeature {
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

struct EditProfileView: View {
    let store: StoreOf<EditProfileFeature>

    var body: some View {
        // TODO: build view
        Text("EditProfile")
    }
}
