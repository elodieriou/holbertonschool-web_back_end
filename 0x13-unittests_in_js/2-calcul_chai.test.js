const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

const { expect } = chai;

describe('calculateNumber', () => {
  it('should return the SUM of a and b arguments', () => {
    expect(calculateNumber('SUM', 1, 3)).equal(4);
    expect(calculateNumber('SUM', 1.4, 4.5)).equal(6);
    expect(calculateNumber('SUM', 1, -1)).equal(0);
  });

  it('should return the SUBTRACT of a and b arguments', () => {
    expect(calculateNumber('SUBTRACT', 3, 1)).equal(2);
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).equal(-4);
    expect(calculateNumber('SUBTRACT', -1, -1)).equal(0);
  });

  it('should return the DIVIDE of a and b arguments', () => {
    expect(calculateNumber('DIVIDE', 3, 1)).equal(3);
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).equal(0.2);
    expect(calculateNumber('DIVIDE', 2, 2)).equal(1);
  });

  it('should return Error if b is equal to 0', () => {
    expect(calculateNumber('DIVIDE', 3, 0)).equal('Error');
  });

  it('should throw an error if arguments a and b are not integers', () => {
    expect(() => calculateNumber('SUM', 1, 'holberton')).throws(
      TypeError, 'The a and b parameters must be integers',
    );
  });

  it('should throw an error if argument type is not a string', () => {
    expect(() => calculateNumber(true, 1, 2)).throws(
      TypeError, 'The type parameter must be a string',
    );
    expect(() => calculateNumber(1, 1, 5)).throws(
      TypeError, 'The type parameter must be a string',
    );
  });

  it('should throw an error if missing arguments', () => {
    expect(() => calculateNumber(1, 'school')).throws(
      Error, 'Missing arguments',
    );
    expect(() => calculateNumber('holberton school')).throws(
      Error, 'Missing arguments',
    );
  });

  it('should throw an error if invalid type', () => {
    expect(() => calculateNumber('SUMM', 1, 2)).throws(
      Error, 'The type parameter only accept SUM, SUBTRACT, or DIVIDE',
    );
  });
});
