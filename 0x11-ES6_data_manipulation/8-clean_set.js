export default function cleanSet(set, startString) {
  let endresult = '';
  if (!startString || !startString.length) return endresult;
  set.forEach((element) => {
    if (element && element.startsWith(startString)) endresult += `${element.slice(startString.length)}-`;
  });
  return endresult.slice(0, endresult.length - 1);
}
