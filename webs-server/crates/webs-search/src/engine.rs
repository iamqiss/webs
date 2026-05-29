pub struct SearchQuery {
    pub text: String,
    pub latitude: Option<f64>,
    pub longitude: Option<f64>,
}

pub struct SearchResult {
    pub wid: String,
    pub relevance: f32,
}

pub struct SearchEngine;

impl SearchEngine {
    pub async fn search(_query: SearchQuery) -> Vec<SearchResult> {
        vec![]
    }
}
