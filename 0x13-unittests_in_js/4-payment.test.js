const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should call the Utils.calculateNumber with the correct parameters', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    sinon.assert.calledOnce(calculateNumberSpy);
    sinon.assert.calledWith(calculateNumberSpy, 'SUM', 100, 20);

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
