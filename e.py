#!/usr/bin/env python3
"""
scaffold_webs_docs.py

Scaffolds the docs/ directory for the Webs monorepo.

Usage:
    chmod +x scaffold_webs_docs.py
    ./scaffold_webs_docs.py

Or:

    python3 scaffold_webs_docs.py
"""

from pathlib import Path

OVERWRITE = False

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def write(path: str, content: str = "") -> None:
    file_path = Path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists() and not OVERWRITE:
        print(f"  skipped   {path}")
        return

    file_path.write_text(content, encoding="utf-8")
    print(f"  created   {path}")


# ──────────────────────────────────────────────────────────────────────────────
# Shared warning
# ──────────────────────────────────────────────────────────────────────────────

SCAFFOLDED_WARNING = """\
> This file was scaffolded automatically and may contain placeholders.

"""

# ──────────────────────────────────────────────────────────────────────────────
# Root docs
# ──────────────────────────────────────────────────────────────────────────────

INDEX = f"""\
# Webs — Documentation

> **Proprietary and Confidential**
> Copyright © 2026 Webs. All rights reserved.

Welcome to the internal documentation for the Webs platform monorepo.

## Documentation structure

| Section | Description |
|---|---|
| [Setup](./setup/README.md) | Local development and tooling |
| [Architecture](./architecture/overview.md) | System design and infrastructure |
| [API](./api/overview.md) | gRPC services and streaming |
| [Server](./server/overview.md) | Rust backend internals |
| [iOS](./ios/overview.md) | SwiftUI + TCA client |
| [Android](./android/overview.md) | Compose + MVI client |
| [Proto](./proto/overview.md) | Protobuf contracts |
| [Design](./design/overview.md) | Product and UX system |
| [Observability](./observability/README.md) | Logging, tracing, metrics |
| [Moderation](./moderation/README.md) | Trust & safety systems |
| [Contributing](./contributing/overview.md) | Workflow and conventions |
| [ADRs](./adr/README.md) | Architecture Decision Records |
| [Runbooks](./runbooks/README.md) | Operational procedures |
| [Glossary](./glossary.md) | Platform terminology |
"""

SUMMARY = """\
# Summary

- Setup
  - Local Development
  - Server
  - iOS
  - Android
  - Proto
  - Tooling

- Architecture
  - Overview
  - Data Flow
  - Database
  - Security
  - Scalability

- API
  - Overview
  - Auth
  - Feed
  - Activity
  - Posts
  - Spins
  - Messages

- Server
- iOS
- Android
- Proto
- Design
- Observability
- Moderation
- ADRs
- Runbooks
"""

GLOSSARY = """\
# Glossary

| Term | Meaning |
|---|---|
| Web | A post on Webs |
| Spin | Short-form vertical video |
| Circle | Curated interest community |
| Story | Ephemeral 24h content |
| FeedEvent | Realtime feed update event |
| ActivityItem | Notification/activity event |
| Stream | Long-lived gRPC streaming connection |
| Fanout | Delivering events to many connected users |
| Repository | Offline-first sync layer |
"""

# ──────────────────────────────────────────────────────────────────────────────
# Architecture
# ──────────────────────────────────────────────────────────────────────────────

ARCH_SCALABILITY = """\
# Scalability

## Horizontal scaling

`webs-server` is stateless.

Any server instance can process any request.

Shared infrastructure:

- SurrealDB
- Object storage
- Iggy message streaming
- Push notification workers

This allows independent horizontal scaling of:
- API servers
- media workers
- feed fanout workers
- notification workers

## Realtime event fanout

Webs uses Iggy for internal event streaming.

Examples:
- new posts
- feed fanout
- activity events
- push notification jobs
- DM delivery
- analytics ingestion

## Why Iggy

Iggy aligns well with the Webs architecture:

- Rust-native ecosystem
- lightweight operational footprint
- low latency
- streaming-first design
- simpler deployment than Kafka
- ideal for realtime mobile workloads

## Future infrastructure

Potential future additions:

- CDN for media delivery
- edge image resizing
- dedicated recommendation service
- search indexing workers
- realtime analytics pipelines
- ML ranking systems

## Scaling strategy

The initial scaling strategy prioritizes:

1. Low operational complexity
2. Efficient memory usage
3. Streaming-first communication
4. Horizontal scalability
5. Minimal infrastructure count

The platform intentionally avoids excessive microservice fragmentation early on.
"""

OBSERVABILITY_README = """\
# Observability

## Stack

| Tool | Purpose |
|---|---|
| OpenTelemetry | Distributed tracing |
| Prometheus | Metrics |
| Grafana | Dashboards |
| Loki | Log aggregation |
| Tempo | Trace storage |

## Coverage

The platform instruments:

- gRPC requests
- stream lifecycle
- database queries
- background jobs
- cache operations
- feed fanout latency
- media upload performance
"""

MODERATION_README = """\
# Moderation

## Scope

Moderation systems cover:

- reporting
- spam prevention
- impersonation
- abusive content
- account enforcement
- rate limiting
- bot detection

## Future systems

Planned additions:

- automated moderation queues
- ML-assisted spam detection
- trust scoring
- safety audit logs
"""

SETUP_README = """\
# Setup

## Requirements

| Tool | Version |
|---|---|
| Rust | stable |
| Xcode | latest |
| Android Studio | latest |
| SurrealDB | 2.x |
| buf | latest |
| protoc | latest |

## Guides

- local-development.md
- server.md
- ios.md
- android.md
- proto.md
- tooling.md
"""

# ──────────────────────────────────────────────────────────────────────────────
# ADR
# ──────────────────────────────────────────────────────────────────────────────

ADR_0009_IGGY = """\
# 0009 — Use Iggy for internal event streaming

**Status:** Accepted
**Date:** 2026-01-01

## Context

Webs requires realtime event distribution for feeds, messaging, activity
delivery, notifications, and analytics ingestion.

The architecture is Rust-first and streaming-heavy.

## Decision

Use Iggy as the internal event streaming platform.

## Alternatives considered

- Kafka
- NATS
- Redis Streams
- RabbitMQ

## Consequences

Advantages:

- Rust-native ecosystem
- lower operational complexity
- lightweight deployment
- strong fit for realtime workloads
- lower memory overhead

Trade-offs:

- smaller ecosystem than Kafka
- fewer managed hosting providers
- younger tooling ecosystem
"""

# ──────────────────────────────────────────────────────────────────────────────
# Main scaffold
# ──────────────────────────────────────────────────────────────────────────────

def scaffold():
    base = "docs"

    print(f"\n🕸  Scaffolding {base}/\n")

    # Root
    write(f"{base}/README.md", INDEX)
    write(f"{base}/SUMMARY.md", SUMMARY)
    write(f"{base}/glossary.md", GLOSSARY)

    # Setup
    write(f"{base}/setup/README.md", SETUP_README)

    for name in [
        "local-development",
        "server",
        "ios",
        "android",
        "proto",
        "tooling",
    ]:
        write(
            f"{base}/setup/{name}.md",
            SCAFFOLDED_WARNING +
            f"# {name.replace('-', ' ').title()}\n\nTODO.\n"
        )

    # Architecture
    write(
        f"{base}/architecture/scalability.md",
        ARCH_SCALABILITY
    )

    # Observability
    write(
        f"{base}/observability/README.md",
        OBSERVABILITY_README
    )

    # Moderation
    write(
        f"{base}/moderation/README.md",
        MODERATION_README
    )

    # ADR
    write(
        f"{base}/adr/0009-iggy-streaming.md",
        ADR_0009_IGGY
    )

    print(f"\n✅ Done. Docs scaffolded in {base}/\n")


if __name__ == "__main__":
    scaffold()


