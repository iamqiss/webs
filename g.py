#!/usr/bin/env python3
"""
Webs iOS v3 Scaffold
Production-grade Apple-style architecture with TCA + DI + Asset pipeline.
"""

import os

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def write(path: str, content: str = ""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")


def touch(path: str):
    write(path, "")


BASE = "webs-ios/WebsApp"

def domain(name): return f"{BASE}/Domains/{name}"
def feature(name): return f"{BASE}/Features/{name}Feature"
def infra(path): return f"{BASE}/Infrastructure/{path}"
def ui(path): return f"{BASE}/UI/{path}"
def assets(path): return f"{BASE}/Assets/{path}"
def core(path): return f"{BASE}/Core/{path}"

# ─────────────────────────────────────────────
# Package.swift
# ─────────────────────────────────────────────

PACKAGE = """\
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "WebsApp",
    platforms: [.iOS(.v17)],
    dependencies: [
        .package(url: "https://github.com/pointfreeco/swift-composable-architecture.git", from: "1.10.0"),
        .package(url: "https://github.com/grpc/grpc-swift.git", from: "1.21.0"),
        .package(url: "https://github.com/apple/swift-protobuf.git", from: "1.26.0"),
    ],
    targets: [
        .target(
            name: "WebsApp",
            dependencies: [
                .product(name: "ComposableArchitecture", package: "swift-composable-architecture"),
                .product(name: "GRPC", package: "grpc-swift"),
                .product(name: "SwiftProtobuf", package: "swift-protobuf"),
            ]
        )
    ]
)
"""

# ─────────────────────────────────────────────
# APP LAYER (TCA ROOT)
# ─────────────────────────────────────────────

APP = """\
import SwiftUI
import ComposableArchitecture

@main
struct WebsApp: App {
    var body: some Scene {
        WindowGroup {
            AppView(
                store: Store(
                    initialState: AppReducer.State(),
                    reducer: { AppReducer() }
                )
            )
        }
    }
}
"""

APP_REDUCER = """\
import ComposableArchitecture

@Reducer
struct AppReducer {

    // ─────────────────────────────
    // STATE
    // ─────────────────────────────
    struct State: Equatable {
        var auth = AuthFeature.State()
        var isLoggedIn = false
    }

    // ─────────────────────────────
    // ACTION
    // ─────────────────────────────
    enum Action {
        case auth(AuthFeature.Action)
        case sessionUpdated(Bool)
    }

    // ─────────────────────────────
    // BODY
    // ─────────────────────────────
    var body: some ReducerOf<Self> {
        Scope(state: \\ .auth, action: \\ .auth) {
            AuthFeature()
        }

        Reduce { state, action in
            switch action {
            case .auth(.loginSuccess):
                state.isLoggedIn = true
                return .none

            default:
                return .none
            }
        }
    }
}
"""

APP_VIEW = """\
import SwiftUI
import ComposableArchitecture

struct AppView: View {
    let store: StoreOf<AppReducer>

    var body: some View {
        SwitchStore(store) { state in
            if state.isLoggedIn {
                MainTabView()
            } else {
                AuthFlowView(store: store.scope(state: \\ .auth, action: \\ .auth))
            }
        }
    }
}
"""

# ─────────────────────────────────────────────
# AUTH FLOW STATE MACHINE
# ─────────────────────────────────────────────

AUTH_FEATURE = """\
import ComposableArchitecture

@Reducer
struct AuthFeature {

    enum Phase: Equatable {
        case splash
        case onboarding
        case login
        case signup
        case passphrase
    }

    struct State: Equatable {
        var phase: Phase = .splash
    }

    enum Action {
        case start
        case nextPhase
        case loginSuccess
    }

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {

            case .start:
                state.phase = .onboarding
                return .none

            case .nextPhase:
                return .none

            case .loginSuccess:
                return .none
            }
        }
    }
}
"""

AUTH_FLOW_VIEW = """\
import SwiftUI
import ComposableArchitecture

struct AuthFlowView: View {
    let store: StoreOf<AuthFeature>

    var body: some View {
        SwitchStore(store) { state in
            switch state.phase {
            case .splash:
                SplashView()

            case .onboarding:
                OnboardingView()

            case .login:
                LoginView()

            case .signup:
                SignUpView()

            case .passphrase:
                PassphraseView()
            }
        }
    }
}
"""

# ─────────────────────────────────────────────
# DEPENDENCY INJECTION (CLEAN ARCHITECTURE CORE)
# ─────────────────────────────────────────────

DI_CONTAINER = """\
import Foundation

// Webs DI Container (replace with real environment in production)
struct AppContainer {
    let authService: AuthService
    let apiClient: APIClient
}

extension AppContainer {
    static let live = AppContainer(
        authService: AuthService(),
        apiClient: APIClient()
    )

    static let mock = AppContainer(
        authService: AuthService(),
        apiClient: APIClient()
    )
}
"""

# ─────────────────────────────────────────────
# INFRASTRUCTURE
# ─────────────────────────────────────────────

INFRA = {
    "GRPC/Client.swift": "struct GRPCClient {}",
    "Networking/APIClient.swift": "struct APIClient {}",
    "Persistence/SwiftDataStack.swift": "// SwiftData stack",
    "Repositories/AuthRepository.swift": "struct AuthRepository {}",
}

# ─────────────────────────────────────────────
# AUTH DOMAIN
# ─────────────────────────────────────────────

AUTH_DOMAIN = {
    "Models/UserSession.swift": "struct UserSession: Equatable { let id: String }",
    "Services/AuthService.swift": "struct AuthService {}",
    "RTC/EmoPatChallenge.swift": "struct EmoPatChallenge { static func generate() -> String { \"x\" } }",
    "Trust/TrustModels.swift": "struct TrustScore { let value: Double }",
    "Trust/TrustCollector.swift": "struct TrustCollector {}",
}

# ─────────────────────────────────────────────
# FEATURES (LIGHT ORCHESTRATION ONLY)
# ─────────────────────────────────────────────

FEATURES = [
    "Auth", "Feed", "Post", "Spins",
    "Profile", "Circles", "Messaging"
]

def feature_stub(name):
    return f"""\
import ComposableArchitecture
import SwiftUI

@Reducer
struct {name}Feature {{
    struct State: Equatable {{}}

    enum Action {{
        case onAppear
    }}

    var body: some ReducerOf<Self> {{
        Reduce {{ state, action in
            return .none
        }}
    }}
}}

struct {name}View: View {{
    let store: StoreOf<{name}Feature>

    var body: some View {{
        Text(\"{name}\")
    }}
}}
"""

# ─────────────────────────────────────────────
# ASSETS SYSTEM (IMPORTANT ADDITION)
# ─────────────────────────────────────────────

ASSETS_STRUCTURE = {
    "Icons/README.md": """\
Drop SVG icons here.

Recommended:
- home.svg
- discover.svg
- post.svg
- circle.svg
- profile.svg
""",

    "Images/README.md": """\
App images:
- splash.png (launch splash)
- app_logo.png (main logo)
- app_store_icon.png (1024x1024)
""",

    "Launch/SplashImages/README.md": """\
Splash assets:
- splash_light.png
- splash_dark.png
- splash_video.mp4 (optional animated intro)
""",

    "AppStore/README.md": """\
App Store assets:
- icon_1024.png (required)
- screenshots_iPhone_1.png
- screenshots_iPhone_2.png
"""
}

# ─────────────────────────────────────────────
# UI SYSTEM
# ─────────────────────────────────────────────

UI_COMPONENTS = [
    "WebCard", "SpinPlayer", "AvatarView",
    "FloatingNavBar", "ComposeButton"
]

# ─────────────────────────────────────────────
# SCHEMA GENERATOR
# ─────────────────────────────────────────────

def scaffold():
    print("\n🕸️ Webs iOS v3 (Production Architecture Scaffold)\n")

    # Root
    write("webs-ios/Package.swift", PACKAGE)
    write(f"{BASE}/WebsApp.swift", APP)
    write(f"{BASE}/AppReducer.swift", APP_REDUCER)
    write(f"{BASE}/AppView.swift", APP_VIEW)

    # Auth flow
    write(f"{BASE}/Features/AuthFeature/AuthFeature.swift", AUTH_FEATURE)
    write(f"{BASE}/Features/AuthFeature/AuthFlowView.swift", AUTH_FLOW_VIEW)

    # DI container
    write(f"{BASE}/Core/DIContainer.swift", DI_CONTAINER)

    # Infrastructure
    for path, content in INFRA.items():
        write(f"{BASE}/Infrastructure/{path}", content)

    # Auth domain
    for path, content in AUTH_DOMAIN.items():
        write(f"{BASE}/Domains/Auth/{path}", content)

    # Features
    for f in FEATURES:
        write(f"{BASE}/Features/{f}Feature/{f}Feature.swift", feature_stub(f))

    # UI
    for c in UI_COMPONENTS:
        write(f"{BASE}/UI/Components/{c}.swift", f"// {c}")

    # Assets system (NEW IMPORTANT PART)
    for path, content in ASSETS_STRUCTURE.items():
        write(f"{BASE}/Assets/{path}", content)

    print("\n✅ Webs iOS v3 scaffold complete (Apple-scale + production architecture)\n")


if __name__ == "__main__":
    scaffold()
