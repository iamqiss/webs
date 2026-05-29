use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TrustSignal {
    pub device_id: String,
    pub tap_variance: f32,
    pub typing_variance: f32,
    pub suspicious: bool,
}

pub struct RtcEngine;

impl RtcEngine {
    pub fn evaluate(signal: &TrustSignal) -> bool {
        signal.suspicious
    }
}
