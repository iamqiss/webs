package app.webs.android.data.repository

import kotlinx.coroutines.flow.Flow

interface MessageRepository {
    // TODO: define repository contract
}

class MessageRepositoryImpl(
    // TODO: inject MessageGrpcClient + MessageDao
) : MessageRepository {
    // TODO: implement — emit from Room, sync from gRPC in background
}
