package app.webs.android.ui.onboarding

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// OnboardingScreen
@Composable
fun OnboardingScreen(
    viewModel: OnboardingViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}
