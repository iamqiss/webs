package app.webs.android.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue

// MainScaffold — hosts the floating nav bar and the compose (＋) button
// The ＋ button floats above the nav, rises on scroll-up, retreats on scroll-down
@Composable
fun MainScaffold(content: @Composable () -> Unit) {
    // TODO: implement floating NavBar with scroll-aware compose button
    content()
}
