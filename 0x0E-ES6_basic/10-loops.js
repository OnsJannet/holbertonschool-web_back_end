export default function appendToEachArrayValue(array, appendString) {
  const second = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    second[idx] = appendString + value;
  }

  return second;
}
