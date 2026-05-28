import SwiftUI
import ComposableArchitecture

// Stories — Stories bar + full-screen story viewer

// MARK: - Reducer

@Reducer
struct StoriesFeature {
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

struct StoriesView: View {
    let store: StoreOf<StoriesFeature>

    var body: some View {
        // TODO: build view
        Text("Stories")
    }
}
