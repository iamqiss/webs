import SwiftUI
import ComposableArchitecture

// Home — For You / Following / Trending feed

// MARK: - Reducer

@Reducer
struct HomeFeature {
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

struct HomeView: View {
    let store: StoreOf<HomeFeature>

    var body: some View {
        // TODO: build view
        Text("Home")
    }
}
