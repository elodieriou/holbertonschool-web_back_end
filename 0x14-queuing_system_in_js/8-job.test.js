import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const queueName = 'push_notification_code_3';
const jobs = [
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  }];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(23, queue)).throws(
      Error, 'Jobs is not an array',
    );
  });

  it('should not throw an error if jobs is an empty array', () => {
    expect(createPushNotificationsJobs([], queue)).equals(undefined);
  });

  it('should create a job in the queue', () => {
    queue.createJob(queueName, jobs).save();
    expect(queue.testMode.jobs.length).to.equal(1);
  });

  it('should set the correct properties on the created job', () => {
    queue.createJob(queueName, jobs).save();
    const job = queue.testMode.jobs[0];
    expect(job.data).to.deep.equal(jobs);
    expect(job.type).equals('push_notification_code_3');
  });

  it('should execute the job as completed', () => {
    queue.createJob(queueName, jobs).save();
    const job = queue.testMode.jobs[0];
    job.on('progress', () => {
      expect(job.state).to.equal('active');
    });
    job.on('complete', () => {
      expect(job.state).equals('completed');
    });
  });
});
