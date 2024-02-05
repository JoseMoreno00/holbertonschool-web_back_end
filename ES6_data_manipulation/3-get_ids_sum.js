export default function getStudentIdsSum(array) {
  return array.reduce((previousValue, student) => previousValue + student.id, 0);
}
