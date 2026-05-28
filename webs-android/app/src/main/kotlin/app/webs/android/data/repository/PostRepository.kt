package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface PostRepository {
    // TODO: define repository contract
}

class PostRepositoryImpl(
    // TODO: inject PostGrpcClient + PostDao
) : PostRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
