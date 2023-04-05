const chai = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

const { expect } = chai;

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise when success is true', () => (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
