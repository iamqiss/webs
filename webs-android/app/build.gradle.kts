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
