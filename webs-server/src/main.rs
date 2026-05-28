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
