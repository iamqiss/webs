package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.StoryEntity

@Dao
interface StoryDao {
    @Query("SELECT * FROM storys")
    fun getAll(): Flow<List<StoryEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<StoryEntity>)

    @Query("DELETE FROM storys")
    suspend fun clear()

    // TODO: additional queries
}
