function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', job);

    newJob.on('enqueue', () => {
      console.log(`Notification job created: ${newJob.id}`);
    });
    newJob.on('complete', () => {
      console.log(`Notification job ${newJob.id} completed`);
    });
    newJob.on('failed', (error) => {
      console.log(`Notification job ${newJob.id} failed: ${error}`);
    });
    newJob.on('progress', (progress) => {
      console.log(`Notification job ${newJob.id} ${progress} complete`);
    });
    newJob.save();
  }
}

module.exports = createPushNotificationsJobs;
