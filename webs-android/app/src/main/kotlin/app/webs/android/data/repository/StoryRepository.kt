package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface StoryRepository {
    // TODO: define repository contract
}

class StoryRepositoryImpl(
    // TODO: inject StoryGrpcClient + StoryDao
) : StoryRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
