use std::net::SocketAddr;

pub async fn serve(_addr: SocketAddr) -> anyhow::Result<()> {
    // TODO: build tonic Server, register all services, serve with TLS
    todo!("implement grpc::serve")
}
