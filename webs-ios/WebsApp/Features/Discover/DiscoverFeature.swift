import SwiftUI
import ComposableArchitecture

// Discover — Search, trending topics, follow suggestions

// MARK: - Reducer

@Reducer
struct DiscoverFeature {
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

struct DiscoverView: View {
    let store: StoreOf<DiscoverFeature>

    var body: some View {
        // TODO: build view
        Text("Discover")
    }
}
