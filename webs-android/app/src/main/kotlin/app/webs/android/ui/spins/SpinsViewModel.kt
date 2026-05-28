package app.webs.android.ui.spins

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// SpinsViewModel — Full-screen vertical video feed
@HiltViewModel
class SpinsViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(SpinsUiState())
    val uiState: StateFlow<SpinsUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class SpinsUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
