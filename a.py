#!/usr/bin/env python3
"""
scaffold_webs_server.py
Scaffolds the webs-server Rust project file tree.
Run from the root of the webs monorepo:
    python3 scaffold_webs_server.py
"""

import os

# ── Helpers ────────────────────────────────────────────────────────────────────

def write(path: str, content: str = "") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")

def touch(path: str) -> None:
    write(path, "")

# ── File contents ──────────────────────────────────────────────────────────────

CARGO_TOML = """\
[package]
name    = "webs-server"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "webs-server"
path = "src/main.rs"

[dependencies]
# async runtime
tokio       = { version = "1", features = ["full"] }

# gRPC
tonic       = "0.11"
prost       = "0.12"

# database
surrealdb   = "2"

# serialization
serde       = { version = "1", features = ["derive"] }
serde_json  = "1"

# auth
jsonwebtoken = "9"
bcrypt       = "0.15"

# config & env
dotenvy     = "0.15"
config      = "0.14"

# logging / tracing
tracing             = "0.1"
tracing-subscriber  = { version = "0.3", features = ["env-filter"] }

# error handling
thiserror   = "1"
anyhow      = "1"

# utilities
uuid        = { version = "1", features = ["v4"] }
chrono      = { version = "0.4", features = ["serde"] }

[build-dependencies]
tonic-build = "0.11"
"""

BUILD_RS = """\
fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Compile all .proto files from the shared proto/ directory.
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .compile(
            &[
                "../proto/auth.proto",
                "../proto/feed.proto",
                "../proto/post.proto",
                "../proto/spins.proto",
                "../proto/profile.proto",
                "../proto/circles.proto",
                "../proto/stories.proto",
                "../proto/messages.proto",
                "../proto/activity.proto",
                "../proto/search.proto",
            ],
            &["../proto"],
        )?;
    Ok(())
}
"""

MAIN_RS = """\
mod config;
mod db;
mod error;
mod auth;
mod grpc;
mod models;
mod services;

use tracing::info;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    // Initialise tracing
    tracing_subscriber::fmt::init();

    // Load config
    let cfg = config::Settings::load()?;
    info!("Starting webs-server on {}", cfg.server.addr);

    // Connect to SurrealDB
    let _db = db::connect(&cfg.database).await?;

    // Start gRPC server
    grpc::serve(cfg.server.addr.parse()?).await?;

    Ok(())
}
"""

CONFIG_MOD = """\
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
"""

DB_MOD = """\
use surrealdb::{engine::remote::ws::Client, Surreal};
use crate::config::DatabaseConfig;

pub type Db = Surreal<Client>;

pub async fn connect(_cfg: &DatabaseConfig) -> anyhow::Result<Db> {
    // TODO: connect to SurrealDB, sign in, set NS/DB
    todo!("implement db::connect")
}
"""

ERROR_RS = """\
use thiserror::Error;

#[derive(Debug, Error)]
pub enum AppError {
    #[error("not found: {0}")]
    NotFound(String),

    #[error("unauthorized")]
    Unauthorized,

    #[error("forbidden")]
    Forbidden,

    #[error("bad request: {0}")]
    BadRequest(String),

    #[error("internal error: {0}")]
    Internal(String),

    #[error(transparent)]
    Database(#[from] surrealdb::Error),

    #[error(transparent)]
    Unexpected(#[from] anyhow::Error),
}
"""

AUTH_MOD = """\
// auth/mod.rs — re-exports auth sub-modules
pub mod jwt;
pub mod password;
pub mod middleware;
"""

AUTH_JWT = """\
// TODO: JWT generation, validation, and refresh token logic
"""

AUTH_PASSWORD = """\
// TODO: bcrypt hashing and verification helpers
"""

AUTH_MIDDLEWARE = """\
// TODO: tonic interceptor for validating Bearer tokens on incoming gRPC calls
"""

GRPC_MOD = """\
// grpc/mod.rs — wires up all gRPC service handlers
pub mod router;
pub mod auth;
pub mod feed;
pub mod post;
pub mod spins;
pub mod profile;
pub mod circles;
pub mod stories;
pub mod messages;
pub mod activity;
pub mod search;
"""

GRPC_ROUTER = """\
use std::net::SocketAddr;

pub async fn serve(_addr: SocketAddr) -> anyhow::Result<()> {
    // TODO: build tonic Server, register all services, serve with TLS
    todo!("implement grpc::serve")
}
"""

MODELS_MOD = """\
pub mod user;
pub mod post;
pub mod spin;
pub mod circle;
pub mod story;
pub mod message;
pub mod activity;
"""

SERVICES_MOD = """\
pub mod auth;
pub mod feed;
pub mod post;
pub mod spin;
pub mod profile;
pub mod circle;
pub mod story;
pub mod message;
pub mod activity;
pub mod search;
"""

ENV_EXAMPLE = """\
# Server
SERVER_ADDR=0.0.0.0:50051

# SurrealDB
DATABASE_URL=ws://localhost:8000
DATABASE_NAMESPACE=webs
DATABASE_DATABASE=prod
DATABASE_USERNAME=root
DATABASE_PASSWORD=root

# Auth
AUTH_JWT_SECRET=change_me_in_production
AUTH_ACCESS_TOKEN_EXPIRY=900
AUTH_REFRESH_TOKEN_EXPIRY=2592000
"""

GITIGNORE = """\
/target
.env
*.pem
*.key
"""

# ── Scaffold definition ────────────────────────────────────────────────────────

def scaffold():
    base = "webs-server"
    print(f"\n🕸  Scaffolding {base}/\n")

    # ── Root files ─────────────────────────────────────────────────────────────
    write(f"{base}/Cargo.toml",    CARGO_TOML)
    write(f"{base}/build.rs",      BUILD_RS)
    write(f"{base}/.env.example",  ENV_EXAMPLE)
    write(f"{base}/.gitignore",    GITIGNORE)

    # ── src/ ───────────────────────────────────────────────────────────────────
    write(f"{base}/src/main.rs",   MAIN_RS)
    write(f"{base}/src/error.rs",  ERROR_RS)

    # config
    write(f"{base}/src/config/mod.rs",  CONFIG_MOD)

    # db
    write(f"{base}/src/db/mod.rs",      DB_MOD)
    touch(f"{base}/src/db/migrations.rs")

    # auth
    write(f"{base}/src/auth/mod.rs",        AUTH_MOD)
    write(f"{base}/src/auth/jwt.rs",         AUTH_JWT)
    write(f"{base}/src/auth/password.rs",    AUTH_PASSWORD)
    write(f"{base}/src/auth/middleware.rs",  AUTH_MIDDLEWARE)

    # grpc
    write(f"{base}/src/grpc/mod.rs",         GRPC_MOD)
    write(f"{base}/src/grpc/router.rs",      GRPC_ROUTER)
    for svc in ["auth", "feed", "post", "spins", "profile",
                "circles", "stories", "messages", "activity", "search"]:
        write(f"{base}/src/grpc/{svc}.rs",
              f"// TODO: gRPC handler — {svc} service\n")

    # models
    write(f"{base}/src/models/mod.rs", MODELS_MOD)
    for model in ["user", "post", "spin", "circle", "story", "message", "activity"]:
        write(f"{base}/src/models/{model}.rs",
              f"// TODO: {model} model — SurrealDB record struct + impl\n")

    # services (business logic layer)
    write(f"{base}/src/services/mod.rs", SERVICES_MOD)
    for svc in ["auth", "feed", "post", "spin", "profile",
                "circle", "story", "message", "activity", "search"]:
        write(f"{base}/src/services/{svc}.rs",
              f"// TODO: {svc} service — business logic between gRPC handler and DB\n")

    # ── migrations/ ────────────────────────────────────────────────────────────
    for mig in [
        "001_users.surql",
        "002_posts.surql",
        "003_spins.surql",
        "004_circles.surql",
        "005_stories.surql",
        "006_messages.surql",
        "007_activity.surql",
        "008_follows.surql",
        "009_reactions.surql",
    ]:
        write(f"{base}/migrations/{mig}",
              f"-- TODO: SurrealDB schema migration — {mig}\n")

    # ── tests/ ─────────────────────────────────────────────────────────────────
    for test in ["auth", "feed", "post", "profile", "activity"]:
        write(f"{base}/tests/{test}_tests.rs",
              f"// TODO: integration tests — {test}\n")

    print(f"\n✅  Done. Open webs-server/ in your editor and run:\n")
    print(f"    cd webs-server && cargo check\n")

# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    scaffold()
