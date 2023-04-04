function calculateNumber(a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined') {
    throw new Error('Missing arguments');
  }

  const arg1 = Number(a);
  const arg2 = Number(b);

  if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
    throw new TypeError('Parameters must be integers');
  }

  return Math.ceil(arg1 + arg2);
}

module.exports = calculateNumber;
