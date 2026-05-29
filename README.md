# <p align="center">
#   <img src="./webs-ios/Webs/Assets.xcassets/AppIcon.appiconset/Icon-1024.png" width="120" />
# </p>

<h1 align="center">🕸 Webs</h1>

<p align="center">
  <b>Post a Web. Watch a Spin. Join a Circle.</b><br/>
  A next-generation social platform built for speed, identity, and realtime interaction.
</p>

<p align="center">
  <a href="https://www.rust-lang.org">
    <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  </a>
  <a href="https://github.com/iamqiss/webs/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge" alt="License" />
  </a>
  <a href="https://github.com/iamqiss/webs">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge" alt="Status" />
</p>
---

> **Proprietary and Confidential**  
> Copyright © 2026 Webs. All rights reserved.  
> Unauthorized copying, distribution, modification, or use of this software, in whole or in part, is strictly prohibited.

---

# ✨ What is Webs?

Webs is a next-generation social platform engineered around:

- ⚡ realtime streaming
- 🧠 intelligent identity
- 📡 offline-first architecture
- 🛡 behavioral trust systems
- 🦀 Rust-powered infrastructure
- 📱 truly native mobile apps

Unlike traditional social platforms built on aging REST architectures, Webs is designed from the ground up for modern mobile interaction.

---

# 🌐 Core Concepts

| Concept | Description |
|---|---|
| **Web** | A post. Text, media, links, or thoughts. |
| **Spin** | Short-form vertical video content. |
| **Circle** | A platform-curated interest community. |
| **Story** | Ephemeral 24-hour content. |
| **WID** | Webs Identifier — internal cryptographic account identity. |
| **RTC** | Real-Time Challenge trust system. |
| **EmoPat** | Behavioral emoji-pattern verification layer. |

---

# 🧠 Philosophy

Webs is built around five principles:

| Principle | Description |
|---|---|
| **Speed First** | Everything should feel instant. |
| **Offline First** | The app remains usable without internet. |
| **Human Identity** | People search naturally using names, not handles. |
| **Behavioral Trust** | Trust is earned through interaction patterns. |
| **Platform Integrity** | Communities are intentionally curated. |

---

# 🔐 Identity System

Webs does not rely on usernames as primary identity.

Every account is assigned a cryptographic identifier called a:

# WID — Webs Identifier

Example:

```text
wid:webs:7QX9M2A4D8K1P

Users primarily interact using:

- names
- profile context
- social proximity
- mutuals
- circles
- relevance
- interaction history

Usernames remain optional for:

- mentions
- creators
- vanity handles
- sharing

---

🔎 Intelligent Search

Webs search is not simple text matching.

It combines:

- SurrealDB indexing
- graph relationships
- behavioral relevance
- Circle affinity
- mutual connections
- proximity weighting
- contextual ranking

Searching for people should feel human:

John Doe
Neo Qiss
Sarah from Sandton
Mike from university

—not like querying a database table.

---

🛡 RTC — Real-Time Challenge System

Webs replaces traditional CAPTCHAs with:

RTC — Real-Time Challenges

RTC silently monitors behavioral telemetry across the app:

- typing cadence
- gesture timing
- touch entropy
- navigation patterns
- interaction pacing
- scrolling behavior
- session variance

Most users never encounter RTC.

If suspicious behavior is detected, lightweight verification activates dynamically.

---

😀 EmoPat — Behavioral Verification

EmoPat is Webs' behavioral verification system.

Instead of:

- distorted text
- traffic lights
- image CAPTCHAs

Users solve lightweight emoji interaction challenges:

- reverse sequences
- memory recall
- category grouping
- pattern continuation
- spatial recognition

RTC evaluates:

- tap intervals
- gesture entropy
- timing variance
- interaction consistency

This makes verification:

- faster for humans
- difficult for bots
- mobile-native
- friction-light

---

🏗 Monorepo Structure

webs/
├── webs-server/        # Rust backend
├── webs-ios/           # Native iOS app
├── webs-android/       # Native Android app
├── proto/              # Shared protobuf contracts
├── docs/               # Internal architecture docs
└── README.md

---

🦀 Backend — "webs-server"

Layer| Technology
Language| Rust
Runtime| Tokio
API| gRPC (tonic)
Database| SurrealDB
Streaming| Iggy
Object Storage| S3-compatible
Search| Intelligent ranking pipeline
Auth| JWT + refresh rotation

---

⚙ Backend Architecture

Clients
   ↓
gRPC Gateway
   ↓
Application Services
   ↓
Domain Layer
   ↓
Iggy Event Bus
   ↓
Workers / Pipelines
   ↓
SurrealDB + Object Storage

---

📡 Streaming-First Infrastructure

Webs heavily uses streaming instead of polling.

Feature| Pattern
Feed| Server streaming
Messages| Bidirectional streaming
Spins| Buffered realtime streaming
Notifications| Persistent streaming
RTC telemetry| Background streaming
Presence| Event streaming

---

📦 Event-Driven Design

Webs uses Iggy as its internal streaming backbone.

auth.events
feed.events
message.events
spin.events
rtc.events
search.events
notification.events
moderation.events
analytics.events

This architecture enables:

- realtime fanout
- async workers
- ranking pipelines
- moderation queues
- analytics ingestion
- scalable feed generation

---

🍎 iOS — "webs-ios"

Layer| Technology
Language| Swift
UI| SwiftUI
Networking| gRPC-Swift
Local Storage| SwiftData
Media| AVFoundation
Architecture| TCA

Built to feel unmistakably Apple.

---

🤖 Android — "webs-android"

Layer| Technology
Language| Kotlin
UI| Jetpack Compose
Networking| gRPC-Kotlin
Local Storage| Room
Media| Media3 / ExoPlayer
Architecture| MVI

Built to feel unmistakably Android.

---

🌙 Offline-First

Webs remains usable without internet connectivity.

Locally cached:

- feeds
- profiles
- circles
- messages
- drafts
- stories
- reactions

Sync reconciliation occurs automatically when connectivity returns.

---

🔵 Circles

Circles are platform-curated communities.

Users cannot create Circles.

This prevents:

- fragmentation
- spam ecosystems
- duplicate groups
- abandoned communities

Users can:

- join Circles
- browse Circle feeds
- discover communities
- tag Webs to Circles

---

🚀 Performance Goals

Metric| Goal
Feed latency| <100ms
Cold start| <1.5s
Streaming reconnect| <500ms
Scroll performance| 120fps-capable
Memory overhead| Minimal

---

🔌 Shared Protobuf Contracts

proto/
├── auth.proto
├── feed.proto
├── post.proto
├── spins.proto
├── profile.proto
├── circles.proto
├── stories.proto
├── messages.proto
├── notifications.proto
├── rtc.proto
├── search.proto
└── telemetry.proto

---

🔒 Security

Webs uses:

- Argon2id passphrase hashing
- refresh token rotation
- encrypted gRPC transport
- RTC trust scoring
- behavioral verification
- signed upload URLs
- server-side trust enforcement

Passwords are not required.

Users authenticate using:

- generated passphrases
- custom passphrases
- device trust
- session continuity

---

🚀 Getting Started

Requirements

- Rust >= 1.78
- SurrealDB >= 2.0
- protoc
- buf
- Xcode >= 16
- Android Studio Koala+

---

Clone

git clone https://github.com/your-org/webs.git
cd webs

---

Server

cd webs-server

cp .env.example .env

cargo build --release
cargo run

---

iOS

cd webs-ios

open Webs.xcodeproj

---

Android

cd webs-android

./gradlew assembleDebug

---

Generate Protobufs

cd proto

buf generate

---

📋 Roadmap

- [ ] Feed & profile systems
- [ ] Realtime messaging
- [ ] Spins recommendation pipeline
- [ ] Stories
- [ ] RTC rollout
- [ ] Search engine v1
- [ ] Creator verification
- [ ] Moderation dashboard
- [ ] Analytics platform
- [ ] Adaptive ranking systems

---

🔒 License

Proprietary. All rights reserved.

Webs and all associated code, systems, infrastructure, designs, assets, and documentation are proprietary intellectual property.

No permission is granted to:

- copy
- redistribute
- sublicense
- fork
- modify
- commercially exploit

without explicit written authorization.

See ""LICENSE"" (./LICENSE) for full terms.
