export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const findGrade = newGrades.find((newGrade) => newGrade.studentId === student.id);
      return { ...student, grade: findGrade ? findGrade.grade : 'N/A' };
    });
}
