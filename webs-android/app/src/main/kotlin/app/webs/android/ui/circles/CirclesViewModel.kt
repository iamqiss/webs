package app.webs.android.ui.circles

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// CirclesViewModel — My Circles + Explore tab
@HiltViewModel
class CirclesViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(CirclesUiState())
    val uiState: StateFlow<CirclesUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class CirclesUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
