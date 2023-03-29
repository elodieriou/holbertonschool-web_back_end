const fs = require("fs");

function countStudents(database_file) {
    let data;

    try {
        data = fs.readFileSync(database_file, 'utf-8');
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
        if(!speciality.includes(elements)) {
            speciality.push(elements);
        }
    });

    const studentsInCS = students.filter((element) => element[3] === speciality[0]);
    const namesCS = [];
    studentsInCS.forEach((student) => {
        namesCS.push(student[0]);
    });
    console.log(`Number of students in ${speciality[0]}: ${studentsInCS.length}. List: ${namesCS.join(', ')}`);

    const studentsInSWE = students.filter((element) => element[3] === speciality[1]);
    const namesSWE = [];
    studentsInSWE.forEach((student) => {
        namesSWE.push(student[0]);
    });
    console.log(`Number of students in ${speciality[1]}: ${studentsInSWE.length}. List: ${namesSWE.join(', ')}`);
}

module.exports = countStudents;
