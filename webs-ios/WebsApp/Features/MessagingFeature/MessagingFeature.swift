import ComposableArchitecture
import SwiftUI

@Reducer
struct MessagingFeature {
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

struct MessagingView: View {
    let store: StoreOf<MessagingFeature>

    var body: some View {
        Text("Messaging")
    }
}
