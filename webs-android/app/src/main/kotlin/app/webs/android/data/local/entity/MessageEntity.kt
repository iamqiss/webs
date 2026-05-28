package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// MessageEntity — Room entity for offline-first message cache
@Entity(tableName = "messages")
data class MessageEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
