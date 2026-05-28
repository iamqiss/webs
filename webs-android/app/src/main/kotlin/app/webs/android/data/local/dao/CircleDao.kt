package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.CircleEntity

@Dao
interface CircleDao {
    @Query("SELECT * FROM circles")
    fun getAll(): Flow<List<CircleEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<CircleEntity>)

    @Query("DELETE FROM circles")
    suspend fun clear()

    // TODO: additional queries
}
