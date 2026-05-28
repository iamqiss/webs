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

    // Lifecycle + ViewModel
    implementation(libs.lifecycle.viewmodel.compose)
    implementation(libs.lifecycle.runtime.compose)

    // Hilt DI
    implementation(libs.hilt.android)
    implementation(libs.hilt.navigation.compose)
    ksp(libs.hilt.compiler)

    // gRPC
    implementation(libs.grpc.kotlin.stub)
    implementation(libs.grpc.android)
    implementation(libs.grpc.okhttp)
    implementation(libs.protobuf.kotlin.lite)

    // Room (offline-first)
    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)

    // DataStore (settings / tokens)
    implementation(libs.datastore.preferences)

    // Media3 / ExoPlayer (Spins)
    implementation(libs.media3.exoplayer)
    implementation(libs.media3.ui)

    // WorkManager (background sync)
    implementation(libs.work.runtime.ktx)
    implementation(libs.hilt.work)

    // Coil (image loading)
    implementation(libs.coil.compose)

    // Coroutines
    implementation(libs.kotlinx.coroutines.android)

    // Testing
    testImplementation(libs.junit)
    testImplementation(libs.kotlinx.coroutines.test)
    testImplementation(libs.turbine)
    androidTestImplementation(libs.androidx.test.ext)
    androidTestImplementation(libs.compose.ui.test.junit4)
}

protobuf {
    protoc { artifact = libs.protoc.get().toString() }
    generateProtoTasks {
        all().forEach { task ->
            task.builtins { id("kotlin") { option("lite") } }
        }
    }
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
turbine                 = "1.1.0"

[libraries]
compose-bom                  = { group = "androidx.compose", name = "compose-bom",            version.ref = "compose-bom" }
compose-ui                   = { group = "androidx.compose.ui", name = "ui" }
compose-ui-tooling           = { group = "androidx.compose.ui", name = "ui-tooling" }
compose-ui-tooling-preview   = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
compose-material3            = { group = "androidx.compose.material3", name = "material3" }
compose-material-icons       = { group = "androidx.compose.material", name = "material-icons-extended" }
compose-ui-test-junit4       = { group = "androidx.compose.ui", name = "ui-test-junit4" }
navigation-compose           = { group = "androidx.navigation", name = "navigation-compose",  version.ref = "navigation" }
lifecycle-viewmodel-compose  = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
lifecycle-runtime-compose    = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose",   version.ref = "lifecycle" }
hilt-android                 = { group = "com.google.dagger", name = "hilt-android",          version.ref = "hilt" }
hilt-compiler                = { group = "com.google.dagger", name = "hilt-compiler",         version.ref = "hilt" }
hilt-navigation-compose      = { group = "androidx.hilt", name = "hilt-navigation-compose",   version = "1.2.0" }
hilt-work                    = { group = "androidx.hilt", name = "hilt-work",                 version = "1.2.0" }
room-runtime                 = { group = "androidx.room", name = "room-runtime",              version.ref = "room" }
room-ktx                     = { group = "androidx.room", name = "room-ktx",                 version.ref = "room" }
room-compiler                = { group = "androidx.room", name = "room-compiler",            version.ref = "room" }
datastore-preferences        = { group = "androidx.datastore", name = "datastore-preferences", version.ref = "datastore" }
grpc-kotlin-stub             = { group = "io.grpc", name = "grpc-kotlin-stub",               version.ref = "grpc-kotlin" }
grpc-android                 = { group = "io.grpc", name = "grpc-android",                   version.ref = "grpc-android" }
grpc-okhttp                  = { group = "io.grpc", name = "grpc-okhttp",                    version.ref = "grpc-android" }
protobuf-kotlin-lite         = { group = "com.google.protobuf", name = "protobuf-kotlin-lite", version.ref = "protobuf" }
protoc                       = { group = "com.google.protobuf", name = "protoc",              version.ref = "protobuf" }
media3-exoplayer             = { group = "androidx.media3", name = "media3-exoplayer",        version.ref = "media3" }
media3-ui                    = { group = "androidx.media3", name = "media3-ui",               version.ref = "media3" }
work-runtime-ktx             = { group = "androidx.work", name = "work-runtime-ktx",         version.ref = "work" }
coil-compose                 = { group = "io.coil-kt", name = "coil-compose",                version.ref = "coil" }
kotlinx-coroutines-android   = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "coroutines" }
kotlinx-coroutines-test      = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-test",    version.ref = "coroutines" }
turbine                      = { group = "app.cash.turbine", name = "turbine",               version.ref = "turbine" }
junit                        = { group = "junit", name = "junit",                            version = "4.13.2" }
androidx-test-ext            = { group = "androidx.test.ext", name = "junit",               version = "1.2.1" }

[plugins]
android-application = { id = "com.android.application",            version.ref = "agp" }
kotlin-android      = { id = "org.jetbrains.kotlin.android",       version.ref = "kotlin" }
kotlin-compose      = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
hilt                = { id = "com.google.dagger.hilt.android",     version.ref = "hilt" }
ksp                 = { id = "com.google.devtools.ksp",            version.ref = "ksp" }
protobuf            = { id = "com.google.protobuf",                version = "0.9.4" }
"""

MANIFEST = """\
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.READ_MEDIA_IMAGES" />
    <uses-permission android:name="android.permission.READ_MEDIA_VIDEO" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.VIBRATE" />

    <application
        android:name=".Webs Application"
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:theme="@style/Theme.Webs"
        android:supportsRtl="true">

        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <!-- TODO: deep link intent filters -->
        </activity>

    </application>
</manifest>
"""

MAIN_ACTIVITY = """\
package app.webs.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import dagger.hilt.android.AndroidEntryPoint
import app.webs.android.ui.theme.WebsTheme
import app.webs.android.navigation.WebsNavHost

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
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
import androidx.hilt.work.HiltWorkerFactory
import androidx.work.Configuration
import dagger.hilt.android.HiltAndroidApp
import javax.inject.Inject

@HiltAndroidApp
class WebsApplication : Application(), Configuration.Provider {
    @Inject lateinit var workerFactory: HiltWorkerFactory

    override val workManagerConfiguration: Configuration
        get() = Configuration.Builder()
            .setWorkerFactory(workerFactory)
            .build()
}
"""

NAV_HOST = """\
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
"""

NAV_DESTINATIONS = """\
package app.webs.android.navigation

// Type-safe route definitions
sealed class Destination(val route: String) {
    // Auth
    data object Splash        : Destination("splash")
    data object Onboarding    : Destination("onboarding")
    data object Login         : Destination("login")
    data object SignUp        : Destination("signup")

    // Main
    data object Home          : Destination("home")
    data object Discover      : Destination("discover")
    data object Spins         : Destination("spins")
    data object Circles       : Destination("circles")
    data object Profile       : Destination("profile/{userId}") {
        fun route(userId: String) = "profile/$userId"
    }

    // Detail
    data object PostDetail    : Destination("post/{postId}") {
        fun route(postId: String) = "post/$postId"
    }
    data object CircleDetail  : Destination("circle/{circleId}") {
        fun route(circleId: String) = "circle/$circleId"
    }
    data object Conversation  : Destination("conversation/{conversationId}") {
        fun route(id: String) = "conversation/$id"
    }

    // Create
    data object CreatePost    : Destination("create/post")
    data object CreateSpin    : Destination("create/spin")

    // Other
    data object Messages      : Destination("messages")
    data object Activity      : Destination("activity")
    data object EditProfile   : Destination("profile/edit")
    data object Settings      : Destination("settings")
}
"""

MAIN_SCAFFOLD = """\
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
"""

WEBS_THEME = """\
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
"""

WEBS_TYPE = """\
package app.webs.android.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.sp

// TODO: define Webs type scale — display, headline, body, label, caption
val WebsTypography = Typography(
    // bodyLarge = TextStyle(...)
)
"""

WEBS_COLOR = """\
package app.webs.android.ui.theme

import androidx.compose.ui.graphics.Color

// TODO: Webs brand color palette
// Used as fallback when dynamic color is unavailable (< API 31)
object WebsColors {
    val Black       = Color(0xFF000000)
    val White       = Color(0xFFFFFFFF)
    val Surface     = Color(0xFFF7F7F7)
    // TODO: add full palette
}
"""

# ── Kotlin file stubs ──────────────────────────────────────────────────────────

def viewmodel_stub(name: str, description: str) -> str:
    return f"""\
package app.webs.android.ui.{name.lower()}

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

// {name}ViewModel — {description}
@HiltViewModel
class {name}ViewModel @Inject constructor(
    // TODO: inject repository
) : ViewModel() {{

    private val _uiState = MutableStateFlow({name}UiState())
    val uiState: StateFlow<{name}UiState> = _uiState.asStateFlow()

    // TODO: implement intents / event handlers
}}

data class {name}UiState(
    val isLoading: Boolean = false,
    val error: String? = null,
    // TODO: state fields
)
"""

def screen_stub(name: str) -> str:
    pkg = name.lower().replace("screen", "")
    return f"""\
package app.webs.android.ui.{pkg}

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.hilt.navigation.compose.hiltViewModel

// {name}
@Composable
fun {name}(
    viewModel: {name.replace("Screen", "")}ViewModel = hiltViewModel(),
    // TODO: navigation callbacks
) {{
    val uiState by viewModel.uiState.collectAsState()
    // TODO: build UI
}}
"""

def model_stub(name: str) -> str:
    return f"""\
package app.webs.android.domain.model

// {name} — domain model
// Mapped from proto-generated type; decoupled for Room persistence
data class {name}(
    val id: String = "",
    // TODO: fields
)
"""

def entity_stub(name: str) -> str:
    return f"""\
package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// {name}Entity — Room entity for offline-first {name.lower()} cache
@Entity(tableName = "{name.lower()}s")
data class {name}Entity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
"""

def dao_stub(name: str) -> str:
    return f"""\
package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.{name}Entity

@Dao
interface {name}Dao {{
    @Query("SELECT * FROM {name.lower()}s")
    fun getAll(): Flow<List<{name}Entity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<{name}Entity>)

    @Query("DELETE FROM {name.lower()}s")
    suspend fun clear()

    // TODO: additional queries
}}
"""

def grpc_stub(name: str) -> str:
    return f"""\
package app.webs.android.data.remote.grpc

// {name}GrpcClient — wraps the generated proto stub for {name.lower()}
// Inject via Hilt; swap for fake in tests
class {name}GrpcClient(
    // TODO: inject ManagedChannel
) {{
    // TODO: implement suspend / Flow methods wrapping the generated stub
}}
"""

def repo_stub(name: str) -> str:
    return f"""\
package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface {name}Repository {{
    // TODO: define repository contract
}}

class {name}RepositoryImpl(
    // TODO: inject {name}GrpcClient + {name}Dao
) : {name}Repository {{
    // TODO: implement — emit from Room, sync from gRPC in background
}}
"""

def worker_stub(name: str) -> str:
    return f"""\
package app.webs.android.data.worker

import android.content.Context
import androidx.hilt.work.HiltWorker
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import dagger.assisted.Assisted
import dagger.assisted.AssistedInject

// {name}Worker — background sync / upload via WorkManager
@HiltWorker
class {name}Worker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    // TODO: inject dependencies
) : CoroutineWorker(context, params) {{
    override suspend fun doWork(): Result {{
        // TODO: implement
        return Result.success()
    }}
}}
"""

def component_stub(name: str) -> str:
    return f"""\
package app.webs.android.ui.components

import androidx.compose.runtime.Composable

// {name} — shared UI component
@Composable
fun {name}() {{
    // TODO: implement
}}
"""

# ── Scaffold ───────────────────────────────────────────────────────────────────

def scaffold():
    base = "webs-android"
    src  = f"{base}/app/src/main/kotlin/app/webs/android"
    test = f"{base}/app/src/test/kotlin/app/webs/android"
    res  = f"{base}/app/src/main/res"

    print(f"\n🕸  Scaffolding {base}/\n")

    # ── Gradle / build ─────────────────────────────────────────────────────────
    write(f"{base}/settings.gradle.kts",                    SETTINGS_GRADLE)
    write(f"{base}/build.gradle.kts",                       BUILD_GRADLE_ROOT)
    write(f"{base}/app/build.gradle.kts",                   BUILD_GRADLE_APP)
    write(f"{base}/gradle/libs.versions.toml",              LIBS_VERSIONS_TOML)
    touch(f"{base}/gradle/wrapper/gradle-wrapper.properties")
    touch(f"{base}/local.properties")
    touch(f"{base}/.gitignore")

    # ── Manifest ───────────────────────────────────────────────────────────────
    write(f"{base}/app/src/main/AndroidManifest.xml",       MANIFEST)

    # ── App entry points ───────────────────────────────────────────────────────
    write(f"{src}/MainActivity.kt",                         MAIN_ACTIVITY)
    write(f"{src}/WebsApplication.kt",                      WEBS_APPLICATION)

    # ── Navigation ─────────────────────────────────────────────────────────────
    write(f"{src}/navigation/WebsNavHost.kt",               NAV_HOST)
    write(f"{src}/navigation/Destination.kt",               NAV_DESTINATIONS)

    # ── Theme ──────────────────────────────────────────────────────────────────
    write(f"{src}/ui/theme/WebsTheme.kt",                   WEBS_THEME)
    write(f"{src}/ui/theme/WebsTypography.kt",              WEBS_TYPE)
    write(f"{src}/ui/theme/WebsColors.kt",                  WEBS_COLOR)
    write(f"{src}/ui/theme/WebsShapes.kt",
          "package app.webs.android.ui.theme\n// TODO: Webs shape tokens\n")

    # ── Main scaffold ──────────────────────────────────────────────────────────
    write(f"{src}/ui/MainScaffold.kt",                      MAIN_SCAFFOLD)

    # ── Screens + ViewModels ───────────────────────────────────────────────────
    screens = {
        "Splash":        "Initial loading / session check",
        "Onboarding":    "First-run onboarding flow",
        "Login":         "Email / social login",
        "SignUp":        "New account creation",
        "Home":          "For You / Following / Trending feed",
        "Discover":      "Search, trending, follow suggestions",
        "Spins":         "Full-screen vertical video feed",
        "PostDetail":    "Single Web detail + comments",
        "CreatePost":    "Compose a Web — text, images, circle tag",
        "CreateSpin":    "Record or upload a Spin",
        "Circles":       "My Circles + Explore tab",
        "CircleDetail":  "Single Circle feed and about page",
        "Stories":       "Full-screen story viewer",
        "Profile":       "Own and other user profiles — Webs + Spins tabs",
        "EditProfile":   "Edit display name, bio, avatar, banner",
        "Messages":      "DM inbox list",
        "Conversation":  "1:1 and group message thread",
        "Activity":      "Activity feed — replies, follows, reactions",
        "Settings":      "Account, privacy, notifications, theme",
    }

    for name, desc in screens.items():
        write(f"{src}/ui/{name.lower()}/{name}Screen.kt",
              screen_stub(f"{name}Screen"))
        write(f"{src}/ui/{name.lower()}/{name}ViewModel.kt",
              viewmodel_stub(name, desc))

    # ── Shared UI components ───────────────────────────────────────────────────
    components = [
        "WebCard",
        "SpinPlayer",
        "AvatarView",
        "StoryRing",
        "StoriesBar",
        "CirclePill",
        "FloatingNavBar",
        "ComposeButton",
        "FollowButton",
        "ReactionBar",
        "UserRow",
        "EmptyState",
        "LoadingSpinner",
        "VerifiedBadge",
    ]
    for c in components:
        write(f"{src}/ui/components/{c}.kt", component_stub(c))

    # ── Domain models ──────────────────────────────────────────────────────────
    models = ["User", "Post", "Spin", "Circle", "Story",
              "Message", "Conversation", "ActivityItem", "SearchResult"]
    for m in models:
        write(f"{src}/domain/model/{m}.kt", model_stub(m))

    # ── Domain use cases ───────────────────────────────────────────────────────
    usecases = [
        ("GetFeedUseCase",           "feed"),
        ("GetPostUseCase",           "post"),
        ("CreatePostUseCase",        "post"),
        ("ReactToPostUseCase",       "post"),
        ("GetSpinsFeedUseCase",      "spin"),
        ("UploadSpinUseCase",        "spin"),
        ("GetProfileUseCase",        "profile"),
        ("FollowUserUseCase",        "profile"),
        ("GetCirclesUseCase",        "circle"),
        ("JoinCircleUseCase",        "circle"),
        ("GetStoriesUseCase",        "story"),
        ("SendMessageUseCase",       "message"),
        ("GetActivityUseCase",       "activity"),
        ("SearchUseCase",            "search"),
        ("LoginUseCase",             "auth"),
        ("SignUpUseCase",            "auth"),
        ("RefreshTokenUseCase",      "auth"),
    ]
    for cls, pkg in usecases:
        write(f"{src}/domain/usecase/{cls}.kt",
              f"package app.webs.android.domain.usecase\n// TODO: {cls}\n")

    # ── Room database ──────────────────────────────────────────────────────────
    write(f"{src}/data/local/WebsDatabase.kt",
          "package app.webs.android.data.local\n// TODO: @Database declaration listing all entities\n")

    entities = ["Post", "Spin", "Circle", "Story", "User", "ActivityItem", "Message"]
    for e in entities:
        write(f"{src}/data/local/entity/{e}Entity.kt", entity_stub(e))
        write(f"{src}/data/local/dao/{e}Dao.kt",       dao_stub(e))

    # ── gRPC clients ───────────────────────────────────────────────────────────
    grpc_clients = ["Auth", "Feed", "Post", "Spins", "Profile",
                    "Circles", "Stories", "Messages", "Activity", "Search"]
    for g in grpc_clients:
        write(f"{src}/data/remote/grpc/{g}GrpcClient.kt", grpc_stub(g))

    write(f"{src}/data/remote/grpc/GrpcChannelProvider.kt",
          "package app.webs.android.data.remote.grpc\n// TODO: Hilt provider for ManagedChannel — TLS, keepalive, auth interceptor\n")
    write(f"{src}/data/remote/grpc/AuthInterceptor.kt",
          "package app.webs.android.data.remote.grpc\n// TODO: ClientInterceptor that attaches Bearer JWT to every gRPC call\n")

    # ── Repositories ───────────────────────────────────────────────────────────
    repos = ["Auth", "Feed", "Post", "Spin", "Profile",
             "Circle", "Story", "Message", "Activity", "Search"]
    for r in repos:
        write(f"{src}/data/repository/{r}Repository.kt", repo_stub(r))

    # ── Workers ────────────────────────────────────────────────────────────────
    workers = ["FeedSync", "PostUpload", "SpinUpload", "ActivitySync"]
    for w in workers:
        write(f"{src}/data/worker/{w}Worker.kt", worker_stub(w))

    # ── DI modules ─────────────────────────────────────────────────────────────
    modules = ["DatabaseModule", "GrpcModule", "RepositoryModule",
               "UseCaseModule", "WorkerModule"]
    for mod in modules:
        write(f"{src}/di/{mod}.kt",
              f"package app.webs.android.di\n\nimport dagger.Module\nimport dagger.hilt.InstallIn\nimport dagger.hilt.components.SingletonComponent\n\n@Module\n@InstallIn(SingletonComponent::class)\nobject {mod} {{\n    // TODO: provide bindings\n}}\n")

    # ── DataStore (settings + tokens) ─────────────────────────────────────────
    write(f"{src}/data/datastore/TokenDataStore.kt",
          "package app.webs.android.data.datastore\n// TODO: DataStore<Preferences> for JWT + refresh token\n")
    write(f"{src}/data/datastore/SettingsDataStore.kt",
          "package app.webs.android.data.datastore\n// TODO: DataStore<Preferences> for theme, language, etc.\n")

    # ── Generated proto stubs ──────────────────────────────────────────────────
    proto_files = ["auth", "feed", "post", "spins", "profile",
                   "circles", "stories", "messages", "activity", "search"]
    for p in proto_files:
        touch(f"{src}/generated/{p}.pb.kt")
        touch(f"{src}/generated/{p}Grpc.kt")

    write(f"{src}/generated/README.md",
          "# Generated\nDo not edit. Run `buf generate` from the `proto/` directory to regenerate.\n")

    # ── Resources ──────────────────────────────────────────────────────────────
    touch(f"{res}/values/strings.xml")
    touch(f"{res}/values/themes.xml")
    touch(f"{res}/drawable/ic_launcher_foreground.xml")
    touch(f"{res}/mipmap-anydpi/ic_launcher.xml")

    # ── Tests ──────────────────────────────────────────────────────────────────
    test_targets = ["Auth", "Feed", "Post", "Profile", "Activity",
                    "Circles", "Repository", "ViewModel"]
    for t in test_targets:
        write(f"{test}/{t.lower()}/{t}Test.kt",
              f"package app.webs.android.{t.lower()}\n// TODO: unit tests — {t}\n")

    print(f"\n✅  Done. Open webs-android/ in Android Studio and sync Gradle.\n")

# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    scaffold()
