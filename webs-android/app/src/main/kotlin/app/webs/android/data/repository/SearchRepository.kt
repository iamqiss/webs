package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface SearchRepository {
    // TODO: define repository contract
}

class SearchRepositoryImpl(
    // TODO: inject SearchGrpcClient + SearchDao
) : SearchRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
