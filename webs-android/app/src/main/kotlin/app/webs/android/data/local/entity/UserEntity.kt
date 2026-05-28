package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// UserEntity — Room entity for offline-first user cache
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
