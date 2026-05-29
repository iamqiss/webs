package app.webs.android.domain.model

data class TrustScore(
    val score: Float,
    val flags: List<TrustFlag>,
    val action: TrustAction,
)

enum class TrustAction {
    ALLOW, RTC, SOFT_BLOCK, HARD_BLOCK
}

enum class TrustFlag {
    EMULATOR_DETECTED,
    SIDELOADED,
    TOO_FAST,
    UNIFORM_KEYSTROKES,
    NO_TYPOS,
    NO_SCROLL,
    NO_OUTSIDE_TAPS,
    EMOPAT_FAILED,
    EMOPAT_TOO_FAST,
    EMOPAT_UNIFORM_TAPS,
}