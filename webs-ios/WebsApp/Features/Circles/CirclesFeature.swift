import SwiftUI
import ComposableArchitecture

// Circles — My Circles feed + Explore tab

// MARK: - Reducer

@Reducer
struct CirclesFeature {
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

struct CirclesView: View {
    let store: StoreOf<CirclesFeature>

    var body: some View {
        // TODO: build view
        Text("Circles")
    }
}
