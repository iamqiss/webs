package app.webs.android.domain.model

data class TrustSignal(
    val typingSpeed: Float,
    val pressure: Float,
    val rhythm: Float,
    val timestamp: Long = System.currentTimeMillis()
)
