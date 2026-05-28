#!/usr/bin/env python3
"""
scaffold_webs_android.py
Scaffolds the webs-android Jetpack Compose project file tree.
Run from the root of the webs monorepo:
    python3 scaffold_webs_android.py
"""

import os

# ── Helpers ────────────────────────────────────────────────────────────────────

def write(path: str, content: str = "") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")

def touch(path: str) -> None:
    write(path, "")

# ── File contents ──────────────────────────────────────────────────────────────

SETTINGS_GRADLE = """\
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "Webs"
include(":app")
"""

BUILD_GRADLE_ROOT = """\
// Top-level build file
plugins {
    alias(libs.plugins.android.application)  apply false
    alias(libs.plugins.kotlin.android)       apply false
    alias(libs.plugins.kotlin.compose)       apply false
    alias(libs.plugins.hilt)                 apply false
    alias(libs.plugins.ksp)                  apply false
    alias(libs.plugins.protobuf)             apply false
}
"""

BUILD_GRADLE_APP = """\
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
    alias(libs.plugins.hilt)
    alias(libs.plugins.ksp)
    alias(libs.plugins.protobuf)
}

android {
    namespace         = "app.webs.android"
    compileSdk        = 35

    defaultConfig {
        applicationId = "app.webs.android"
        minSdk        = 26
        targetSdk     = 35
        versionCode   = 1
        versionName   = "1.0.0"
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {

    // Compose BOM
    implementation(platform(libs.compose.bom))
    implementation(libs.compose.ui)
    implementation(libs.compose.ui.tooling.preview)
    implementation(libs.compose.material3)
    implementation(libs.compose.material.icons)

    debugImplementation(libs.compose.ui.tooling)

    // Navigation
    implementation(libs.navigation.compose)

    // Lifecycle
    implementation(libs.lifecycle.viewmodel.compose)
    implementation(libs.lifecycle.runtime.compose)

    // Hilt
    implementation(libs.hilt.android)
    implementation(libs.hilt.navigation.compose)
    ksp(libs.hilt.compiler)

    // Room
    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)

    // DataStore
    implementation(libs.datastore.preferences)

    // Coroutines
    implementation(libs.kotlinx.coroutines.android)

    // Coil
    implementation(libs.coil.compose)

    // WorkManager
    implementation(libs.work.runtime.ktx)
    implementation(libs.hilt.work)

    // Media3
    implementation(libs.media3.exoplayer)
    implementation(libs.media3.ui)

    // gRPC
    implementation(libs.grpc.kotlin.stub)
    implementation(libs.grpc.android)
    implementation(libs.grpc.okhttp)
    implementation(libs.protobuf.kotlin.lite)

    // Testing
    testImplementation(libs.junit)
}
"""

LIBS_VERSIONS_TOML = """\
[versions]
agp                     = "8.5.0"
kotlin                  = "2.0.0"
compose-bom             = "2024.06.00"
navigation              = "2.8.0"
lifecycle               = "2.8.2"
hilt                    = "2.51.1"
ksp                     = "2.0.0-1.0.21"
room                    = "2.6.1"
datastore               = "1.1.1"
grpc-kotlin             = "1.4.1"
grpc-android            = "1.64.0"
protobuf                = "4.27.0"
media3                  = "1.3.1"
work                    = "2.9.0"
coil                    = "2.7.0"
coroutines              = "1.8.1"

[libraries]
compose-bom                  = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-ui                   = { group = "androidx.compose.ui", name = "ui" }
compose-ui-tooling           = { group = "androidx.compose.ui", name = "ui-tooling" }
compose-ui-tooling-preview   = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
compose-material3            = { group = "androidx.compose.material3", name = "material3" }
compose-material-icons       = { group = "androidx.compose.material", name = "material-icons-extended" }

navigation-compose           = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigation" }

lifecycle-viewmodel-compose  = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
lifecycle-runtime-compose    = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose", version.ref = "lifecycle" }

hilt-android                 = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler                = { group = "com.google.dagger", name = "hilt-compiler", version.ref = "hilt" }
hilt-navigation-compose      = { group = "androidx.hilt", name = "hilt-navigation-compose", version = "1.2.0" }
hilt-work                    = { group = "androidx.hilt", name = "hilt-work", version = "1.2.0" }

room-runtime                 = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx                     = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-compiler                = { group = "androidx.room", name = "room-compiler", version.ref = "room" }

datastore-preferences        = { group = "androidx.datastore", name = "datastore-preferences", version.ref = "datastore" }

grpc-kotlin-stub             = { group = "io.grpc", name = "grpc-kotlin-stub", version.ref = "grpc-kotlin" }
grpc-android                 = { group = "io.grpc", name = "grpc-android", version.ref = "grpc-android" }
grpc-okhttp                  = { group = "io.grpc", name = "grpc-okhttp", version.ref = "grpc-android" }

protobuf-kotlin-lite         = { group = "com.google.protobuf", name = "protobuf-kotlin-lite", version.ref = "protobuf" }

media3-exoplayer             = { group = "androidx.media3", name = "media3-exoplayer", version.ref = "media3" }
media3-ui                    = { group = "androidx.media3", name = "media3-ui", version.ref = "media3" }

work-runtime-ktx             = { group = "androidx.work", name = "work-runtime-ktx", version.ref = "work" }

coil-compose                 = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }

kotlinx-coroutines-android   = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "coroutines" }

junit                        = { group = "junit", name = "junit", version = "4.13.2" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android      = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose      = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
hilt                = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
ksp                 = { id = "com.google.devtools.ksp", version.ref = "ksp" }
protobuf            = { id = "com.google.protobuf", version = "0.9.4" }
"""

MANIFEST = """\
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:name=".WebsApplication"
        android:label="@string/app_name"
        android:supportsRtl="true">

        <activity
            android:name=".MainActivity"
            android:exported="true">

            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

        </activity>

    </application>

</manifest>
"""

MAIN_ACTIVITY = """\
package app.webs.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import dagger.hilt.android.AndroidEntryPoint
import app.webs.android.navigation.WebsNavHost
import app.webs.android.ui.theme.WebsTheme

@AndroidEntryPoint
class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            WebsTheme {
                WebsNavHost()
            }
        }
    }
}
"""

WEBS_APPLICATION = """\
package app.webs.android

import android.app.Application
import dagger.hilt.android.HiltAndroidApp

@HiltAndroidApp
class WebsApplication : Application()
"""

NAV_HOST = """\
package app.webs.android.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.rememberNavController

@Composable
fun WebsNavHost() {

    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "passphrase"
    ) {

        authNavGraph(
            onAuthenticated = {
                navController.navigate("home")
            }
        )
    }
}
"""

WEBS_THEME = """\
package app.webs.android.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable

@Composable
fun WebsTheme(
    content: @Composable () -> Unit
) {
    MaterialTheme(
        content = content
    )
}
"""

PASSPHRASE_SCREEN = """\
package app.webs.android.ui.auth

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel

@Composable
fun PassphraseScreen(
    viewModel: AuthViewModel = hiltViewModel(),
    onAuthenticated: () -> Unit = {}
) {

    var passphrase by remember {
        mutableStateOf("")
    }

    val uiState by viewModel.uiState.collectAsState()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        verticalArrangement = Arrangement.Center
    ) {

        Text(
            text = "Enter Passphrase",
            style = MaterialTheme.typography.headlineMedium
        )

        Spacer(modifier = Modifier.height(16.dp))

        OutlinedTextField(
            value = passphrase,
            onValueChange = {
                passphrase = it
            },
            modifier = Modifier.fillMaxWidth(),
            singleLine = true
        )

        Spacer(modifier = Modifier.height(16.dp))

        Button(
            onClick = {
                viewModel.authenticate(
                    passphrase,
                    onAuthenticated
                )
            },
            modifier = Modifier.fillMaxWidth()
        ) {
            Text("Unlock")
        }

        uiState.error?.let {
            Spacer(modifier = Modifier.height(12.dp))

            Text(
                text = it,
                color = MaterialTheme.colorScheme.error
            )
        }
    }
}
"""

EMOPAT = """\
package app.webs.android.ui.auth

data class EmoPat(
    val baselineTypingSpeed: Float = 0f,
    val baselinePressure: Float = 0f,
    val baselineRhythm: Float = 0f,
    val confidenceScore: Float = 0f
)
"""

EMOPAT_CHALLENGE = """\
package app.webs.android.ui.auth

enum class EmoPatChallenge {
    HOLD,
    SWIPE,
    TYPE
}
"""

TRUST_SIGNAL = """\
package app.webs.android.domain.model

data class TrustSignal(
    val typingSpeed: Float,
    val touchPressure: Float,
    val rhythmVariance: Float,
    val timestamp: Long = System.currentTimeMillis()
)
"""

TRUST_COLLECTOR = """\
package app.webs.android.data.trust

import app.webs.android.domain.model.TrustSignal
import kotlin.math.abs

class TrustCollector {

    private val signals = mutableListOf<TrustSignal>()

    fun addSignal(signal: TrustSignal) {
        signals.add(signal)
    }

    fun clear() {
        signals.clear()
    }

    fun averageTypingSpeed(): Float {
        if (signals.isEmpty()) return 0f

        return signals
            .map { it.typingSpeed }
            .average()
            .toFloat()
    }

    fun averagePressure(): Float {
        if (signals.isEmpty()) return 0f

        return signals
            .map { it.touchPressure }
            .average()
            .toFloat()
    }

    fun rhythmVariance(): Float {

        if (signals.size < 2) return 0f

        val deltas = signals.zipWithNext {
            a, b ->
            abs(a.timestamp - b.timestamp).toFloat()
        }

        return deltas.average().toFloat()
    }
}
"""

EMOPAT_TELEMETRY = """\
package app.webs.android.data.trust

import app.webs.android.domain.model.TrustSignal
import kotlin.math.abs

class EmoPatTelemetry {

    fun calculateConfidence(
        current: TrustSignal,
        baselineSpeed: Float,
        baselinePressure: Float
    ): Float {

        val speedDelta =
            abs(current.typingSpeed - baselineSpeed)

        val pressureDelta =
            abs(current.touchPressure - baselinePressure)

        val score =
            1f - ((speedDelta + pressureDelta) / 2f)

        return score.coerceIn(0f, 1f)
    }
}
"""

AUTH_VIEWMODEL = """\
package app.webs.android.ui.auth

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch
import javax.inject.Inject

data class AuthUiState(
    val isLoading: Boolean = false,
    val error: String? = null
)

@HiltViewModel
class AuthViewModel @Inject constructor(
) : ViewModel() {

    private val _uiState =
        MutableStateFlow(AuthUiState())

    val uiState: StateFlow<AuthUiState> =
        _uiState.asStateFlow()

    fun authenticate(
        passphrase: String,
        onSuccess: () -> Unit
    ) {

        viewModelScope.launch {

            _uiState.value =
                AuthUiState(isLoading = true)

            if (passphrase.length >= 8) {
                onSuccess()
            } else {
                _uiState.value =
                    AuthUiState(
                        error = "Invalid passphrase"
                    )
            }
        }
    }
}
"""

AUTH_NAV_GRAPH = """\
package app.webs.android.navigation

import androidx.navigation.NavGraphBuilder
import androidx.navigation.compose.composable
import app.webs.android.ui.auth.PassphraseScreen

fun NavGraphBuilder.authNavGraph(
    onAuthenticated: () -> Unit
) {

    composable("passphrase") {

        PassphraseScreen(
            onAuthenticated = onAuthenticated
        )
    }
}
"""

# ── Scaffold ───────────────────────────────────────────────────────────────────

def scaffold():

    base = "webs-android"

    src = f"{base}/app/src/main/kotlin/app/webs/android"

    print(f"\\n🕸  Scaffolding {base}/\\n")

    # Gradle
    write(f"{base}/settings.gradle.kts", SETTINGS_GRADLE)
    write(f"{base}/build.gradle.kts", BUILD_GRADLE_ROOT)
    write(f"{base}/app/build.gradle.kts", BUILD_GRADLE_APP)
    write(f"{base}/gradle/libs.versions.toml", LIBS_VERSIONS_TOML)

    # Manifest
    write(f"{base}/app/src/main/AndroidManifest.xml", MANIFEST)

    # App
    write(f"{src}/MainActivity.kt", MAIN_ACTIVITY)
    write(f"{src}/WebsApplication.kt", WEBS_APPLICATION)

    # Navigation
    write(f"{src}/navigation/WebsNavHost.kt", NAV_HOST)
    write(f"{src}/navigation/AuthNavGraph.kt", AUTH_NAV_GRAPH)

    # Theme
    write(f"{src}/ui/theme/WebsTheme.kt", WEBS_THEME)

    # Auth
    write(f"{src}/ui/auth/PassphraseScreen.kt", PASSPHRASE_SCREEN)
    write(f"{src}/ui/auth/AuthViewModel.kt", AUTH_VIEWMODEL)
    write(f"{src}/ui/auth/EmoPat.kt", EMOPAT)
    write(f"{src}/ui/auth/EmoPatChallenge.kt", EMOPAT_CHALLENGE)

    # Trust
    write(f"{src}/domain/model/TrustSignal.kt", TRUST_SIGNAL)
    write(f"{src}/data/trust/TrustCollector.kt", TRUST_COLLECTOR)
    write(f"{src}/data/trust/EmoPatTelemetry.kt", EMOPAT_TELEMETRY)

    print("\\n✅ Done. Open webs-android/ in Android Studio and sync Gradle.\\n")

# ── Entry ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    scaffold()


