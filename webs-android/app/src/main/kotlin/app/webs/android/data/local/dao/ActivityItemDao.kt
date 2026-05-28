package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.ActivityItemEntity

@Dao
interface ActivityItemDao {
    @Query("SELECT * FROM activityitems")
    fun getAll(): Flow<List<ActivityItemEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<ActivityItemEntity>)

    @Query("DELETE FROM activityitems")
    suspend fun clear()

    // TODO: additional queries
}
