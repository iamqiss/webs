package app.webs.android.ui.signup

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// SignUpViewModel — New account creation
@HiltViewModel
class SignUpViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(SignUpUiState())
    val uiState: StateFlow<SignUpUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class SignUpUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
