#!/usr/bin/env python3
"""
scaffold_webs_proto.py
Scaffolds the shared proto/ directory for the Webs monorepo.
Run from the root of the webs monorepo:
    python3 scaffold_webs_proto.py
"""

import os

# ── Helpers ────────────────────────────────────────────────────────────────────

def write(path: str, content: str = "") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"  created  {path}")

def touch(path: str) -> None:
    write(path, "")

# ── buf.yaml ──────────────────────────────────────────────────────────────────

BUF_YAML = """\
version: v2
modules:
  - path: .
lint:
  use:
    - DEFAULT
  except:
    - PACKAGE_VERSION_SUFFIX
breaking:
  use:
    - FILE
"""

BUF_GEN_YAML = """\
version: v2
plugins:
  # Rust (tonic / prost)
  - remote: buf.build/community/neoeinstein-prost
    out: ../webs-server/src/generated
    opt:
      - file_descriptor_set=false

  - remote: buf.build/community/neoeinstein-tonic
    out: ../webs-server/src/generated
    opt:
      - compile_well_known_types=true
      - extern_path=.google.protobuf=::pbjson_types

  # Swift (grpc-swift / swift-protobuf)
  - remote: buf.build/grpc/swift
    out: ../webs-ios/WebsApp/Generated

  - remote: buf.build/apple/swift
    out: ../webs-ios/WebsApp/Generated

  # Kotlin (grpc-kotlin / protobuf-kotlin-lite)
  - remote: buf.build/grpc/kotlin
    out: ../webs-android/app/src/main/kotlin/app/webs/android/generated

  - remote: buf.build/protocolbuffers/kotlin
    out: ../webs-android/app/src/main/kotlin/app/webs/android/generated
    opt:
      - lite
"""

COMMON_PROTO = """\
syntax = "proto3";
package webs.common.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "google/protobuf/timestamp.proto";

// Pagination

message PageRequest {
  string cursor = 1; // opaque cursor from previous response
  int32  limit  = 2; // max items; server may cap
}

message PageInfo {
  string next_cursor = 1; // empty = end of feed
  bool   has_more    = 2;
}

// Media

message MediaItem {
  string    url          = 1;
  string    thumbnail    = 2;
  MediaType type         = 3;
  int32     width        = 4;
  int32     height       = 5;
  int32     duration_sec = 6; // video only
}

enum MediaType {
  MEDIA_TYPE_UNSPECIFIED = 0;
  MEDIA_TYPE_IMAGE       = 1;
  MEDIA_TYPE_VIDEO       = 2;
}

// Embedded user summary (used inside posts, comments, activity, etc.)

message UserSummary {
  string id           = 1;
  string username     = 2;
  string display_name = 3;
  string avatar_url   = 4;
  bool   verified     = 5;
}

// Reactions

message ReactionCounts {
  int64 likes     = 1;
  int64 dislikes  = 2;
  int64 comments  = 3;
  int64 reshares  = 4;
  int64 bookmarks = 5;
}

// Empty placeholder

message Empty {}
"""

AUTH_PROTO = """\
syntax = "proto3";
package webs.auth.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "google/protobuf/timestamp.proto";

service AuthService {
  rpc SignUp        (SignUpRequest)       returns (AuthResponse);
  rpc Login         (LoginRequest)        returns (AuthResponse);
  rpc RefreshToken  (RefreshTokenRequest) returns (AuthResponse);
  rpc Logout        (LogoutRequest)       returns (LogoutResponse);
  rpc CheckUsername (CheckUsernameRequest) returns (CheckUsernameResponse);
}

message SignUpRequest {
  string email        = 1;
  string username     = 2;
  string display_name = 3;
  string password     = 4;
}

message LoginRequest {
  string identifier = 1; // email or username
  string password   = 2;
}

message RefreshTokenRequest { string refresh_token = 1; }

message LogoutRequest  { string refresh_token = 1; }
message LogoutResponse { bool   success        = 1; }

message CheckUsernameRequest  { string username   = 1; }
message CheckUsernameResponse { bool   available  = 1; }

message AuthResponse {
  string                    access_token  = 1;
  string                    refresh_token = 2;
  google.protobuf.Timestamp expires_at    = 3;
  UserAuth                  user          = 4;
}

message UserAuth {
  string id           = 1;
  string username     = 2;
  string display_name = 3;
  string avatar_url   = 4;
  bool   verified     = 5;
}
"""

FEED_PROTO = """\
syntax = "proto3";
package webs.feed.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "post.proto";

service FeedService {
  // Server-streaming — new Webs pushed as they arrive
  rpc StreamForYou     (FeedRequest)      returns (stream FeedEvent);
  rpc StreamFollowing  (FeedRequest)      returns (stream FeedEvent);
  rpc StreamTrending   (FeedRequest)      returns (stream FeedEvent);
  rpc StreamCircleFeed (CircleFeedRequest) returns (stream FeedEvent);
}

message FeedRequest {
  webs.common.v1.PageRequest page = 1;
}

message CircleFeedRequest {
  string                     circle_id = 1;
  webs.common.v1.PageRequest page      = 2;
}

message FeedEvent {
  oneof event {
    webs.post.v1.Post new_post  = 1;
    string            delete_id = 2; // post removed — drop from local feed
    FeedPage          page      = 3; // initial page burst
  }
}

message FeedPage {
  repeated webs.post.v1.Post posts = 1;
  webs.common.v1.PageInfo    page  = 2;
}
"""

POST_PROTO = """\
syntax = "proto3";
package webs.post.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service PostService {
  rpc CreatePost    (CreatePostRequest)    returns (Post);
  rpc GetPost       (GetPostRequest)       returns (Post);
  rpc DeletePost    (DeletePostRequest)    returns (webs.common.v1.Empty);
  rpc ReactToPost   (ReactRequest)         returns (webs.common.v1.ReactionCounts);
  rpc BookmarkPost  (BookmarkRequest)      returns (webs.common.v1.Empty);
  rpc ResharePost   (ReshareRequest)       returns (Post);
  rpc GetComments   (GetCommentsRequest)   returns (stream Comment);
  rpc AddComment    (AddCommentRequest)    returns (Comment);
  rpc DeleteComment (DeleteCommentRequest) returns (webs.common.v1.Empty);
}

message Post {
  string                            id          = 1;
  webs.common.v1.UserSummary        author      = 2;
  string                            body        = 3;
  repeated webs.common.v1.MediaItem media       = 4;
  string                            circle_id   = 5;
  string                            category    = 6;
  webs.common.v1.ReactionCounts     reactions   = 7;
  bool                              bookmarked  = 8;
  bool                              reshared    = 9;
  string                            reshare_of  = 10;
  google.protobuf.Timestamp         created_at  = 11;
}

message Comment {
  string                            id          = 1;
  webs.common.v1.UserSummary        author      = 2;
  string                            body        = 3;
  repeated webs.common.v1.MediaItem media       = 4;
  webs.common.v1.ReactionCounts     reactions   = 5;
  google.protobuf.Timestamp         created_at  = 6;
}

message CreatePostRequest {
  string          body       = 1;
  repeated string media_urls = 2;
  string          circle_id  = 3;
  string          category   = 4;
}

message GetPostRequest       { string id      = 1; }
message DeletePostRequest    { string id      = 1; }
message BookmarkRequest      { string post_id = 1; bool bookmark = 2; }
message ReshareRequest       { string post_id = 1; string comment = 2; }
message DeleteCommentRequest { string id      = 1; }

message ReactRequest {
  string       post_id  = 1;
  ReactionType reaction = 2;
}

enum ReactionType {
  REACTION_UNSPECIFIED = 0;
  REACTION_LIKE        = 1;
  REACTION_DISLIKE     = 2;
}

message GetCommentsRequest {
  string                     post_id = 1;
  webs.common.v1.PageRequest page    = 2;
}

message AddCommentRequest {
  string          post_id    = 1;
  string          body       = 2;
  repeated string media_urls = 3;
}
"""

SPINS_PROTO = """\
syntax = "proto3";
package webs.spins.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service SpinsService {
  // Bidirectional — client sends scroll events; server preloads next Spins
  rpc StreamSpins  (stream SpinScrollEvent) returns (stream SpinBatch);
  rpc UploadSpin   (UploadSpinRequest)       returns (Spin);
  rpc DeleteSpin   (DeleteSpinRequest)       returns (webs.common.v1.Empty);
  rpc ReactToSpin  (SpinReactRequest)        returns (webs.common.v1.ReactionCounts);
  rpc GetUserSpins (GetUserSpinsRequest)     returns (stream Spin);
}

message Spin {
  string                        id           = 1;
  webs.common.v1.UserSummary    author       = 2;
  string                        caption      = 3;
  string                        video_url    = 4;
  string                        thumbnail    = 5;
  int32                         duration_sec = 6;
  string                        circle_id    = 7;
  string                        audio_title  = 8;
  webs.common.v1.ReactionCounts reactions    = 9;
  google.protobuf.Timestamp     created_at   = 10;
}

message SpinScrollEvent {
  string current_spin_id = 1;
  bool   finished        = 2; // watched to end
}

message SpinBatch        { repeated Spin spins = 1; }
message DeleteSpinRequest { string id          = 1; }

message UploadSpinRequest {
  string caption     = 1;
  string video_url   = 2; // pre-signed object storage URL
  string circle_id   = 3;
  string audio_title = 4;
}

message SpinReactRequest {
  string                        id        = 1;
  webs.common.v1.ReactionCounts reactions = 2;
}

message GetUserSpinsRequest {
  string                     user_id = 1;
  webs.common.v1.PageRequest page    = 2;
}
"""

PROFILE_PROTO = """\
syntax = "proto3";
package webs.profile.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service ProfileService {
  rpc GetProfile    (GetProfileRequest)    returns (Profile);
  rpc UpdateProfile (UpdateProfileRequest) returns (Profile);
  rpc Follow        (FollowRequest)        returns (FollowResponse);
  rpc GetFollowers  (GetFollowRequest)     returns (stream webs.common.v1.UserSummary);
  rpc GetFollowing  (GetFollowRequest)     returns (stream webs.common.v1.UserSummary);
  rpc BlockUser     (BlockRequest)         returns (webs.common.v1.Empty);
  rpc ReportUser    (ReportRequest)        returns (webs.common.v1.Empty);
}

message Profile {
  string                    id              = 1;
  string                    username        = 2;
  string                    display_name    = 3;
  string                    bio             = 4;
  string                    avatar_url      = 5;
  string                    banner_url      = 6;
  bool                      verified        = 7;
  int64                     followers_count = 8;
  int64                     following_count = 9;
  bool                      is_following    = 10;
  bool                      follows_you     = 11;
  google.protobuf.Timestamp joined_at       = 12;
}

message GetProfileRequest { string user_id = 1; }

message UpdateProfileRequest {
  string display_name = 1;
  string bio          = 2;
  string avatar_url   = 3;
  string banner_url   = 4;
}

message FollowRequest {
  string user_id = 1;
  bool   follow  = 2;
}

message FollowResponse {
  bool  is_following    = 1;
  int64 followers_count = 2;
}

message GetFollowRequest {
  string                     user_id = 1;
  webs.common.v1.PageRequest page    = 2;
}

message BlockRequest  { string user_id = 1; bool block  = 2; }
message ReportRequest { string user_id = 1; string reason = 2; }
"""

CIRCLES_PROTO = """\
syntax = "proto3";
package webs.circles.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

// Circles are created and managed by Webs only.
// Users may join, leave, browse, and tag posts to Circles.
service CirclesService {
  rpc GetMyCircles   (webs.common.v1.Empty) returns (stream Circle);
  rpc ExploreCircles (ExploreRequest)        returns (stream Circle);
  rpc GetCircle      (GetCircleRequest)      returns (Circle);
  rpc JoinCircle     (JoinRequest)           returns (JoinResponse);
  rpc LeaveCircle    (LeaveRequest)          returns (webs.common.v1.Empty);
  rpc GetCategories  (webs.common.v1.Empty)  returns (CategoriesResponse);
}

message Circle {
  string                    id             = 1;
  string                    name           = 2;
  string                    description    = 3;
  string                    category       = 4;
  string                    avatar_url     = 5;
  string                    banner_url     = 6;
  int64                     members_count  = 7;
  int64                     posts_count    = 8;
  bool                      is_member      = 9;
  google.protobuf.Timestamp created_at     = 10;
}

message ExploreRequest {
  string                     category = 1;
  webs.common.v1.PageRequest page     = 2;
}

message GetCircleRequest { string id        = 1; }
message JoinRequest      { string circle_id = 1; }
message LeaveRequest     { string circle_id = 1; }

message JoinResponse {
  bool  is_member     = 1;
  int64 members_count = 2;
}

message CategoriesResponse { repeated string categories = 1; }
"""

STORIES_PROTO = """\
syntax = "proto3";
package webs.stories.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service StoriesService {
  // Server-streaming — ordered story queue for the stories bar
  rpc GetStoriesBar  (webs.common.v1.Empty)   returns (stream StoryGroup);
  rpc GetUserStories (GetUserStoriesRequest)   returns (stream Story);
  rpc PostStory      (PostStoryRequest)        returns (Story);
  rpc DeleteStory    (DeleteStoryRequest)      returns (webs.common.v1.Empty);
  rpc MarkSeen       (MarkSeenRequest)         returns (webs.common.v1.Empty);
}

message Story {
  string                        id         = 1;
  webs.common.v1.UserSummary    author     = 2;
  webs.common.v1.MediaItem      media      = 3;
  string                        text       = 4;
  bool                          seen       = 5;
  google.protobuf.Timestamp     created_at = 6;
  google.protobuf.Timestamp     expires_at = 7; // 24h after creation
}

message StoryGroup {
  webs.common.v1.UserSummary user       = 1;
  int32                      count      = 2;
  bool                       has_unseen = 3;
}

message GetUserStoriesRequest { string user_id = 1; }
message DeleteStoryRequest    { string id      = 1; }
message MarkSeenRequest       { string id      = 1; }

message PostStoryRequest {
  string                        media_url  = 1;
  string                        text       = 2;
  webs.common.v1.MediaType      media_type = 3;
}
"""

MESSAGES_PROTO = """\
syntax = "proto3";
package webs.messages.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service MessagesService {
  rpc GetInbox           (webs.common.v1.Empty)   returns (stream Conversation);
  // Bidirectional — real-time chat with typing indicators and read receipts
  rpc StreamConversation (stream ChatEvent)        returns (stream ChatEvent);
  rpc CreateConversation (CreateConversationRequest) returns (Conversation);
  rpc SendMessage        (SendMessageRequest)      returns (Message);
  rpc DeleteMessage      (DeleteMessageRequest)    returns (webs.common.v1.Empty);
  rpc MarkRead           (MarkReadRequest)         returns (webs.common.v1.Empty);
}

message Conversation {
  string                              id            = 1;
  repeated webs.common.v1.UserSummary participants  = 2;
  Message                             last_message  = 3;
  int32                               unread_count  = 4;
  bool                                is_group      = 5;
  string                              group_name    = 6;
  string                              group_avatar  = 7;
  google.protobuf.Timestamp           updated_at    = 8;
}

message Message {
  string                            id              = 1;
  string                            conversation_id = 2;
  webs.common.v1.UserSummary        sender          = 3;
  string                            body            = 4;
  repeated webs.common.v1.MediaItem media           = 5;
  bool                              read            = 6;
  google.protobuf.Timestamp         created_at      = 7;
}

message ChatEvent {
  oneof event {
    Message      new_message = 1;
    TypingEvent  typing      = 2;
    ReadEvent    read        = 3;
    string       delete_id   = 4;
  }
}

message TypingEvent { string user_id = 1; bool typing = 2; }
message ReadEvent   { string message_id = 1; string user_id = 2; }

message CreateConversationRequest {
  repeated string participant_ids = 1;
  bool            is_group        = 2;
  string          group_name      = 3;
}

message SendMessageRequest {
  string          conversation_id = 1;
  string          body            = 2;
  repeated string media_urls      = 3;
}

message DeleteMessageRequest { string id              = 1; }
message MarkReadRequest      { string conversation_id = 1; string up_to_message_id = 2; }
"""

ACTIVITY_PROTO = """\
syntax = "proto3";
package webs.activity.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "google/protobuf/timestamp.proto";

service ActivityService {
  // Server-streaming — activity items pushed in real time
  rpc StreamActivity (ActivityRequest)          returns (stream ActivityItem);
  rpc MarkAllRead    (webs.common.v1.Empty)     returns (webs.common.v1.Empty);
  rpc MarkRead       (MarkActivityReadRequest)  returns (webs.common.v1.Empty);
}

message ActivityItem {
  string                        id         = 1;
  ActivityType                  type       = 2;
  webs.common.v1.UserSummary    actor      = 3;
  string                        target_id  = 4; // post, spin, or comment id
  string                        preview    = 5; // short content snippet
  string                        media_url  = 6; // optional thumbnail
  bool                          read       = 7;
  google.protobuf.Timestamp     created_at = 8;
}

enum ActivityType {
  ACTIVITY_UNSPECIFIED = 0;
  ACTIVITY_LIKE        = 1;
  ACTIVITY_DISLIKE     = 2;
  ACTIVITY_COMMENT     = 3;
  ACTIVITY_RESHARE     = 4;
  ACTIVITY_FOLLOW      = 5;
  ACTIVITY_MENTION     = 6;
  ACTIVITY_REPLY       = 7;
}

message ActivityRequest       { webs.common.v1.PageRequest page = 1; }
message MarkActivityReadRequest { repeated string ids            = 1; }
"""

SEARCH_PROTO = """\
syntax = "proto3";
package webs.search.v1;
option java_package        = "app.webs.android.generated";
option java_multiple_files = true;
option swift_prefix        = "Webs";

import "common.proto";
import "post.proto";

service SearchService {
  rpc Search         (SearchRequest)      returns (SearchResponse);
  rpc SearchPeople   (SearchRequest)      returns (stream webs.common.v1.UserSummary);
  rpc Trending       (TrendingRequest)    returns (TrendingResponse);
  rpc GetSuggestions (SuggestionsRequest) returns (SuggestionsResponse);
}

message SearchRequest {
  string                     query  = 1;
  SearchFilter               filter = 2;
  webs.common.v1.PageRequest page   = 3;
}

enum SearchFilter {
  SEARCH_FILTER_ALL    = 0;
  SEARCH_FILTER_POSTS  = 1;
  SEARCH_FILTER_PEOPLE = 2;
  SEARCH_FILTER_TOPICS = 3;
  SEARCH_FILTER_MEDIA  = 4;
}

message SearchResponse {
  repeated webs.common.v1.UserSummary people = 1;
  repeated webs.post.v1.Post          posts  = 2;
  repeated TopicResult                topics = 3;
  webs.common.v1.PageInfo             page   = 4;
}

message TopicResult {
  string topic      = 1;
  int64  post_count = 2;
  string category   = 3;
}

message TrendingRequest    { string category = 1; }
message TrendingResponse   { repeated TopicResult topics = 1; }
message SuggestionsRequest { webs.common.v1.PageRequest page = 1; }
message SuggestionsResponse { repeated webs.common.v1.UserSummary users = 1; }
"""

PROTO_README = """\
# proto/

Shared Protobuf definitions for the Webs platform.
Single source of truth for all client-server contracts.

## Files

| File | Package | Description |
|---|---|---|
| `common.proto` | `webs.common.v1` | Shared types — pagination, media, user summary, reactions |
| `auth.proto` | `webs.auth.v1` | Signup, login, token refresh |
| `feed.proto` | `webs.feed.v1` | Home feed — For You, Following, Trending (server-streaming) |
| `post.proto` | `webs.post.v1` | Webs (posts), comments, reactions |
| `spins.proto` | `webs.spins.v1` | Short-form video — bidirectional streaming for preloading |
| `profile.proto` | `webs.profile.v1` | User profiles, follow graph |
| `circles.proto` | `webs.circles.v1` | Platform-curated communities |
| `stories.proto` | `webs.stories.v1` | Ephemeral 24h stories |
| `messages.proto` | `webs.messages.v1` | DMs and group threads — bidirectional streaming |
| `activity.proto` | `webs.activity.v1` | Activity feed — likes, follows, mentions (server-streaming) |
| `search.proto` | `webs.search.v1` | Full-text search, trending topics, follow suggestions |

## Streaming patterns

| Service | Pattern | Reason |
|---|---|---|
| Feed | Server-streaming | Push new Webs as they arrive |
| Spins | Bidirectional | Client reports scroll position; server preloads next batch |
| Messages | Bidirectional | Real-time chat — typing indicators, read receipts |
| Activity | Server-streaming | Push new activity items instantly |
| Stories | Server-streaming | Ordered story queue for the stories bar |

## Generate stubs

```bash
cd proto
buf generate
```

Outputs land in:
- `../webs-server/src/generated/`   — Rust (prost + tonic)
- `../webs-ios/WebsApp/Generated/`  — Swift (grpc-swift + swift-protobuf)
- `../webs-android/.../generated/`  — Kotlin lite

## Lint and breaking change detection

```bash
buf lint
buf breaking --against '.git#branch=main'
```

## Rules

- Never edit generated files directly
- All proto changes must be reviewed before merging
- Breaking changes require a version bump in the package name
"""

# ── Scaffold ───────────────────────────────────────────────────────────────────

def scaffold():
    base = "proto"
    print(f"\n🕸  Scaffolding {base}/\n")

    write(f"{base}/buf.yaml",        BUF_YAML)
    write(f"{base}/buf.gen.yaml",    BUF_GEN_YAML)
    write(f"{base}/common.proto",    COMMON_PROTO)
    write(f"{base}/auth.proto",      AUTH_PROTO)
    write(f"{base}/feed.proto",      FEED_PROTO)
    write(f"{base}/post.proto",      POST_PROTO)
    write(f"{base}/spins.proto",     SPINS_PROTO)
    write(f"{base}/profile.proto",   PROFILE_PROTO)
    write(f"{base}/circles.proto",   CIRCLES_PROTO)
    write(f"{base}/stories.proto",   STORIES_PROTO)
    write(f"{base}/messages.proto",  MESSAGES_PROTO)
    write(f"{base}/activity.proto",  ACTIVITY_PROTO)
    write(f"{base}/search.proto",    SEARCH_PROTO)
    write(f"{base}/README.md",       PROTO_README)

    print(f"\n✅  Done. Run `cd proto && buf generate` to emit all stubs.\n")

# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    scaffold()
