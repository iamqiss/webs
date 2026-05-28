package app.webs.android.feature.auth

sealed class AuthState {
    data object Splash : AuthState()
    data object Onboarding : AuthState()
    data object Login : AuthState()
    data object Signup : AuthState()
    data object Passphrase : AuthState()
}
