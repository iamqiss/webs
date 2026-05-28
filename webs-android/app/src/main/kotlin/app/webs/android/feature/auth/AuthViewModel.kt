package app.webs.android.feature.auth

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class AuthViewModel : ViewModel() {

    private val _state =
        MutableStateFlow<AuthState>(AuthState.Splash)

    val state: StateFlow<AuthState> = _state

    fun next() {
        _state.value = when (_state.value) {
            AuthState.Splash -> AuthState.Onboarding
            AuthState.Onboarding -> AuthState.Login
            AuthState.Login -> AuthState.Passphrase
            AuthState.Passphrase -> AuthState.Passphrase
            AuthState.Signup -> AuthState.Login
        }
    }
}
