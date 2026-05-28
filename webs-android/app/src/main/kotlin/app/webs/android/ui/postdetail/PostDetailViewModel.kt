package app.webs.android.ui.postdetail

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// PostDetailViewModel — Single Web detail + comments
@HiltViewModel
class PostDetailViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(PostDetailUiState())
    val uiState: StateFlow<PostDetailUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class PostDetailUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
