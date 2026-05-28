package app.webs.android.data.trust

import app.webs.android.domain.model.TrustSignal
import kotlin.math.abs

class EmoPatEngine {

    fun score(
        signal: TrustSignal,
        baselineSpeed: Float,
        baselinePressure: Float
    ): Float {

        val speedDelta = abs(signal.typingSpeed - baselineSpeed)
        val pressureDelta = abs(signal.pressure - baselinePressure)

        return (1f - (speedDelta + pressureDelta) / 2f)
            .coerceIn(0f, 1f)
    }
}
