use anyhow::Result;
#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::fmt().init();
    tracing::info!("🚀 Webs Server starting");
    bootstrap().await
}
async fn bootstrap() -> Result<()> {
    // TODO: initialize config, db, services, grpc server
    Ok(())
}
