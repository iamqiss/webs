package app.webs.android.domain.model

import androidx.compose.ui.geometry.Offset

data class TrustSignals(
    val deviceFingerprint: String = "",
    val isEmulator: Boolean = false,
    val installSource: String = "",
    val androidVersion: Int = 0,

    // Typing behavior
    val avgKeystrokeDelayMs: Long = 0L,
    val keystrokeVariance: Float = 0f,
    val backspaceCount: Int = 0,
    val totalTypingMs: Long = 0L,

    // Session behavior
    val fieldFocusOrder: List<String> = emptyList(),
    val timeOnScreenMs: Long = 0L,
    val scrollEvents: Int = 0,
    val hasTouchedOutside: Boolean = false,

    // EmoPat telemetry
    val emoPat: EmoPatSignals? = null,
)

data class EmoPatSignals(
    val challengeId: String,
    val challengeType: String,
    val tapTimestampsMs: List<Long>,
    val tapIntervals: List<Long>,
    val tapPositions: List<Offset>,
    val tapDistances: List<Float>,
    val durationMs: Long,
    val passed: Boolean,
    val attempts: Int,
)