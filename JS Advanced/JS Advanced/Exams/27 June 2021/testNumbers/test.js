let { expect } = require('chai');

const testNumbers = {
    sumNumbers: function (num1, num2) {
        let sum = 0;

        if (typeof (num1) !== 'number' || typeof (num2) !== 'number') {
            return undefined;
        } else {
            sum = (num1 + num2).toFixed(2);
            return sum
        }
    },
    numberChecker: function (input) {
        input = Number(input);

        if (isNaN(input)) {
            throw new Error('The input is not a number!');
        }

        if (input % 2 === 0) {
            return 'The number is even!';
        } else {
            return 'The number is odd!';
        }

    },
    averageSumArray: function (arr) {

        let arraySum = 0;

        for (let i = 0; i < arr.length; i++) {
            arraySum += arr[i]
        }

        return arraySum / arr.length
    }
};


describe("Tests …", function () {
    describe("sumNumbers FUNC TESTS", function () {
        it("invalid type for first arg", function () {
            expect(testNumbers.sumNumbers('invalid', 1)).to.be.undefined
        });
        it("invalid type for second arg", function () {
            expect(testNumbers.sumNumbers(1, 'invalid')).to.be.undefined
        });
        it("invalid type for args", function () {
            expect(testNumbers.sumNumbers('invalid', 'invalid')).to.be.undefined
        });
        it("valid args, positives", function () {
            expect(testNumbers.sumNumbers(1, 2)).to.equal('3.00');
        });
        it("valid args, negatives", function () {
            expect(testNumbers.sumNumbers(-1, -2)).to.equal('-3.00');
        });
        it("valid args, positive/negative", function () {
            expect(testNumbers.sumNumbers(5, -2)).to.equal('3.00');
        });
        it("valid args, negative/positive", function () {
            expect(testNumbers.sumNumbers(-5, 2)).to.equal('-3.00');
        });
        it("valid args, zeros", function () {
            expect(testNumbers.sumNumbers(0, 0)).to.equal('0.00');
        });
    });
    describe("numberChecker FUNC TESTS", function () {
        it("invalid type, throw error", function () {
            expect(() => { testNumbers.numberChecker('invalid') }).
                to.throw('The input is not a number!')
        });

        it("even num", function () {
            expect(testNumbers.numberChecker(2)).to.equal('The number is even!');
        });

        it("odd num", function () {
            expect(testNumbers.numberChecker(1)).to.equal('The number is odd!');
        });

        it("even num", function () {
            expect(testNumbers.numberChecker(0)).to.equal('The number is even!');
        });

    });
    describe("averageSumArray FUNC TESTS", function () {
        it("valid [1, 2, 3]", function () {
            expect(testNumbers.averageSumArray([1, 2, 3])).to.equal(2);
        });
        it("valid [] NAN", function () {
            expect(testNumbers.averageSumArray([])).to.be.NaN;
        });
        it("valid [-1, -2, -3]", function () {
            expect(testNumbers.averageSumArray([-1, -2, -3])).to.equal(-2);
        });
        it("valid [1]", function () {
            expect(testNumbers.averageSumArray([1])).to.equal(1);
        });
    });
});


