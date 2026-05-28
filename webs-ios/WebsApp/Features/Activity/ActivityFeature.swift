import SwiftUI
import ComposableArchitecture

// Activity — Activity feed — replies, follows, reactions

// MARK: - Reducer

@Reducer
struct ActivityFeature {
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

struct ActivityView: View {
    let store: StoreOf<ActivityFeature>

    var body: some View {
        // TODO: build view
        Text("Activity")
    }
}
