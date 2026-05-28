import SwiftUI
import ComposableArchitecture

// Spins — Full-screen vertical video feed

// MARK: - Reducer

@Reducer
struct SpinsFeature {
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

struct SpinsView: View {
    let store: StoreOf<SpinsFeature>

    var body: some View {
        // TODO: build view
        Text("Spins")
    }
}
