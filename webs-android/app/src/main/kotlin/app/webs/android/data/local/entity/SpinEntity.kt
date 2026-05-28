package app.webs.android.data.local.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

// SpinEntity — Room entity for offline-first spin cache
@Entity(tableName = "spins")
data class SpinEntity(
    @PrimaryKey val id: String = "",
    // TODO: cached fields
)
