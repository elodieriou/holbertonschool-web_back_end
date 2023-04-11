import kue from 'kue';

const queue = kue.createQueue();

const object = {
  phoneNumber: '0645649206',
  message: 'Hello Élo!',
};

const queueName = 'push_notification_code';

const job = queue
  .create(queueName, object)
  .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
