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
