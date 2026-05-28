package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface AuthRepository {
    // TODO: define repository contract
}

class AuthRepositoryImpl(
    // TODO: inject AuthGrpcClient + AuthDao
) : AuthRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
