const Utils = {
  calculateNumber: (type, a, b) => {
    if (typeof a === 'undefined' || typeof b === 'undefined' || typeof type === 'undefined') {
      throw new Error('Missing arguments');
    }

    let arg1 = Number(a);
    let arg2 = Number(b);

    if (Number.isNaN(arg1) || Number.isNaN(arg2)) {
      throw new TypeError('The a and b parameters must be integers');
    }

    if (typeof type !== 'string') {
      throw new TypeError('The type parameter must be a string');
    }

    arg1 = Math.round(arg1);
    arg2 = Math.round(arg2);

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
  },
};

module.exports = Utils;
