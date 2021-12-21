let { isOddOrEven } = require('./isOddOrEven');
let { expect } = require('chai');

describe('Test odd or even program', function() {
    it('returns undefined if type is NOT string', function() {
        expect(isOddOrEven([1, 2 ,3])).to.be.undefined;
    });
    it('returns even', function() {
        expect(isOddOrEven('hello!')).to.equal('even');
    });
    it('returns even-empty string', function() {
        expect(isOddOrEven('')).to.equal('even');
    });
    it('returns odd', function() {
        expect(isOddOrEven('hello')).to.equal('odd');
    });
});