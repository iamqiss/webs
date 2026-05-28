package app.webs.android.ui.messages

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// MessagesViewModel — DM inbox list
@HiltViewModel
class MessagesViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(MessagesUiState())
    val uiState: StateFlow<MessagesUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class MessagesUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
