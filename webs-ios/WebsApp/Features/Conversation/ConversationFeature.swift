import SwiftUI
import ComposableArchitecture

// Conversation — 1:1 and group message thread

// MARK: - Reducer

@Reducer
struct ConversationFeature {
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

struct ConversationView: View {
    let store: StoreOf<ConversationFeature>

    var body: some View {
        // TODO: build view
        Text("Conversation")
    }
}
