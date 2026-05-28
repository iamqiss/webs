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
