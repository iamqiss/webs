package app.webs.android.feature.auth

import androidx.compose.runtime.*
import androidx.hilt.navigation.compose.hiltViewModel

@Composable
fun AuthScreen(
    viewModel: AuthViewModel = hiltViewModel(),
    onAuthenticated: () -> Unit
) {

    val state = viewModel.state.collectAsState()

    when (state.value) {

        AuthState.Splash -> SplashScreen()
        AuthState.Onboarding -> OnboardingScreen()
        AuthState.Login -> LoginScreen()
        AuthState.Signup -> SignUpScreen()
        AuthState.Passphrase -> PassphraseScreen(
            onAuthenticated = onAuthenticated
        )
    }
}
