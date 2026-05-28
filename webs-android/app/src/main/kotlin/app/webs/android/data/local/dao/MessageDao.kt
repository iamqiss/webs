package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.MessageEntity

@Dao
interface MessageDao {
    @Query("SELECT * FROM messages")
    fun getAll(): Flow<List<MessageEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<MessageEntity>)

    @Query("DELETE FROM messages")
    suspend fun clear()

    // TODO: additional queries
}
