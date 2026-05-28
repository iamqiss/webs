package app.webs.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import dagger.hilt.android.AndroidEntryPoint
import app.webs.android.core.navigation.WebsAppNavHost
import app.webs.android.ui.theme.WebsTheme

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            WebsTheme {
                WebsAppNavHost()
            }
        }
    }
}
