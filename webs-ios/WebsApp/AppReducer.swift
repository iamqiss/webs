import ComposableArchitecture

@Reducer
struct AppReducer {

    // ─────────────────────────────
    // STATE
    // ─────────────────────────────
    struct State: Equatable {
        var auth = AuthFeature.State()
        var isLoggedIn = false
    }

    // ─────────────────────────────
    // ACTION
    // ─────────────────────────────
    enum Action {
        case auth(AuthFeature.Action)
        case sessionUpdated(Bool)
    }

    // ─────────────────────────────
    // BODY
    // ─────────────────────────────
    var body: some ReducerOf<Self> {
        Scope(state: \ .auth, action: \ .auth) {
            AuthFeature()
        }

        Reduce { state, action in
            switch action {
            case .auth(.loginSuccess):
                state.isLoggedIn = true
                return .none

            default:
                return .none
            }
        }
    }
}
