export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const int8 = new Int8Array(length);
  int8[position] = value;

  const { buffer } = int8;
  const newView = new DataView(buffer, 0, length);

  return newView;
}
