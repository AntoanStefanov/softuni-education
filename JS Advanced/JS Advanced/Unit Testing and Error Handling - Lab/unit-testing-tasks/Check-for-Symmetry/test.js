let { expect } = require('chai');
let { isSymmetric } = require('./checkForSymmetry');


describe('05. Check for symmetry', function () {
    it('should return true, array is symmetric same element-string', function () {
        // expect(isSymmetric(['a', 'a', 'a', 'a'])).to.equal(true);
        expect(isSymmetric(['a', 'a', 'a', 'a'])).to.be.true;
    });
    it('should return true, array is symmetric same element-number', function () {
        expect(isSymmetric([1, 1, 1, 1])).to.equal(true);
    });
    it('should return true, array is symmetric different element', function () {
        expect(isSymmetric(['a', 'a', 'b', 'a', 'a'])).to.equal(true);
    });
    it('should return true, array is symmetric different element type', function () {
        expect(isSymmetric(['a', 'a', 1, 'a', 'a'])).to.equal(true);
    });
    it('should return true, array is symmetric one element', function () {
        expect(isSymmetric(['a'])).to.equal(true);
    });
    it('should return true, array is empty and symmetric', function () {
        expect(isSymmetric([])).to.equal(true);
    });
    // 2 test case judge
    it('should return false, array is type-different symmetric', function () {
        expect(isSymmetric([1, 2, '1'])).to.equal(false);
    });
    it('should return false, incorrect input-string', function () {
        expect(isSymmetric('incorrect type')).to.equal(false);
    });
    it('should return false, incorrect input-number', function () {
        expect(isSymmetric(1)).to.equal(false);
    });
    it('should return false, array is NOT symmetric', function () {
        expect(isSymmetric(['a', 'a', 'a', 'a', 'b'])).to.equal(false);
    });
});
