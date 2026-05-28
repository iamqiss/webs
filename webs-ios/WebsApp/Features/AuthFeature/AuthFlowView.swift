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
