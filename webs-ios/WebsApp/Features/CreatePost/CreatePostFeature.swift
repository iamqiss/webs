import SwiftUI
import ComposableArchitecture

// CreatePost — Compose a Web — text, images, category, Circle tag

// MARK: - Reducer

@Reducer
struct CreatePostFeature {
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

struct CreatePostView: View {
    let store: StoreOf<CreatePostFeature>

    var body: some View {
        // TODO: build view
        Text("CreatePost")
    }
}
