package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// PostEntity — Room entity for offline-first post cache
@Entity(tableName = "posts")
data class PostEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
