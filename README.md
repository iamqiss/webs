# 🕸 Webs

> **Proprietary and Confidential**
> Copyright © 2026 Webs. All rights reserved.
> Unauthorized copying, distribution, modification, or use of this software, in whole or in part, is strictly prohibited.

---

Webs is a next-generation social platform built for speed, community, and expression. Post a **Web**. Watch a **Spin**. Join a **Circle**. Connect with people around what actually matters to you — without the noise.

This is the official monorepo housing all core components of the Webs platform.

---

## 📦 Monorepo Structure

```
webs/
├── webs-server/       # Backend — Rust + SurrealDB + gRPC
├── webs-ios/          # iOS client — SwiftUI
├── webs-android/      # Android client — Jetpack Compose
├── proto/             # Shared Protobuf definitions (gRPC contracts)
├── docs/              # Architecture decisions, API specs, internal docs
└── README.md
```

---

## ✨ What is Webs?

Webs is a social platform designed from the ground up with three principles:

- **Speed first** — sub-100ms interactions, gRPC streaming, zero compromise
- **Offline first** — your feed, profile, and drafts are available without a connection
- **Platform integrity** — Circles are curated by Webs, not the chaos of user-created groups

### Core Concepts

| Concept | Description |
|---|---|
| **Web** | A post. Text, images, or links. To post is to *web*. |
| **Spin** | Short-form video content. The Webs equivalent of Reels. |
| **Circle** | A curated interest community, created and maintained by Webs. Users can join, tag posts to, and explore Circles — but not create them. |
| **Stories** | Ephemeral 24-hour content, surfaced at the top of the Home feed. |

---

## 🏗️ Tech Stack

### Server — `webs-server`

| Layer | Technology |
|---|---|
| Language | **Rust** |
| Database | **SurrealDB** |
| API Protocol | **gRPC** (tonic) with bidirectional streaming |
| Auth | JWT + refresh token rotation |
| Media | Object storage (S3-compatible) |
| Search | SurrealDB full-text search |
| Runtime | Tokio async runtime |

Rust + SurrealDB + gRPC is not an arbitrary choice. This stack is estimated to reduce infrastructure costs by **~80%** compared to traditional Node/Go + PostgreSQL + REST architectures at equivalent scale, owing to:

- Rust's near-zero memory overhead and fearless concurrency
- SurrealDB's multi-model nature eliminating the need for separate graph, relational, and document stores
- gRPC's binary framing (Protocol Buffers) dramatically reducing payload sizes vs JSON REST
- Streaming connections replacing expensive polling patterns

### iOS — `webs-ios`

| Layer | Technology |
|---|---|
| Language | **Swift** |
| UI Framework | **SwiftUI** |
| Networking | **gRPC-Swift** |
| Local Storage | **SwiftData** (offline-first) |
| Media Playback | **AVFoundation** |
| Architecture | **TCA (The Composable Architecture)** |

The iOS app is built to feel unmistakably Apple — following Human Interface Guidelines, leveraging native gestures, and using platform APIs wherever possible. No cross-platform compromise.

### Android — `webs-android`

| Layer | Technology |
|---|---|
| Language | **Kotlin** |
| UI Framework | **Jetpack Compose** |
| Networking | **gRPC-Kotlin** |
| Local Storage | **Room** (offline-first) |
| Media Playback | **Media3 / ExoPlayer** |
| Architecture | **MVI + ViewModel** |

The Android app is built to feel unmistakably Google — following Material You guidelines, supporting dynamic color theming, and respecting Android's back stack and lifecycle natively. No half-measures.

---

## 🔌 gRPC & Shared Protobuf

All client-server communication is defined in `/proto` and shared across all three packages. This is the single source of truth for the Webs API contract.

```
proto/
├── auth.proto         # Authentication & sessions
├── feed.proto         # Home feed, For You, Following, Trending
├── post.proto         # Webs (posts) — create, read, react, share
├── spins.proto        # Spin upload, streaming, engagement
├── profile.proto      # User profiles, follow graph
├── circles.proto      # Circle discovery, membership, feeds
├── stories.proto      # Story upload & viewing
├── messages.proto     # Direct messages & group threads
├── notifications.proto
└── search.proto
```

Key streaming patterns:
- **Feed** uses server-side streaming — new Webs pushed as they arrive
- **Spins** uses bidirectional streaming for buffered preloading
- **Messages** uses bidirectional streaming for real-time chat
- **Stories** uses server-side streaming for ordered playback queues

---

## 📡 Offline-First Architecture

Webs is designed to remain usable without a network connection.

### iOS
- Feed, profiles, and Circles are cached via **SwiftData** with TTL-based invalidation
- Draft Webs and Spins are queued locally and synced on reconnect
- Optimistic UI updates for reactions and follows — rolled back gracefully on failure

### Android
- Feed and profile data persisted in **Room** with a clean repository layer abstracting local vs remote
- WorkManager handles background sync and upload queuing
- Offline indicator surfaced subtly in the UI without blocking interaction

---

## 🧭 Navigation Structure

Webs uses a floating bottom navigation bar with five items:

```
[ Home ]  [ Discover ]  [ Spins ]  [ Circles ]  [ Profile ]
```

- The **＋ (Compose)** button floats above the nav bar, animated — it rises slightly on scroll up and retreats on scroll down
- **Spins** tab launches a full-screen vertical video feed
- **Circles** tab shows joined Circles and an Explore view for discovering new ones

---

## 👤 Profile

The profile screen surfaces what matters:

- **Followers** and **Following** counts only — no post count, no Circle count
- Two content tabs: **Webs** and **Spins**
- Own profile shows **Edit Profile** button
- Other profiles show **Follow** and **Message** buttons
- Verified badge displayed inline with display name

---

## 🔵 Circles — Platform-Curated Communities

Circles on Webs are **not user-created**. They are created, named, and maintained by the Webs platform team. This is an intentional product decision:

- Eliminates fragmentation, duplicate communities, and low-quality groups
- Ensures every Circle has a clear identity and content standard
- Users can **join**, **tag their Webs** to a Circle, **browse** Circle feeds, and **be discovered** through Circles
- Gives Webs full editorial control over community taxonomy

---

## 🚀 Getting Started

### Prerequisites

- Rust `>=1.78` with `cargo`
- SurrealDB `>=2.0`
- Xcode `>=16` (iOS)
- Android Studio Koala or later (Android)
- `protoc` — Protocol Buffer compiler
- `buf` — Protobuf linting and generation (recommended)

### Clone

```bash
git clone https://github.com/your-org/webs.git
cd webs
```

### Server

```bash
cd webs-server
cp .env.example .env          # Configure DB, secrets, storage
cargo build --release
cargo run
```

### iOS

```bash
cd webs-ios
open Webs.xcodeproj
# Select target device and run
```

### Android

```bash
cd webs-android
# Open in Android Studio and sync Gradle
./gradlew assembleDebug
```

### Regenerate Protobuf

```bash
cd proto
buf generate
```

This outputs generated Swift and Kotlin stubs into `webs-ios/Generated/` and `webs-android/generated/` respectively.

---

## 🗂️ Key Conventions

- **Branch naming**: `feature/`, `fix/`, `chore/`, `proto/`
- **Commit style**: Conventional Commits (`feat:`, `fix:`, `refactor:`, etc.)
- **Proto changes**: Always discussed before merging — breaking changes require a version bump
- **No shared UI code** between iOS and Android — both apps are native-first, built to feel like they belong on their platform

---

## 📋 Roadmap Highlights

- [ ] Core feed, profile, and Webs (post) flow
- [ ] Spins — upload, playback, and For You ranking
- [ ] Stories — ephemeral 24h content
- [ ] Circles — curated discovery and feeds
- [ ] Direct Messages — 1:1 and group threads
- [ ] Notifications — push + in-app
- [ ] Search — people, topics, Circles, Webs
- [ ] Verified accounts and trust signals
- [ ] Content moderation tooling (internal)
- [ ] Analytics & creator insights

---

## 🔒 License

**Proprietary. All rights reserved.**

This software and all associated source code, documentation, and assets are the exclusive property of Webs. No part of this repository may be copied, modified, distributed, sublicensed, or used in any form without explicit written permission from the owners.

See [`LICENSE`](./LICENSE) for full terms.
