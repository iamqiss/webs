package app.webs.android.ui.createspin

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// CreateSpinViewModel — Record or upload a Spin
@HiltViewModel
class CreateSpinViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(CreateSpinUiState())
    val uiState: StateFlow<CreateSpinUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class CreateSpinUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
