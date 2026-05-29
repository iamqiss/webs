pub struct IdentityRepo;
impl IdentityRepo {
    pub async fn find_by_wid(&self, wid: &str) -> anyhow::Result<Option<crate::models::identity::Identity>> {
        todo!("SurrealDB query")
    }
}
