function calculateNumber(type, a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined' || typeof type === 'undefined') {
    throw new Error('Missing arguments');
  }

  if (typeof type !== 'string') {
    throw new TypeError('The type parameter must be a string');
  }

  const arg1 = Math.round(a);
  const arg2 = Math.round(b);

  if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
    throw new TypeError('The a and b parameters must be integers');
  }

  switch (type) {
    case 'SUM':
      return arg1 + arg2;
    case 'SUBTRACT':
      return arg1 - arg2;
    case 'DIVIDE':
      return (arg2 === 0) ? 'Error' : arg1 / arg2;
    default:
      throw new Error('The type parameter only accept SUM, SUBTRACT, or DIVIDE');
  }
}

module.exports = calculateNumber;
