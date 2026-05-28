#!/usr/bin/env python3
"""
Webs Android v3 Scaffold
Production-grade Clean Architecture + Compose + Hilt + Navigation modular system.
"""

import os

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def write(path: str, content: str = ""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")


def touch(path: str):
    write(path, "")


BASE = "webs-android/app/src/main/kotlin/app/webs/android"

def domain(path): return f"{BASE}/domain/{path}"
def data(path): return f"{BASE}/data/{path}"
def feature(path): return f"{BASE}/feature/{path}"
def ui(path): return f"{BASE}/ui/{path}"
def core(path): return f"{BASE}/core/{path}"
def assets(path): return f"webs-android/assets/{path}"

# ─────────────────────────────────────────────
# CLEAN ARCHITECTURE ROOT APP
# ─────────────────────────────────────────────

MAIN_ACTIVITY = """\
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
"""

APPLICATION = """\
package app.webs.android

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class WebsApplication : Application()
"""

# ─────────────────────────────────────────────
# APP NAVIGATION ROOT (STATE MACHINE)
# ─────────────────────────────────────────────

APP_NAV = """\
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
"""

# ─────────────────────────────────────────────
# AUTH FEATURE (STATE MACHINE LIKE iOS)
# ─────────────────────────────────────────────

AUTH_STATE = """\
package app.webs.android.feature.auth

sealed class AuthState {
    data object Splash : AuthState()
    data object Onboarding : AuthState()
    data object Login : AuthState()
    data object Signup : AuthState()
    data object Passphrase : AuthState()
}
"""

AUTH_VIEWMODEL = """\
package app.webs.android.feature.auth

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class AuthViewModel : ViewModel() {

    private val _state =
        MutableStateFlow<AuthState>(AuthState.Splash)

    val state: StateFlow<AuthState> = _state

    fun next() {
        _state.value = when (_state.value) {
            AuthState.Splash -> AuthState.Onboarding
            AuthState.Onboarding -> AuthState.Login
            AuthState.Login -> AuthState.Passphrase
            AuthState.Passphrase -> AuthState.Passphrase
            AuthState.Signup -> AuthState.Login
        }
    }
}
"""

AUTH_SCREEN = """\
package app.webs.android.feature.auth

import androidx.compose.runtime.*
import androidx.hilt.navigation.compose.hiltViewModel

@Composable
fun AuthScreen(
    viewModel: AuthViewModel = hiltViewModel(),
    onAuthenticated: () -> Unit
) {

    val state = viewModel.state.collectAsState()

    when (state.value) {

        AuthState.Splash -> SplashScreen()
        AuthState.Onboarding -> OnboardingScreen()
        AuthState.Login -> LoginScreen()
        AuthState.Signup -> SignUpScreen()
        AuthState.Passphrase -> PassphraseScreen(
            onAuthenticated = onAuthenticated
        )
    }
}
"""

# ─────────────────────────────────────────────
# DOMAIN (BUSINESS LOGIC)
# ─────────────────────────────────────────────

TRUST_SIGNAL = """\
package app.webs.android.domain.model

data class TrustSignal(
    val typingSpeed: Float,
    val pressure: Float,
    val rhythm: Float,
    val timestamp: Long = System.currentTimeMillis()
)
"""

EMOPAT = """\
package app.webs.android.domain.auth

data class EmoPat(
    val baselineSpeed: Float = 0f,
    val baselinePressure: Float = 0f,
    val confidence: Float = 0f
)
"""

# ─────────────────────────────────────────────
# DATA LAYER (TRUST ENGINE)
# ─────────────────────────────────────────────

TRUST_COLLECTOR = """\
package app.webs.android.data.trust

import app.webs.android.domain.model.TrustSignal

class TrustCollector {

    private val signals = mutableListOf<TrustSignal>()

    fun add(signal: TrustSignal) {
        signals.add(signal)
    }

    fun averageSpeed(): Float =
        signals.map { it.typingSpeed }.average().toFloat()
}
"""

EMOPAT_ENGINE = """\
package app.webs.android.data.trust

import app.webs.android.domain.model.TrustSignal
import kotlin.math.abs

class EmoPatEngine {

    fun score(
        signal: TrustSignal,
        baselineSpeed: Float,
        baselinePressure: Float
    ): Float {

        val speedDelta = abs(signal.typingSpeed - baselineSpeed)
        val pressureDelta = abs(signal.pressure - baselinePressure)

        return (1f - (speedDelta + pressureDelta) / 2f)
            .coerceIn(0f, 1f)
    }
}
"""

# ─────────────────────────────────────────────
# NAVIGATION GRAPH (AUTH)
# ─────────────────────────────────────────────

AUTH_GRAPH = """\
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
"""

# ─────────────────────────────────────────────
# UI SCREENS (STUBS)
# ─────────────────────────────────────────────

SCREENS = [
    "SplashScreen",
    "OnboardingScreen",
    "LoginScreen",
    "SignUpScreen",
    "PassphraseScreen"
]

def screen_stub(name):
    return f"""\
package app.webs.android.feature.auth

import androidx.compose.material3.*
import androidx.compose.runtime.Composable

@Composable
fun {name}() {{
    Text(\"{name}\")
}}
"""

# ─────────────────────────────────────────────
# ASSETS PIPELINE (IMPORTANT ADDITION YOU ASKED FOR)
# ─────────────────────────────────────────────

ASSETS = {
    "icons/README.md": """\
SVG ICONS:
- home.svg
- discover.svg
- post.svg
- circle.svg
- profile.svg
""",

    "images/README.md": """\
APP IMAGES:
- splash.png
- app_logo.png
- banner.png
""",

    "app_store/README.md": """\
APP STORE:
- icon_1024.png
- screenshot_1.png
- screenshot_2.png
""",

    "splash/README.md": """\
SPLASH ASSETS:
- splash_light.png
- splash_dark.png
"""
}

# ─────────────────────────────────────────────
# SCHEMA GENERATOR
# ─────────────────────────────────────────────

def scaffold():

    print("\n🕸 Webs Android v3 (Clean Architecture + Production Compose)\n")

    # App core
    write("webs-android/app/src/main/java/app/webs/android/MainActivity.kt", MAIN_ACTIVITY)
    write("webs-android/app/src/main/java/app/webs/android/WebsApplication.kt", APPLICATION)

    # Navigation
    write(f"{BASE}/core/navigation/WebsAppNavHost.kt", APP_NAV)
    write(f"{BASE}/feature/auth/AuthGraph.kt", AUTH_GRAPH)

    # Auth feature
    write(f"{BASE}/feature/auth/AuthState.kt", AUTH_STATE)
    write(f"{BASE}/feature/auth/AuthViewModel.kt", AUTH_VIEWMODEL)
    write(f"{BASE}/feature/auth/AuthScreen.kt", AUTH_SCREEN)

    # Screens
    for s in SCREENS:
        write(f"{BASE}/feature/auth/{s}.kt", screen_stub(s))

    # Domain
    write(domain("model/TrustSignal.kt"), TRUST_SIGNAL)
    write(domain("auth/EmoPat.kt"), EMOPAT)

    # Data
    write(data("trust/TrustCollector.kt"), TRUST_COLLECTOR)
    write(data("trust/EmoPatEngine.kt"), EMOPAT_ENGINE)

    # Assets system
    for path, content in ASSETS.items():
        write(f"webs-android/assets/{path}", content)

    print("\n✅ Webs Android v3 scaffold complete (production-grade architecture)\n")


if __name__ == "__main__":
    scaffold()
