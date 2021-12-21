let { mathEnforcer } = require('./mathEnforcer');
let { expect } = require('chai');

describe('Test mathEnforcer program', function () {

    // it('test if it has needed methods', function () {
    //     expect(mathEnforcer).to.have.own.property('addFive');
    //     expect(mathEnforcer).to.have.own.property('subtractTen');
    //     expect(mathEnforcer).to.have.own.property('sum');
    // });
    describe('Test invalid inputs', function () {
        it('test addFive invalid input', function () {
            expect(mathEnforcer.addFive('test')).to.be.undefined;
        });
        it('test subtractTen invalid input', function () {
            expect(mathEnforcer.subtractTen('test')).to.be.undefined;
        });
        it('test sum invalid first arg input', function () {
            expect(mathEnforcer.sum('test', 2)).to.be.undefined;
        });
        it('test sum invalid second arg input', function () {
            expect(mathEnforcer.sum(2, 'test')).to.be.undefined;
        });
        it('test sum both invalid input', function () {
            expect(mathEnforcer.sum('arg', 'test')).to.be.undefined;
        });
    });

    describe('test addFive method', function () {
        it('zero', function () {
            expect(mathEnforcer.addFive(0)).to.equal(5);
        });
        it('positive', function () {
            expect(mathEnforcer.addFive(10)).to.equal(15);
        });
        it('negative', function () {
            expect(mathEnforcer.addFive(-10)).to.equal(-5);
        });
        it('float positive', function () {
            expect(mathEnforcer.addFive(2.5)).closeTo(7.5, 0.01);
        });
    })

    describe('test subtractTen method', function () {
        it('zero', function () {
            expect(mathEnforcer.subtractTen(0)).to.equal(-10);
        });
        it('positive', function () {
            expect(mathEnforcer.subtractTen(10)).to.equal(0);
        });
        it('negative', function () {
            expect(mathEnforcer.subtractTen(-10)).to.equal(-20);
        });
        it('float positive', function () {
            expect(mathEnforcer.subtractTen(2.5)).closeTo(-7.5, 0.01);
        });
    })

    describe('test sum method', function () {
        it('zero', function () {
            expect(mathEnforcer.sum(0, 0)).to.equal(0);
        });
        it('positive', function () {
            expect(mathEnforcer.sum(10, 10)).to.equal(20);
        });
        it('negative', function () {
            expect(mathEnforcer.sum(-10, -10)).to.equal(-20);
        });
        it('float positive', function () {
            expect(mathEnforcer.sum(2.5, -2.5)).closeTo(0, 0.01);
        });
    })
});