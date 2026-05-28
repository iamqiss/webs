package app.webs.android.ui.stories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// StoriesViewModel — Full-screen story viewer
@HiltViewModel
class StoriesViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(StoriesUiState())
    val uiState: StateFlow<StoriesUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class StoriesUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
