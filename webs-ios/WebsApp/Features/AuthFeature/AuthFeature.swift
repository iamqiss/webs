import ComposableArchitecture
import SwiftUI

@Reducer
struct AuthFeature {
    struct State: Equatable {}

    enum Action {
        case onAppear
    }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            return .none
        }
    }
}

struct AuthView: View {
    let store: StoreOf<AuthFeature>

    var body: some View {
        Text("Auth")
    }
}
