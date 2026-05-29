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
import app.webs.android.R
import kotlinx.coroutines.delay

@Composable
fun SplashScreen(
    onNavigateToOnboarding: () -> Unit,
    onAlreadyLoggedIn: () -> Unit
) {
    val isDarkTheme = isSystemInDarkTheme()

    LaunchedEffect(Unit) {
        // Simulate loading + check auth state
        delay(1600)

        // TODO: Replace with real auth check (DataStore, JWT, etc.)
        val isLoggedIn = false // Change to true during testing if needed

        if (isLoggedIn) {
            onAlreadyLoggedIn()
        } else {
            onNavigateToOnboarding()
        }
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(if (isDarkTheme) Color.Black else Color.White),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Main splash image
            Image(
                painter = painterResource(
                    id = if (isDarkTheme) R.drawable.splash_dark else R.drawable.splash
                ),
                contentDescription = "Webs Splash",
                modifier = Modifier.size(180.dp),
                contentScale = ContentScale.Fit
            )

            Spacer(Modifier.height(32.dp))

            // Logo text
            Text(
                text = "Webs",
                fontSize = 48.sp,
                fontWeight = FontWeight.Bold,
                letterSpacing = (-2).sp,
                color = if (isDarkTheme) Color.White else Color.Black
            )

            Spacer(Modifier.height(12.dp))

            // Tagline
            Text(
                text = "Post a Web.\nWatch a Spin.\nJoin a Circle.",
                fontSize = 18.sp,
                fontWeight = FontWeight.Medium,
                textAlign = TextAlign.Center,
                lineHeight = 26.sp,
                color = if (isDarkTheme) Color.LightGray else Color.DarkGray,
                modifier = Modifier.padding(horizontal = 40.dp)
            )
        }

        // Bottom branding
        Text(
            text = "© 2026 Webs • All Rights Reserved",
            fontSize = 12.sp,
            color = Color.Gray,
            modifier = Modifier
                .align(Alignment.BottomCenter)
                .padding(bottom = 48.dp)
        )
    }
}
