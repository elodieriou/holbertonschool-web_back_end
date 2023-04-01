const express = require('express');

const hostname = '127.0.0.1';
const port = 1245;

const app = express();

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.listen(port, hostname);
module.exports = app;
