let { lookupChar } = require('./charLookUp');
let { expect } = require('chai');


describe('Test lookupChar program', function () {
    it('should return undefined if first arg is NOT a string', function () {
        expect(lookupChar([1, 2, 3], 1)).to.be.undefined;
    });
    it('should return undefined if second arg is NOT an integer', function () {
        expect(lookupChar('text', 1.5)).to.be.undefined;
    });
    it('should return "Incorrect index" index lower than 0', function () {
        expect(lookupChar('text', -1)).to.be.equal('Incorrect index');
    });
    it('should return "Incorrect index" index above string length', function () {
        expect(lookupChar('text', 4)).to.be.equal('Incorrect index');
    });
    it('should return first char', function () {
        expect(lookupChar('text', 0)).to.be.equal('t');
    });
    it('should return last char', function () {
        expect(lookupChar('text', 3)).to.be.equal('t');
    });
    it('should return "x" char', function () {
        expect(lookupChar('text', 2)).to.be.equal('x');
    });
});