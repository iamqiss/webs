package app.webs.android.data.worker

import android.content.Context
import androidx.hilt.work.HiltWorker
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import dagger.assisted.Assisted
import dagger.assisted.AssistedInject

// PostUploadWorker — background sync / upload via WorkManager
@HiltWorker
class PostUploadWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    // TODO: inject dependencies
) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result {
        // TODO: implement
        return Result.success()
    }
}
