package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface FeedRepository {
    // TODO: define repository contract
}

class FeedRepositoryImpl(
    // TODO: inject FeedGrpcClient + FeedDao
) : FeedRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
