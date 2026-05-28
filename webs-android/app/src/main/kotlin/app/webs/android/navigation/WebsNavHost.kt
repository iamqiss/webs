package app.webs.android.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.rememberNavController

// WebsNavHost — top-level navigation graph
// Sealed destinations keep routes type-safe
@Composable
fun WebsNavHost() {
    val navController = rememberNavController()
    // TODO: define NavHost with auth and main graphs
    NavHost(navController = navController, startDestination = "home") {
        // TODO: composable destinations
    }
}
