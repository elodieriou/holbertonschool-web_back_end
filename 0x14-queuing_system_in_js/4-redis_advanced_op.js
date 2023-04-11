import redis from 'redis';

const client = redis.createClient();

client.hset('HolbertonSchools', 'Portland', '50', 'Seattle', '80', 'New York', '20', 'Bogota', '20', 'Cali', '40', 'Paris', '2', redis.print);
client.hgetall('HolbertonSchools', (error, result) => {
  console.log(result);
});
