import SwiftUI
import ComposableArchitecture

// Auth — Login, signup, token refresh flow

// MARK: - Reducer

@Reducer
struct AuthFeature {
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

struct AuthView: View {
    let store: StoreOf<AuthFeature>

    var body: some View {
        // TODO: build view
        Text("Auth")
    }
}
