package app.webs.android.ui.createspin

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// CreateSpinScreen
@Composable
fun CreateSpinScreen(
    viewModel: CreateSpinViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}
