export default function guardrail(matchFunction) {
  const queue = [];

  try {
    queue.push(matchFunction());
  } catch (error) {
    queue.push(`${error.name}: ${error.message}`);
  }

  queue.push('Guardrail was processed');
  return queue;
}
