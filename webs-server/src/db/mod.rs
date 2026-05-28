use surrealdb::{engine::remote::ws::Client, Surreal};
use crate::config::DatabaseConfig;

pub type Db = Surreal<Client>;

pub async fn connect(_cfg: &DatabaseConfig) -> anyhow::Result<Db> {
    // TODO: connect to SurrealDB, sign in, set NS/DB
    todo!("implement db::connect")
}
