import SwiftUI
import ComposableArchitecture

// Settings — Account, privacy, notifications, theme

// MARK: - Reducer

@Reducer
struct SettingsFeature {
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

struct SettingsView: View {
    let store: StoreOf<SettingsFeature>

    var body: some View {
        // TODO: build view
        Text("Settings")
    }
}
