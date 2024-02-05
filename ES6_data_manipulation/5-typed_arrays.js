export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const int8 = new Int8Array(length);
  int8[position] = value;
  const { buffer } = int8;
  const int8typedarray = new DataView(buffer, 0, length);

  return int8typedarray;
}
