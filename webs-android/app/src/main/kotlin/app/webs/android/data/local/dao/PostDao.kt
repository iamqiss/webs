package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.PostEntity

@Dao
interface PostDao {
    @Query("SELECT * FROM posts")
    fun getAll(): Flow<List<PostEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<PostEntity>)

    @Query("DELETE FROM posts")
    suspend fun clear()

    // TODO: additional queries
}
