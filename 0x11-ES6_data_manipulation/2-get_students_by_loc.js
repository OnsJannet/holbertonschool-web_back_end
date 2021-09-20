export default function getStudentsByLocation(StudentList, city) {
  return StudentList.filter((student) => student.location === city);
}
