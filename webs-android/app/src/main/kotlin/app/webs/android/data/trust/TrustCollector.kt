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
