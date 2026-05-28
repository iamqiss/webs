package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// ActivityItemEntity — Room entity for offline-first activityitem cache
@Entity(tableName = "activityitems")
data class ActivityItemEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
