const sinon = require('sinon');
const mocha = require('mocha');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;

  mocha.beforeEach(() => {
    consoleLogSpy = sinon.spy(console, 'log');
  });

  mocha.afterEach(() => {
    consoleLogSpy.restore();
  });

  it('should log the correct total for 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 120');
  });

  it('should log the correct total for 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    sinon.assert.calledOnce(consoleLogSpy);
    sinon.assert.calledWith(consoleLogSpy, 'The total is: 20');
  });
});
