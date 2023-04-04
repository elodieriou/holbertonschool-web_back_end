const sinon = require('sinon');
const chai = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const { expect } = chai;

describe('sendPaymentRequestToApi', () => {
  it('should call the Utils.calculateNumber with the correct parameters', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(calculateNumberSpy);
    sinon.assert.calledWith(calculateNumberSpy, 'SUM', 100, 20);

    calculateNumberSpy.restore();
  });

  it('should call the Utils.calculateNumber and result is equal to call sendPaymentRequestToApi', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    const sendPaymentRequestToApiSpy = sendPaymentRequestToApi(100, 20);

    expect(calculateNumberSpy('SUM', 100, 20)).equal(sendPaymentRequestToApiSpy);

    calculateNumberSpy.restore();
  });
});
