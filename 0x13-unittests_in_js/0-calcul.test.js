const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should return integer', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, -3), -2);
    assert.strictEqual(calculateNumber(1, -1), 0);
  });

  it('should return rounded float', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should cast into integer', () => {
    assert.strictEqual(calculateNumber(1, '3'), 4);
    assert.strictEqual(calculateNumber(1, true), 2);
  });

  it('should throw an error if arguments are not integers', () => {
    assert.throws(() => calculateNumber(1, 'holberton'), {
      name: 'TypeError',
      message: 'Parameters must be integers',
    });
  });

  it('should throw an error if missing one argument', () => {
    assert.throws(() => calculateNumber('school'), {
      name: 'Error',
      message: 'Missing arguments',
    });
  });
});
