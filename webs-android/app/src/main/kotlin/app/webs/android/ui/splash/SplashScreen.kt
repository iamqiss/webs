package app.webs.android.ui.splash

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.hilt.navigation.compose.hiltViewModel
import app.webs.android.R

@Composable
fun SplashScreen(
    viewModel: SplashViewModel = hiltViewModel(),
    onNavigateToOnboarding: () -> Unit,
    onNavigateToHome: () -> Unit
) {
    val state by viewModel.uiState.collectAsState()
    val isDarkTheme = isSystemInDarkTheme()

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(if (isDarkTheme) Color.Black else Color.White),
        contentAlignment = Alignment.Center
    ) {
        when (state) {
            is SplashUiState.Loading -> {
                SplashContent(isDarkTheme = isDarkTheme)
            }
            is SplashUiState.Authenticated -> {
                LaunchedEffect(Unit) {
                    onNavigateToHome()
                }
                SplashContent(isDarkTheme = isDarkTheme) // Keep showing splash while navigating
            }
            is SplashUiState.Unauthenticated -> {
                LaunchedEffect(Unit) {
                    onNavigateToOnboarding()
                }
                SplashContent(isDarkTheme = isDarkTheme)
            }
        }
    }
}

@Composable
private fun SplashContent(isDarkTheme: Boolean) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center,
        modifier = Modifier.fillMaxSize()
    ) {
        // Splash Image
        Image(
            painter = painterResource(
                id = if (isDarkTheme) R.drawable.splash_dark else R.drawable.splash
            ),
            contentDescription = "Webs Splash",
            modifier = Modifier.size(160.dp),
            contentScale = ContentScale.Fit
        )

        Spacer(Modifier.height(40.dp))

        // Logo Text
        Text(
            text = "Webs",
            fontSize = 52.sp,
            fontWeight = FontWeight.Bold,
            letterSpacing = (-2.5).sp,
            color = if (isDarkTheme) Color.White else Color.Black
        )

        Spacer(Modifier.height(16.dp))

        // Tagline
        Text(
            text = "Post a Web.\nWatch a Spin.\nJoin a Circle.",
            fontSize = 17.sp,
            fontWeight = FontWeight.Medium,
            textAlign = TextAlign.Center,
            lineHeight = 28.sp,
            color = if (isDarkTheme) Color(0xFFAAAAAA) else Color(0xFF555555),
            modifier = Modifier.padding(horizontal = 48.dp)
        )
    }

    // Footer
    Text(
        text = "© 2026 Webs",
        fontSize = 12.sp,
        color = Color.Gray,
        modifier = Modifier
            .align(Alignment.BottomCenter)
            .padding(bottom = 48.dp)
    )
}
