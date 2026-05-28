package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.UserEntity

@Dao
interface UserDao {
    @Query("SELECT * FROM users")
    fun getAll(): Flow<List<UserEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<UserEntity>)

    @Query("DELETE FROM users")
    suspend fun clear()

    // TODO: additional queries
}
