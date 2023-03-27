export default function getStudentsByLocation(students, city) {
  return students.filter((s) => s.location === city);
}
