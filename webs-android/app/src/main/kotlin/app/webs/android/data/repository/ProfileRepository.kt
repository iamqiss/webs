package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface ProfileRepository {
    // TODO: define repository contract
}

class ProfileRepositoryImpl(
    // TODO: inject ProfileGrpcClient + ProfileDao
) : ProfileRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
