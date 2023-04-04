const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('should return the SUM of a and b arguments', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
  });

  it('should return the SUBTRACT of a and b arguments', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.strictEqual(calculateNumber('SUBTRACT', -1, -1), 0);
  });

  it('should return the DIVIDE of a and b arguments', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3, 1), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 2, 2), 1);
  });

  it('should return Error if b is equal to 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 3, 0), 'Error');
  });

  it('should throw an error if arguments a and b are not integers', () => {
    assert.throws(() => calculateNumber('SUM', 1, 'holberton'), {
      name: 'TypeError',
      message: 'The a and b parameters must be integers',
    });
  });

  it('should throw an error if argument type is not a string', () => {
    assert.throws(() => calculateNumber(true, 1, 2), {
      name: 'TypeError',
      message: 'The type parameter must be a string',
    });
    assert.throws(() => calculateNumber(1, 1, 5), {
      name: 'TypeError',
      message: 'The type parameter must be a string',
    });
  });

  it('should throw an error if missing arguments', () => {
    assert.throws(() => calculateNumber(1, 'school'), {
      name: 'Error',
      message: 'Missing arguments',
    });
    assert.throws(() => calculateNumber('holberton school'), {
      name: 'Error',
      message: 'Missing arguments',
    });
  });

  it('should throw an error if invalid type', () => {
    assert.throws(() => calculateNumber('SUMM', 1, 2), {
      name: 'Error',
      message: 'The type parameter only accept SUM, SUBTRACT, or DIVIDE',
    });
  });
});
