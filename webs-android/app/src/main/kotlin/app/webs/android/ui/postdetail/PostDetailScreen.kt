package app.webs.android.ui.postdetail

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// PostDetailScreen
@Composable
fun PostDetailScreen(
    viewModel: PostDetailViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}
