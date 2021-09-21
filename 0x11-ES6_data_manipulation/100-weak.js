export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const Quries = weakMap.get(endpoint);
  if (Quries + 1 === 5) throw Error('Endpoint load is high');
  if (Quries) {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}
