const chai = require('chai');
const request = require('request');

const { expect } = chai;

describe('basic integration testing', () => {
  it('should return a statuscode 200', (done) => {
    const options = {
      url: 'http://localhost:7865',
      method: 'GET'
    }
    request('http://localhost:7865', (error, response) => {
      expect(response.statusCode).equal(200);
      done();
    });
  });

  it('should return the body', (done) => {
    const options = {
      url: 'http://localhost:7865',
      method: 'GET'
    }
    request(options, (error, response, body) => {
      expect(body).equal('Welcome to the payment system');
      done();
    });
  });

  it('should request the method GET', (done) => {
    const options = {
      url: 'http://localhost:7865',
      method: 'GET'
    }
    request(options, (error, response) => {
      expect(response.request.method).equal('GET');
      done();
    });
  });
});

describe('GET /cart/ID route testing', () => {
  it('should return a 200 status code for a valid ID', (done) => {
    const options = {
      url: 'http://localhost:7865/cart/12',
      method: 'GET'
    }
    request('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).equal(200);
      expect(body).equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return a 404 status code for invalid ID', (done) => {
    const options = {
      url: 'http://localhost:7865/cart/hello',
      method: 'GET'
    }
    request(options, (error, response, body) => {
      expect(response.statusCode).equal(404);
      done();
    });
  });
});

describe('GET /available_payments route testing', () => {
  it('should return a 200 status code and the object', (done) => {
    const options = {
      url: 'http://localhost:7865/available_payments',
      method: 'GET'
    }
    request(options, (error, response, body) => {
      const expected = {
        payment_methods: {
          credit_cards: true,
          paypal: false,
        }
      }
      const actual = JSON.parse(body);
      expect(actual).to.deep.equal(expected);
      expect(response.statusCode).equal(200);
      done();
    });
  });
});

describe('POST /login route testing', () => {
  it('should return the status code 200 and the correct username', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {
        userName: 'Betty'
      }
    }
    request(options, (error, response, body) => {
      expect(body).equal(`Welcome ${options.json.userName}`);
      expect(response.statusCode).equal(200);
      done();
    });
  });

  it('should return the status 200 but username is undefined', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST'
    }
    request(options, (error, response, body) => {
      expect(body).equal('Welcome undefined');
      expect(response.statusCode).equal(200);
      done();
    })
  })
});
