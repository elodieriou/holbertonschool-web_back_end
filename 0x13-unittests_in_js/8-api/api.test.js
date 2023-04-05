const chai = require('chai');
const request = require('request');

const { expect } = chai;

describe('basic integration testing', () => {
  const options = {
    url: 'http://localhost:7865',
    method: 'GET',
  };

  it('should return a statuscode 200', () => (done) => {
    request(options, (response) => {
      expect(response.statusCode).equal(200);
      done();
    });
  });

  it('should return the body', () => (done) => {
    request(options, (body) => {
      expect(body).equal('Welcome to the payment system');
      done();
    });
  });
});
