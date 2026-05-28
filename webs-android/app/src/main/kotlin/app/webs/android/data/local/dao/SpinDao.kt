package app.webs.android.data.local.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import kotlinx.coroutines.flow.Flow
import app.webs.android.data.local.entity.SpinEntity

@Dao
interface SpinDao {
    @Query("SELECT * FROM spins")
    fun getAll(): Flow<List<SpinEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(items: List<SpinEntity>)

    @Query("DELETE FROM spins")
    suspend fun clear()

    // TODO: additional queries
}
