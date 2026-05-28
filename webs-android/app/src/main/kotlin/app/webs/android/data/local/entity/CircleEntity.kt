package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// CircleEntity — Room entity for offline-first circle cache
@Entity(tableName = "circles")
data class CircleEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
