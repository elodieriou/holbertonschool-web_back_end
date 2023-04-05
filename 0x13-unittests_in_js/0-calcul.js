function calculateNumber(a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined') {
    throw new Error('Missing arguments');
  }

  const arg1 = Math.round(a);
  const arg2 = Math.round(b);

  if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
    throw new TypeError('Parameters must be integers');
  }

  return arg1 + arg2;
}

module.exports = calculateNumber;
