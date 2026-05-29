use thiserror::Error;
#[derive(Error, Debug)]
pub enum AppError {
    #[error("db error")]
    Database(#[from] surrealdb::Error),
    #[error("auth failed")]
    Unauthorized,
    #[error("{0}")]
    Validation(String),
}
