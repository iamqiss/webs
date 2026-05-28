package app.webs.android.ui.conversation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// ConversationViewModel — 1:1 and group message thread
@HiltViewModel
class ConversationViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ConversationUiState())
    val uiState: StateFlow<ConversationUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class ConversationUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
