package app.webs.android.core.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.rememberNavController

@Composable
fun WebsAppNavHost() {

    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "auth"
    ) {
        authGraph(
            onAuthenticated = {
                navController.navigate("home")
            }
        )

        composable("home") {
            HomeScreen()
        }
    }
}
