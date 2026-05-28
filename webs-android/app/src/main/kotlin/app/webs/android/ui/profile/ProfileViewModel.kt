package app.webs.android.ui.profile

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// ProfileViewModel — Own and other user profiles — Webs + Spins tabs
@HiltViewModel
class ProfileViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ProfileUiState())
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class ProfileUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
