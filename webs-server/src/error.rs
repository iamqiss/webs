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
