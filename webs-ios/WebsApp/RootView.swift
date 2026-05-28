import SwiftUI
import ComposableArchitecture

// RootView — decides between AuthView and MainTabView
// based on session state in AppReducer
struct RootView: View {
    var body: some View {
        // TODO: observe AppReducer session state
        MainTabView()
    }
}
