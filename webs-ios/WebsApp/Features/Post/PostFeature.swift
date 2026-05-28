import SwiftUI
import ComposableArchitecture

// Post — Single Web (post) detail + comments

// MARK: - Reducer

@Reducer
struct PostFeature {
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

struct PostView: View {
    let store: StoreOf<PostFeature>

    var body: some View {
        // TODO: build view
        Text("Post")
    }
}
