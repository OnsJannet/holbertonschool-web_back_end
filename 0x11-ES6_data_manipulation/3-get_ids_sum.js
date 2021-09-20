export default function getStudentIdsSum(StudentList) {
  return StudentList.reduce((previousValue, student) => previousValue + student.id, 0);
}
