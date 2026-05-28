package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface ActivityRepository {
    // TODO: define repository contract
}

class ActivityRepositoryImpl(
    // TODO: inject ActivityGrpcClient + ActivityDao
) : ActivityRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
