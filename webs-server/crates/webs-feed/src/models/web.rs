#[derive(serde::Serialize, serde::Deserialize)]
pub struct Web { pub id: String, pub author_wid: crate::types::Wid, pub content: String, pub created_at: crate::types::Timestamp }
