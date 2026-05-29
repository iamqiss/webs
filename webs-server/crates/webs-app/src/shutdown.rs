pub async fn graceful() { tokio::signal::ctrl_c().await.ok(); }
