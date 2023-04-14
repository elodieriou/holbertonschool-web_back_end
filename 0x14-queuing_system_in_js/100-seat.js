import redis from 'redis';
import util from 'util';
import kue from 'kue';
import express, { response } from 'express';

// Server redis

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const availableSeats = 'available_seats';

function reserveSeat(number) {
  client.set(availableSeats, number, redis.print);
}

async function getCurrentAvailableSeats() {
  const reply = await getAsync(availableSeats);
  return reply;
}

reserveSeat(2);
let reservationEnabled = true;

// Queue

const queue = kue.createQueue();

// API express

const port = 1245;
const app = express();
const queueName = 'reserve_seat';

app.get('/available_seats', async (request, response) => {
  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats < 1) reservationEnabled = false;

  const numberOfAvailableSeats = {
    numberOfAvailableSeats: currentAvailableSeats,
  };
  response.send(numberOfAvailableSeats);
});

app.get('/reserve_seat', (request, response) => {
  const reservationBlocked = { status: 'Reservation are blocked' };
  if (!reservationEnabled) response.send(reservationBlocked);
  else {
    const reservationProcess = { status: 'Reservation in process' };
    const reservationFailed = { status: 'Reservation failed' };
    const job = queue
      .createJob(queueName)
      .save((error) => {
        if (!error) response.send(reservationProcess);
        else response.send(reservationFailed);
      });
    job.on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (error) => {
      console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });
  }
});

app.get('/process', (request, response) => {
  const queueProcessing = { status: 'Queue processing' };
  response.send(queueProcessing);

  queue.process(queueName, async (job, done) => {
    const currentAvailableSeat = await getCurrentAvailableSeats();
    const newNumberOfSeatAvailable = Number(currentAvailableSeat) - 1;

    if (reservationEnabled) reserveSeat(newNumberOfSeatAvailable);
    else done(Error('Not enough seats available'));

    if (newNumberOfSeatAvailable === 0) reservationEnabled = false;

    done();
  });
});

app.listen(port);
module.exports = app;
