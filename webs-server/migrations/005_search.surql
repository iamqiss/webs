DEFINE TABLE search_index SCHEMALESS;

DEFINE INDEX content_search
ON search_index FIELDS content
SEARCH ANALYZER ascii BM25;
