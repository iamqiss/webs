package app.webs.android.ui.onboarding

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// OnboardingViewModel — First-run onboarding flow
@HiltViewModel
class OnboardingViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(OnboardingUiState())
    val uiState: StateFlow<OnboardingUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class OnboardingUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
