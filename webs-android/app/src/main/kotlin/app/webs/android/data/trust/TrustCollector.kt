package app.webs.android.data.trust

import app.webs.android.domain.model.*

class TrustCollector {

    private var screenEnteredMs = System.currentTimeMillis()
    private val keystrokeTimestamps = mutableListOf<Long>()
    private var backspaceCount = 0
    private var scrollEvents = 0
    private var hasTouchedOutside = false
    private val fieldFocusOrder = mutableListOf<String>()

    fun onScreenEnter() { screenEnteredMs = System.currentTimeMillis() }
    fun onScroll() { scrollEvents++ }
    fun onTouchOutside() { hasTouchedOutside = true }
    fun onFieldFocus(fieldName: String) { fieldFocusOrder.add(fieldName) }
    fun onBackspace() { backspaceCount++ }
    fun onKeystroke() { keystrokeTimestamps.add(System.currentTimeMillis()) }

    fun collect(
        deviceFingerprint: String,
        isEmulator: Boolean,
        installSource: String,
        androidVersion: Int,
        emoPat: EmoPatSignals? = null,
    ): TrustSignals {
        val intervals = keystrokeTimestamps.zipWithNext { a, b -> b - a }
        val avgDelay = if (intervals.isEmpty()) 0L else intervals.average().toLong()
        val variance = if (intervals.size < 2) 0f else {
            val mean = intervals.average()
            intervals.map { (it - mean).toFloat().pow(2) }.average().toFloat().let { kotlin.math.sqrt(it) }
        }

        return TrustSignals(
            deviceFingerprint = deviceFingerprint,
            isEmulator = isEmulator,
            installSource = installSource,
            androidVersion = androidVersion,
            avgKeystrokeDelayMs = avgDelay,
            keystrokeVariance = variance,
            backspaceCount = backspaceCount,
            totalTypingMs = if (keystrokeTimestamps.size < 2) 0L else keystrokeTimestamps.last() - keystrokeTimestamps.first(),
            fieldFocusOrder = fieldFocusOrder.toList(),
            timeOnScreenMs = System.currentTimeMillis() - screenEnteredMs,
            scrollEvents = scrollEvents,
            hasTouchedOutside = hasTouchedOutside,
            emoPat = emoPat
        )
    }

    fun score(signals: TrustSignals): TrustScore {
        var score = 1.0f
        val flags = mutableListOf<TrustFlag>()

        if (signals.isEmulator) { score -= 0.5f; flags.add(TrustFlag.EMULATOR_DETECTED) }
        if (signals.installSource == "sideload") { score -= 0.2f; flags.add(TrustFlag.SIDELOADED) }
        if (signals.timeOnScreenMs < 3000) { score -= 0.3f; flags.add(TrustFlag.TOO_FAST) }
        if (signals.avgKeystrokeDelayMs in 1..30) { score -= 0.25f; flags.add(TrustFlag.UNIFORM_KEYSTROKES) }
        if (signals.keystrokeVariance < 5f && signals.totalTypingMs > 0) { score -= 0.2f; flags.add(TrustFlag.UNIFORM_KEYSTROKES) }
        if (signals.backspaceCount == 0 && signals.totalTypingMs > 1000) { score -= 0.1f; flags.add(TrustFlag.NO_TYPOS) }
        if (!signals.hasTouchedOutside) { score -= 0.05f; flags.add(TrustFlag.NO_OUTSIDE_TAPS) }

        signals.emoPat?.let { ep ->
            if (!ep.passed) { score -= 0.4f; flags.add(TrustFlag.EMOPAT_FAILED) }
            val avgTap = ep.tapIntervals.average()
            if (avgTap < 80) { score -= 0.25f; flags.add(TrustFlag.EMOPAT_TOO_FAST) }
            val tapVar = ep.tapIntervals.map { (it - avgTap).pow(2) }.average()
            if (tapVar < 100) { score -= 0.2f; flags.add(TrustFlag.EMOPAT_UNIFORM_TAPS) }
        }

        score = score.coerceIn(0f, 1f)

        val action = when {
            score >= 0.70f -> TrustAction.ALLOW
            score >= 0.45f -> TrustAction.RTC
            score >= 0.20f -> TrustAction.SOFT_BLOCK
            else -> TrustAction.HARD_BLOCK
        }

        return TrustScore(score, flags.distinct(), action)
    }
}