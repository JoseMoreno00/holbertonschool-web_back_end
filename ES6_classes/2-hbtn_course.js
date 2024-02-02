export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Students must be an array');
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this.name;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this.name = newName;
  }

  get length() {
    return this.length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('Length must be a number');
    this.length = newLength;
  }

  get students() {
    return this.students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) throw TypeError('Students must be an array');
    this.students = newStudents;
  }
}
