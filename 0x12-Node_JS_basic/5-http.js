const http = require('http');
const countStudents = require('./3-read_file_async');
const process = require('process');

const hostname = '127.0.0.1';
const port = 1245;
const data = process.argv[2];

const app = http.createServer( async (request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');

    const url = request.url;

    if (url === '/') {
        response.write('Hello Holberton School!');
    } else if (url === '/students') {
        response.write('This is the list of our students\n');
        try {
            const students = await countStudents(data);
            response.end(`${students.join('\n')}`);
        } catch (error) {
            response.end(`${error.name}: ${error.message}`);
        }
    }
    response.end();
});

app.listen(port, hostname, () => {});
module.exports = app;