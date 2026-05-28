import SwiftUI

// MainTabView — floating nav bar with 5 tabs
// [ Home ] [ Discover ] [ Spins ] [ Circles ] [ Profile ]
// Compose (＋) button floats above, animates on scroll
struct MainTabView: View {
    @State private var selectedTab: Tab = .home

    enum Tab {
        case home, discover, spins, circles, profile
    }

    var body: some View {
        // TODO: implement floating nav bar + tab routing
        TabView(selection: $selectedTab) {
            Text("Home")      .tag(Tab.home)
            Text("Discover")  .tag(Tab.discover)
            Text("Spins")     .tag(Tab.spins)
            Text("Circles")   .tag(Tab.circles)
            Text("Profile")   .tag(Tab.profile)
        }
    }
}
