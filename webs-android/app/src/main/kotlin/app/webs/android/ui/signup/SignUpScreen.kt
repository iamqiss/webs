package app.webs.android.ui.signup

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// SignUpScreen
@Composable
fun SignUpScreen(
    viewModel: SignUpViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}
