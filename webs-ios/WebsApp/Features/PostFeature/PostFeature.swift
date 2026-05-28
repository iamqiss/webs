import ComposableArchitecture
import SwiftUI

@Reducer
struct PostFeature {
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

struct PostView: View {
    let store: StoreOf<PostFeature>

    var body: some View {
        Text("Post")
    }
}
