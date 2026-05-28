use serde::Deserialize;

#[derive(Debug, Deserialize)]
pub struct Settings {
    pub server:   ServerConfig,
    pub database: DatabaseConfig,
    pub auth:     AuthConfig,
}

#[derive(Debug, Deserialize)]
pub struct ServerConfig {
    pub addr: String,
}

#[derive(Debug, Deserialize)]
pub struct DatabaseConfig {
    pub url:       String,
    pub namespace: String,
    pub database:  String,
    pub username:  String,
    pub password:  String,
}

#[derive(Debug, Deserialize)]
pub struct AuthConfig {
    pub jwt_secret:          String,
    pub access_token_expiry:  u64,
    pub refresh_token_expiry: u64,
}

impl Settings {
    pub fn load() -> anyhow::Result<Self> {
        dotenvy::dotenv().ok();
        // TODO: load from config file + env overrides
        todo!("implement Settings::load")
    }
}
