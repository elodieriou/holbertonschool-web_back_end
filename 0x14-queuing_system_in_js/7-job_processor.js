import kue from 'kue';

const blacklisted = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklisted.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();
const queueName = 'push_notification_code_2';
queue.process(queueName, 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
