import SwiftUI
import ComposableArchitecture

struct AppView: View {
    let store: StoreOf<AppReducer>

    var body: some View {
        SwitchStore(store) { state in
            if state.isLoggedIn {
                MainTabView()
            } else {
                AuthFlowView(store: store.scope(state: \ .auth, action: \ .auth))
            }
        }
    }
}
