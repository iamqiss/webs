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
