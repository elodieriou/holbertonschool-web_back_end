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

  it('should always return 10 and verify that log the message with returns value', (done) => {
    const calculateNumberSpy = sinon.stub(Utils, 'calculateNumber');
    calculateNumberSpy.returns(10);

    const consoleLogSpy = sinon.stub(console, 'log');
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 10');

    calculateNumberSpy.restore();
    consoleLogSpy.restore();
    done();
  });
});
