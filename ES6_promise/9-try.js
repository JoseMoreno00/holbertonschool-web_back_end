export default function guardrail(mathFunction) {
  let value = '';
  try {
    value = mathFunction();
  } catch (error) {
    value = error.toString();
  }
  const queue = [];
  queue.push(value);
  queue.push('Guardrail was processed');

  return queue;
}
