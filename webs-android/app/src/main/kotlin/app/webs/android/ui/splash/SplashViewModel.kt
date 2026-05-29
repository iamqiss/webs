package app.webs.android.ui.splash

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class SplashViewModel @Inject constructor(
    // TODO: Inject AuthRepository or SessionManager here later
) : ViewModel() {

    private val _uiState = MutableStateFlow<SplashUiState>(SplashUiState.Loading)
    val uiState: StateFlow<SplashUiState> = _uiState.asStateFlow()

    init {
        checkAuthStatus()
    }

    private fun checkAuthStatus() {
        viewModelScope.launch {
            // Simulate network / local storage check delay
            delay(1400)

            // TODO: Replace with real logic
            // val isLoggedIn = authRepository.isUserLoggedIn()
            val isLoggedIn = false   // Change this to test logged-in flow

            _uiState.value = if (isLoggedIn) {
                SplashUiState.Authenticated
            } else {
                SplashUiState.Unauthenticated
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// UI State
// ─────────────────────────────────────────────────────────────────────────────

sealed class SplashUiState {
    object Loading : SplashUiState()
    object Authenticated : SplashUiState()
    object Unauthenticated : SplashUiState()
}
