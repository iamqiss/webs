import SwiftUI
import ComposableArchitecture

// CircleDetail — Single Circle feed and about page

// MARK: - Reducer

@Reducer
struct CircleDetailFeature {
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

struct CircleDetailView: View {
    let store: StoreOf<CircleDetailFeature>

    var body: some View {
        // TODO: build view
        Text("CircleDetail")
    }
}
