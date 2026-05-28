package app.webs.android.ui.home

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// HomeViewModel — For You / Following / Trending feed
@HiltViewModel
class HomeViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(HomeUiState())
    val uiState: StateFlow<HomeUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class HomeUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
