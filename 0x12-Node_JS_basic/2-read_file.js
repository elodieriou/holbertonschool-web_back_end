const fs = require('fs');

function countStudents(file) {
  let data;

  try {
    data = fs.readFileSync(file, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const removeNewLine = data.split('\n');
  removeNewLine.shift();
  const students = removeNewLine.filter((element) => element).map((students) => students.split(','));
  console.log(`Number of students: ${students.length}`);

  const speciality = [];
  students.forEach((student) => {
    const elements = student[3];
    if (!speciality.includes(elements)) {
      speciality.push(elements);
    }
  });

  speciality.forEach((spe) => {
    const studentsBySpe = students.filter((element) => element[3] === spe);
    const namesStudents = [];
    studentsBySpe.forEach((student) => {
      namesStudents.push(student[0]);
    });
    console.log(`Number of students in ${spe}: ${studentsBySpe.length}. List: ${namesStudents.join(', ')}`);
  });
}

module.exports = countStudents;
