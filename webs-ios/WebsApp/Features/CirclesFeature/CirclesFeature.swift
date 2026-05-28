import ComposableArchitecture
import SwiftUI

@Reducer
struct CirclesFeature {
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

struct CirclesView: View {
    let store: StoreOf<CirclesFeature>

    var body: some View {
        Text("Circles")
    }
}
