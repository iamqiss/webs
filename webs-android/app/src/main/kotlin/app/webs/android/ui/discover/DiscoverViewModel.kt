package app.webs.android.ui.discover

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// DiscoverViewModel — Search, trending, follow suggestions
@HiltViewModel
class DiscoverViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(DiscoverUiState())
    val uiState: StateFlow<DiscoverUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class DiscoverUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
