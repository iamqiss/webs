import ComposableArchitecture
import SwiftUI

@Reducer
struct SpinsFeature {
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

struct SpinsView: View {
    let store: StoreOf<SpinsFeature>

    var body: some View {
        Text("Spins")
    }
}
