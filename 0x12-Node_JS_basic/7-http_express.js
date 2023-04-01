const express = require('express');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;
const file = process.argv[2];

const app = express();

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  response.write('This is the list of our students\n');
  countStudents(file)
    .then((data) => {
      response.end(`${data.join('\n')}`);
    })
    .catch((error) => {
      response.end(error.message);
    });
});

app.listen(port, hostname);
module.exports = app;
