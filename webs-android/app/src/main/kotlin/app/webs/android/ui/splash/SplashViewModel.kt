package app.webs.android.ui.splash

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// SplashViewModel — Initial loading / session check
@HiltViewModel
class SplashViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(SplashUiState())
    val uiState: StateFlow<SplashUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class SplashUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
