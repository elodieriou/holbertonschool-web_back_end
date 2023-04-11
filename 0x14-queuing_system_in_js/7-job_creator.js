import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const queueName = 'push_notification_code_2';
jobs.forEach((object) => {
  const job = queue
    .create(queueName, object)
    .save((error) => {
      if (!error) console.log(`Notification job created: ${job.id}`);
    });

  job.on('complete', (job) => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (job, error) => {
    console.log(`Notification job ${job.id} failed: ${error.message}`);
  });

  job.on('progress', (job, progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});