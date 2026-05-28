package app.webs.android.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable

// WebsTheme — Material You with dynamic color support
// Follows the user's system wallpaper color on Android 12+
@Composable
fun WebsTheme(
    darkTheme: Boolean = false, // TODO: read from settings DataStore
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    // TODO: build ColorScheme — dynamic on API 31+, fallback to Webs brand palette
    MaterialTheme(content = content)
}
