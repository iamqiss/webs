DEFINE TABLE session SCHEMAFULL;

DEFINE FIELD wid ON session TYPE string;
DEFINE FIELD refresh_hash ON session TYPE string;
DEFINE FIELD device_id ON session TYPE string;
DEFINE FIELD created_at ON session TYPE datetime;
DEFINE FIELD expires_at ON session TYPE datetime;
