package app.webs.android.ui.createpost

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// CreatePostScreen
@Composable
fun CreatePostScreen(
    viewModel: CreatePostViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}
