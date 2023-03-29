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

    const studentsInCS = [];
    students.filter((element) => element[3] === speciality[0]).forEach((student) => {
        studentsInCS.push(student[0]);
    });
    console.log(`Number of students in ${speciality[0]}: 6. List: ${studentsInCS.join(', ')}`);

    const studentsInSWE = [];
    students.filter((element) => element[3] === speciality[1]).forEach((student) => {
        studentsInSWE.push(student[0]);
    });
    console.log(`Number of students in ${speciality[1]}: 4. List: ${studentsInSWE.join(', ')}`);
}

module.exports = countStudents;
