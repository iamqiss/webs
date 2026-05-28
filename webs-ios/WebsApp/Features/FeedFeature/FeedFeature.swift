import ComposableArchitecture
import SwiftUI

@Reducer
struct FeedFeature {
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

struct FeedView: View {
    let store: StoreOf<FeedFeature>

    var body: some View {
        Text("Feed")
    }
}
