package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface SpinRepository {
    // TODO: define repository contract
}

class SpinRepositoryImpl(
    // TODO: inject SpinGrpcClient + SpinDao
) : SpinRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
