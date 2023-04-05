const sinon = require('sinon');
const chai = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
  it('should call the Utils.calculateNumber and result is equal to call sendPaymentRequestToApi', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const expected = Utils.calculateNumber('SUM', 100, 20);
    const actual = sendPaymentRequestToApi(100, 20);

    expect(actual).equal(expected);
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).equal(true);

    calculateNumberSpy.restore();
  });

  it('should call the Utils.calculateNumber and displays console.log', () => {
    const consoleLogSpy = sinon.stub(console, 'log');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 120');

    consoleLogSpy.restore();
  });

  it('should call the Utils.calculateNumber and returns the sum', () => {
    const returnSpy = sinon.stub(Utils, 'calculateNumber');
    returnSpy.returns(120);

    returnSpy.restore();
  });
});