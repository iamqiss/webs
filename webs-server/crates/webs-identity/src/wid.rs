pub fn generate_wid() -> String { format!("wid:webs:{}", uuid::Uuid::new_v4()) }
