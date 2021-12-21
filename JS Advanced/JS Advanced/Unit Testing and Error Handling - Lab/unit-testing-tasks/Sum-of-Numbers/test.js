let { sum } = require('./sumNumbers');
const { expect } = require('chai');


describe('04. Sum Function Test', () => { // packet s testove suite
    it('array with numbers should return 10', () => {
        expect(sum([1, 2, 3, 4])).to.equal(10);
    });
    it('array with numbers and number in string type should return 15', () => {
        expect(sum([1, 2, 3, 4, '5'])).to.equal(15);
    });
    it('empty array should return 0', () => {
        expect(sum([])).to.equal(0);
    });
    it('passing no args should throw TypeError , because arr will be undefined, undefined is not iterable', () => {
        expect(sum).to.throw(TypeError);
    });
    it('string with numbers, iterable, expected 6', () => {
        expect(sum('123')).to.equal(6);
    });
});