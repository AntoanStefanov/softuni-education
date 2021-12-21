let { expect } = require('chai');

const numberOperations = {
    powNumber: function (num) {
        return num * num;
    },
    numberChecker: function (input) {
        input = Number(input);

        if (isNaN(input)) {
            throw new Error('The input is not a number!');
        }

        if (input < 100) {
            return 'The number is lower than 100!';
        } else {
            return 'The number is greater or equal to 100!';
        }
    },
    sumArrays: function (array1, array2) {

        const longerArr = array1.length > array2.length ? array1 : array2;
        const rounds = array1.length < array2.length ? array1.length : array2.length;

        const resultArr = [];

        for (let i = 0; i < rounds; i++) {
            resultArr.push(array1[i] + array2[i]);
        }

        resultArr.push(...longerArr.slice(rounds));

        return resultArr
    }
};


describe('Tests...', function () {
    describe('powNumber func - no need validation', function () {
        it('valid input', function () {
            expect(numberOperations.powNumber(2)).to.equal(4);
        });

        it('valid input', function () {
            expect(numberOperations.powNumber(1)).to.equal(1);
        });

        it('valid input', function () {
            expect(numberOperations.powNumber(-3)).to.equal(9);
        });

        it('valid input', function () {
            expect(numberOperations.powNumber(0)).to.equal(0);
        });
    });

    describe('numberChecker func', function () {
        it('invalid input', function () {
            expect(() => numberOperations.numberChecker('invalid')).to.throw('The input is not a number!');
        });

        it('invalid input', function () {
            expect(() => numberOperations.numberChecker([1])).to.throw('The input is not a number!');
        });

        it('invalid input', function () {
            expect(() => numberOperations.numberChecker('1')).to.throw('The input is not a number!');
        });
        it('valid lower than 100', function () {
            expect(numberOperations.numberChecker(99)).to.equal('The number is lower than 100!');
        });

        it('valid greater or equal than 100', function () {
            expect(numberOperations.numberChecker(100)).to.equal('The number is greater or equal to 100!');
        });

        it('valid greater or equal than 100', function () {
            expect(numberOperations.numberChecker(101)).to.equal('The number is greater or equal to 100!');
        });
    });

    describe('sumArrays func', function () {
        it('valid second arg larger', function () {
            expect(numberOperations.sumArrays([1, 2, 3], [1, 2, 3, 4])).to.eql([2, 4, 6, 4]);
        });
        it('valid first arg larger', function () {
            expect(numberOperations.sumArrays([1, 2, 3, 4], [1, 2, 3])).to.eql([2, 4, 6, 4]);
        });
        it('valid equal', function () {
            expect(numberOperations.sumArrays([1, 2, 3], [1, 2, 3])).to.eql([2, 4, 6]);
        });
    });
});