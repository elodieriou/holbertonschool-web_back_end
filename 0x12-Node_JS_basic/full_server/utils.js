const fs = require('fs');
function readDatabase(file) {
    return new Promise((resolve, reject) => {

        fs.readFile(file, 'utf-8', (error, data) => {
            if (error) {
                reject(Error('Cannot load the database'));

            } else {
                const removeNewLine = data.split('\n');
                removeNewLine.shift();

                const students = removeNewLine.filter((element) => element).map((students) => students.split(','));
                const studentsBySeciality = students.reduce((accumulator, student) => {
                    const [firstName, lastName, age, spe] = student;
                    if (!accumulator[spe]) {
                        accumulator[spe] = [];
                    }
                    accumulator[spe].push(firstName);
                    return accumulator;
                }, {});

                const sortedSpeciality = Object.fromEntries(
                    Object.entries(studentsBySeciality)
                        .sort(([keyA], [keyB]) => keyA.localeCompare(keyB, 'en', { sensitivity: 'base' }))
                );
                resolve(sortedSpeciality);
            }
        });
    });
}

module.exports = readDatabase;
