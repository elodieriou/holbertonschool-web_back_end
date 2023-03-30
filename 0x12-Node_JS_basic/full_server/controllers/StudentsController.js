import readDatabase from '../utils';
import process from 'process';

const file = process.argv[2];
class StudentsController {
    static getAllStudents(request, response) {
        response.write('This is the list of our students\n');

        const studentsBySpe = []
        readDatabase(file)
            .then((data) => {
                Object.entries(data).forEach(([key, values]) => {
                    studentsBySpe.push(`Number of students in ${key}: ${values.length}. List: ${values}`);
                });
                response.status(200);
                response.end(`${studentsBySpe.join('\n')}`);
            })
            .catch((error) => {
                response.status(500);
                response.end(error.message);
            });
    }

    static getAllStudentsByMajor(request, response) {
        const { major } = request.params;
        if (!major.includes('CS') && !major.includes('SWE')) {
            response.status(500);
            response.end('Major parameter must be CS or SWE');
        }
        readDatabase(file)
            .then((data) => {
                response.status(200);
                response.end(`List: ${data[major].join(', ')}`);
            })
            .catch((error) => {
                response.status(500);
                response.end('Cannot load the database');
            });
    }
}
export default StudentsController;
