export default function appendToEachArrayValue(array, appendString) {
  const Myarray = [];
  for (const idx of array) {
    Myarray.push(appendString + idx);
  }

  return Myarray;
}
