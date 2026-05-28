package app.webs.android.ui.circledetail

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// CircleDetailViewModel — Single Circle feed and about page
@HiltViewModel
class CircleDetailViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(CircleDetailUiState())
    val uiState: StateFlow<CircleDetailUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class CircleDetailUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
