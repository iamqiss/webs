package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// StoryEntity — Room entity for offline-first story cache
@Entity(tableName = "storys")
data class StoryEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
