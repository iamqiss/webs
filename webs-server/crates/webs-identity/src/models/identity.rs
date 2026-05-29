use crate::types::Wid;
#[derive(serde::Serialize, serde::Deserialize, Debug)]
pub struct Identity { pub wid: Wid, pub name: String, pub verified: bool }
