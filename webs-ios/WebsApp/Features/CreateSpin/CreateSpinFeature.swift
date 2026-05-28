import SwiftUI
import ComposableArchitecture

// CreateSpin — Record or upload a Spin

// MARK: - Reducer

@Reducer
struct CreateSpinFeature {
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

struct CreateSpinView: View {
    let store: StoreOf<CreateSpinFeature>

    var body: some View {
        // TODO: build view
        Text("CreateSpin")
    }
}
