import SwiftUI
import ComposableArchitecture

// Messages — DM inbox list

// MARK: - Reducer

@Reducer
struct MessagesFeature {
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

struct MessagesView: View {
    let store: StoreOf<MessagesFeature>

    var body: some View {
        // TODO: build view
        Text("Messages")
    }
}
