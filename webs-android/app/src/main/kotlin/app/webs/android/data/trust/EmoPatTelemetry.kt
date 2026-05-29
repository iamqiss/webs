package app.webs.android.data.trust

import androidx.compose.ui.geometry.Offset
import app.webs.android.domain.model.EmoPatSignals

class EmoPatTelemetry {
    private var challengeId = ""
    private var startMs = 0L
    private val tapTimestamps = mutableListOf<Long>()
    private val tapPositions = mutableListOf<Offset>()
    private var attempts = 0

    fun onChallengeStart(id: String, timestampMs: Long) {
        challengeId = id
        startMs = timestampMs
        tapTimestamps.clear()
        tapPositions.clear()
    }

    fun onTap(emoji: String, position: Offset, timestampMs: Long) {
        tapTimestamps.add(timestampMs)
        tapPositions.add(position)
    }

    fun onChallengeEnd(
        challengeId: String,
        passed: Boolean,
        taps: List<String>,
        timestampMs: Long
    ): EmoPatSignals {
        if (!passed) attempts++

        val intervals = tapTimestamps.zipWithNext { a, b -> b - a }
        val distances = tapPositions.zipWithNext { a, b ->
            kotlin.math.sqrt((b.x - a.x).pow(2) + (b.y - a.y).pow(2))
        }

        return EmoPatSignals(
            challengeId = challengeId,
            challengeType = "",
            tapTimestampsMs = tapTimestamps.toList(),
            tapIntervals = intervals,
            tapPositions = tapPositions.toList(),
            tapDistances = distances,
            durationMs = timestampMs - startMs,
            passed = passed,
            attempts = attempts
        )
    }

    fun reset() {
        challengeId = ""
        startMs = 0L
        attempts = 0
        tapTimestamps.clear()
        tapPositions.clear()
    }
}