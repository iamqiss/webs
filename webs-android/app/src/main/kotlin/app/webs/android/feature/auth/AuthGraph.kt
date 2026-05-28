package app.webs.android.feature.auth

import androidx.navigation.NavGraphBuilder
import androidx.navigation.compose.composable

fun NavGraphBuilder.authGraph(
    onAuthenticated: () -> Unit
) {

    composable("auth") {
        AuthScreen(
            onAuthenticated = onAuthenticated
        )
    }
}
