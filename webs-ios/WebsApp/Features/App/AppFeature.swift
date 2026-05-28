import SwiftUI
import ComposableArchitecture

// App — Root app reducer — session, routing, deep links

// MARK: - Reducer

@Reducer
struct AppFeature {
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

struct AppView: View {
    let store: StoreOf<AppFeature>

    var body: some View {
        // TODO: build view
        Text("App")
    }
}
