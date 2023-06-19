import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '234556677889',
  message: 'Job has this object has its data',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.log('Notification job failed');
  }
  // console.log('Notification job completed');
});

job.on('complete', () => {
  console.log('Notification job completed');
});
