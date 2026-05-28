package app.webs.android.ui.editprofile

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// EditProfileViewModel — Edit display name, bio, avatar, banner
@HiltViewModel
class EditProfileViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {

    private val _uiState = MutableStateFlow(EditProfileUiState())
    val uiState: StateFlow<EditProfileUiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}

data class EditProfileUiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
