package app.webs.android.ui.createpost

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// CreatePostViewModel — Compose a Web — text, images, circle tag
@HiltViewModel
class CreatePostViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(CreatePostUiState())
    val uiState: StateFlow<CreatePostUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class CreatePostUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
