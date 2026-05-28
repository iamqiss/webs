package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface CircleRepository {
    // TODO: define repository contract
}

class CircleRepositoryImpl(
    // TODO: inject CircleGrpcClient + CircleDao
) : CircleRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
