import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response, file) {
    response.write('This is the list of our students\n');

    const studentsBySpe = [];
    readDatabase(file)
      .then((data) => {
        Object.entries(data).sort().forEach(([key, values]) => {
          studentsBySpe.push(`Number of students in ${key}: ${values.length}. List: ${values.join(', ')}`);
        });
        response.status(200);
        response.send(`${studentsBySpe.join('\n')}`);
      })
      .catch((error) => {
        response.status(500);
        response.send(error.message);
      });
  }

  static getAllStudentsByMajor(request, response, file) {
    const { major } = request.params;
    if (!major.includes('CS') && !major.includes('SWE')) {
      response.status(500);
      response.send('Major parameter must be CS or SWE');
    }
    readDatabase(file)
      .then((data) => {
        response.status(200);
        response.send(`List: ${data[major].join(', ')}`);
      })
      .catch((error) => {
        response.status(500);
        response.send(error.message);
      });
  }
}
export default StudentsController;
