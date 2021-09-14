export default function guardrail(mathFunction) {
  const queue = [];
  let value;
  try {
    value = mathFunction();
  } catch (error) {
    value = `${error.name}: ${error.message}`;
  }
  queue.push(value);
  queue.push('Guardrail was processed');
  return queue;
}
