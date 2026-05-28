package app.webs.android.ui.settings

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// SettingsViewModel — Account, privacy, notifications, theme
@HiltViewModel
class SettingsViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(SettingsUiState())
    val uiState: StateFlow<SettingsUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class SettingsUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
