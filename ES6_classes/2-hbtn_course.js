export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Students must be a array of strings');
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    this._name = name;
  }

  set length(length) {
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students)) throw TypeError('Students must be a array of strings');
    this._students = students;
  }
}
