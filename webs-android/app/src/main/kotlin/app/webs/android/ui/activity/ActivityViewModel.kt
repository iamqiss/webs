package app.webs.android.ui.activity

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// ActivityViewModel — Activity feed — replies, follows, reactions
@HiltViewModel
class ActivityViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ActivityUiState())
    val uiState: StateFlow<ActivityUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class ActivityUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
