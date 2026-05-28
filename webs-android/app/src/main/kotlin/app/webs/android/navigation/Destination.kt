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
