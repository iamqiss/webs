#!/usr/bin/env python3
"""
scaffold_webs_ios.py
Scaffolds the webs-ios SwiftUI project file tree.
Run from the root of the webs monorepo:
    python3 scaffold_webs_ios.py
"""

import os

# ── Helpers ────────────────────────────────────────────────────────────────────

def write(path: str, content: str = "") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")

def touch(path: str) -> None:
    write(path, "")

# ── File contents ──────────────────────────────────────────────────────────────

PACKAGE_SWIFT = """\
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "WebsApp",
    platforms: [.iOS(.v17)],
    dependencies: [
        // gRPC
        .package(url: "https://github.com/grpc/grpc-swift.git", from: "1.21.0"),
        // TCA — The Composable Architecture
        .package(url: "https://github.com/pointfreeco/swift-composable-architecture.git", from: "1.10.0"),
        // Swift Protobuf
        .package(url: "https://github.com/apple/swift-protobuf.git", from: "1.26.0"),
    ],
    targets: [
        .target(
            name: "WebsApp",
            dependencies: [
                .product(name: "GRPC",                      package: "grpc-swift"),
                .product(name: "ComposableArchitecture",    package: "swift-composable-architecture"),
                .product(name: "SwiftProtobuf",             package: "swift-protobuf"),
            ]
        ),
        .testTarget(
            name: "WebsAppTests",
            dependencies: ["WebsApp"]
        ),
    ]
)
"""

APP_SWIFT = """\
import SwiftUI
import ComposableArchitecture

@main
struct WebsApp: App {
    var body: some Scene {
        WindowGroup {
            // TODO: inject store and route to RootView
            RootView()
        }
    }
}
"""

ROOT_VIEW = """\
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
"""

MAIN_TAB_VIEW = """\
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
"""

# ── Features ───────────────────────────────────────────────────────────────────

def feature_stub(name: str, description: str) -> str:
    return f"""\
import SwiftUI
import ComposableArchitecture

// {name} — {description}

// MARK: - Reducer

@Reducer
struct {name}Feature {{
    @ObservableState
    struct State: Equatable {{
        // TODO: state
    }}

    enum Action {{
        // TODO: actions
    }}

    var body: some ReducerOf<Self> {{
        Reduce {{ state, action in
            // TODO: logic
            return .none
        }}
    }}
}}

// MARK: - View

struct {name}View: View {{
    let store: StoreOf<{name}Feature>

    var body: some View {{
        // TODO: build view
        Text("{name}")
    }}
}}
"""

# ── Model stubs ────────────────────────────────────────────────────────────────

def model_stub(name: str) -> str:
    return f"""\
import Foundation

// {name} — local domain model
// Mirrors the proto-generated type but decoupled for SwiftData persistence
struct {name}: Identifiable, Equatable, Codable {{
    let id: String
    // TODO: fields
}}
"""

# ── SwiftData store stub ───────────────────────────────────────────────────────

def store_stub(name: str) -> str:
    return f"""\
import SwiftData
import Foundation

// {name}Store — SwiftData persistence for offline-first {name.lower()} data
@Model
final class {name}Store {{
    var id: String = ""
    // TODO: persisted fields mirroring {name} domain model
    init() {{}}
}}
"""

# ── gRPC client stub ───────────────────────────────────────────────────────────

def grpc_stub(name: str) -> str:
    return f"""\
import GRPC
import NIO

// {name}GRPCClient — wraps the generated proto client for {name.lower()}
// All calls go through this layer; swap for mock in tests
struct {name}GRPCClient {{
    // TODO: inject channel and initialise generated client
    // TODO: implement request/stream methods
}}
"""

# ── Repository stub ────────────────────────────────────────────────────────────

def repo_stub(name: str) -> str:
    return f"""\
import Foundation

// {name}Repository — single source of truth
// Reads from SwiftData cache, syncs from gRPC, writes back locally
struct {name}Repository {{
    // TODO: inject {name}GRPCClient + SwiftData context
    // TODO: implement fetch, stream, mutate methods
}}
"""

# ── View stub ──────────────────────────────────────────────────────────────────

def view_stub(name: str) -> str:
    return f"// TODO: {name}\n"

# ── Scaffold ───────────────────────────────────────────────────────────────────

def scaffold():
    base = "webs-ios"
    app  = f"{base}/WebsApp"
    print(f"\n🕸  Scaffolding {base}/\n")

    # Root
    write(f"{base}/Package.swift",  PACKAGE_SWIFT)
    touch(f"{base}/.gitignore")
    touch(f"{base}/README.md")

    # App entry
    write(f"{app}/WebsApp.swift",             APP_SWIFT)
    write(f"{app}/RootView.swift",            ROOT_VIEW)
    write(f"{app}/MainTabView.swift",         MAIN_TAB_VIEW)

    # ── Features ───────────────────────────────────────────────────────────────
    features = {
        "App":        "Root app reducer — session, routing, deep links",
        "Auth":       "Login, signup, token refresh flow",
        "Home":       "For You / Following / Trending feed",
        "Discover":   "Search, trending topics, follow suggestions",
        "Spins":      "Full-screen vertical video feed",
        "Post":       "Single Web (post) detail + comments",
        "CreatePost": "Compose a Web — text, images, category, Circle tag",
        "CreateSpin": "Record or upload a Spin",
        "Circles":    "My Circles feed + Explore tab",
        "CircleDetail":"Single Circle feed and about page",
        "Stories":    "Stories bar + full-screen story viewer",
        "Profile":    "Own and other user profiles — Webs + Spins tabs",
        "EditProfile":"Edit display name, bio, avatar, banner",
        "Messages":   "DM inbox list",
        "Conversation":"1:1 and group message thread",
        "Activity":   "Activity feed — replies, follows, reactions",
        "Settings":   "Account, privacy, notifications, theme",
    }

    for name, desc in features.items():
        path = f"{app}/Features/{name}/{name}Feature.swift"
        write(path, feature_stub(name, desc))

    # ── Models ─────────────────────────────────────────────────────────────────
    models = ["User", "Post", "Spin", "Circle", "Story",
              "Message", "Conversation", "ActivityItem", "SearchResult"]
    for m in models:
        write(f"{app}/Models/{m}.swift", model_stub(m))

    # ── SwiftData (offline cache) ──────────────────────────────────────────────
    stores = ["Post", "Spin", "Circle", "Story", "User", "ActivityItem"]
    for s in stores:
        write(f"{app}/LocalStore/{s}Store.swift", store_stub(s))

    # ── gRPC clients ───────────────────────────────────────────────────────────
    clients = ["Auth", "Feed", "Post", "Spins", "Profile",
               "Circles", "Stories", "Messages", "Activity", "Search"]
    for c in clients:
        write(f"{app}/GRPC/{c}GRPCClient.swift", grpc_stub(c))

    # gRPC channel / interceptor setup
    write(f"{app}/GRPC/GRPCChannel.swift",
          "// TODO: configure shared gRPC channel — TLS, keepalive, interceptors\n")
    write(f"{app}/GRPC/AuthInterceptor.swift",
          "// TODO: tonic interceptor that attaches Bearer JWT to every call\n")

    # ── Repositories ───────────────────────────────────────────────────────────
    repos = ["Auth", "Feed", "Post", "Spin", "Profile",
             "Circle", "Story", "Message", "Activity", "Search"]
    for r in repos:
        write(f"{app}/Repositories/{r}Repository.swift", repo_stub(r))

    # ── Shared UI components ───────────────────────────────────────────────────
    components = [
        "WebCard",          # single post card in feed
        "SpinPlayer",       # full-screen video player
        "AvatarView",       # user avatar with optional verified badge
        "StoryRing",        # story ring around avatar
        "StoriesBar",       # horizontal stories strip at top of home
        "CirclePill",       # small circle tag chip
        "FloatingNavBar",   # the custom floating bottom nav
        "ComposeButton",    # animated ＋ compose button
        "FollowButton",     # follow / unfollow toggle
        "ReactionBar",      # like, dislike, comment, reshare, bookmark row
        "UserRow",          # compact user row for lists
        "EmptyState",       # empty feed / search / activity state
        "LoadingSpinner",   # branded loading indicator
    ]
    for c in components:
        write(f"{app}/Components/{c}.swift", view_stub(c))

    # ── Screens (thin views that host Feature views) ───────────────────────────
    screens = [
        "SplashScreen",
        "OnboardingScreen",
        "LoginScreen",
        "SignUpScreen",
        "HomeScreen",
        "DiscoverScreen",
        "SpinsScreen",
        "PostDetailScreen",
        "CreatePostScreen",
        "CreateSpinScreen",
        "CirclesScreen",
        "CircleDetailScreen",
        "StoriesScreen",
        "ProfileScreen",
        "EditProfileScreen",
        "MessagesScreen",
        "ConversationScreen",
        "ActivityScreen",
        "SettingsScreen",
    ]
    for s in screens:
        write(f"{app}/Screens/{s}.swift", view_stub(s))

    # ── Theme ──────────────────────────────────────────────────────────────────
    write(f"{app}/Theme/Colors.swift",
          "// TODO: Webs color palette — semantic tokens mapped to light/dark\n")
    write(f"{app}/Theme/Typography.swift",
          "// TODO: Webs type scale — display, headline, body, caption\n")
    write(f"{app}/Theme/Spacing.swift",
          "// TODO: spacing constants — 4pt grid\n")
    write(f"{app}/Theme/Icons.swift",
          "// TODO: SF Symbols + custom icon references\n")
    write(f"{app}/Theme/Animations.swift",
          "// TODO: shared animation curves and durations\n")

    # ── Utilities ──────────────────────────────────────────────────────────────
    write(f"{app}/Utilities/Extensions.swift",
          "// TODO: View, String, Date extensions\n")
    write(f"{app}/Utilities/DateFormatter+Webs.swift",
          "// TODO: relative date formatting — '35m', '2h', 'Apr 10'\n")
    write(f"{app}/Utilities/ImageCache.swift",
          "// TODO: lightweight in-memory + disk image cache\n")
    write(f"{app}/Utilities/HapticEngine.swift",
          "// TODO: haptic feedback helpers\n")
    write(f"{app}/Utilities/NetworkMonitor.swift",
          "// TODO: NWPathMonitor wrapper — publishes online/offline state\n")
    write(f"{app}/Utilities/KeychainHelper.swift",
          "// TODO: secure storage for JWT + refresh token\n")
    write(f"{app}/Utilities/Logger+Webs.swift",
          "// TODO: os.Logger categories for each subsystem\n")

    # ── Generated proto stubs ──────────────────────────────────────────────────
    proto_files = ["auth", "feed", "post", "spins", "profile",
                   "circles", "stories", "messages", "activity", "search"]
    for p in proto_files:
        touch(f"{app}/Generated/{p}.grpc.swift")
        touch(f"{app}/Generated/{p}.pb.swift")

    write(f"{app}/Generated/README.md",
          "# Generated\nDo not edit. Run `buf generate` from the `proto/` directory to regenerate.\n")

    # ── Tests ──────────────────────────────────────────────────────────────────
    test_targets = ["Auth", "Feed", "Post", "Profile", "Activity", "Repositories"]
    for t in test_targets:
        write(f"{base}/WebsAppTests/{t}Tests.swift",
              f"// TODO: unit tests — {t}\n")

    print(f"\n✅  Done. Open webs-ios/ in Xcode and resolve packages.\n")

# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    scaffold()
