let { createCalculator } = require('./addSubtract');
const { expect } = require('chai');

// TODO https://youtu.be/gzQ1_-KKPRQ?t=10433 = new instance every test. 
describe('07. Add/Subtract Test', () => { // packet s testove suite
    it('should be object type', () => {
        expect(createCalculator()).to.be.an('object');
    });
    it('check if object has add, subtract and get methods(properties)', () => {
        let calc = createCalculator();
        //By default, both own and inherited properties are included.
        // Add .own earlier in the chain to exclude inherited properties from the search.
        // to.have.property , checks inherited properties also
        expect(calc).to.have.own.property('add');
        expect(calc).to.have.own.property('subtract');
        expect(calc).to.have.own.property('get');
        // expect(calc).to.has.ownProperty('get'); viktor style
    });
    it('internal sum should not be ABLE to be modified closure', () => {
        let calc = createCalculator();
        calc.value += 2;
        expect(calc.get()).to.equal(0);
        // expect(createCalculator().value).to.equal(undefined);
    });
    it('check add function with int', () => {
        let calc = createCalculator();
        calc.add(2);
        expect(calc.get()).to.equal(2);

    });
    it('check add function with string num', () => {
        let calc = createCalculator();
        calc.add('3');
        expect(calc.get()).to.equal(3);

    });
    it('check subtract function with int', () => {
        let calc = createCalculator();
        calc.subtract(2);
        expect(calc.get()).to.equal(-2);

    });
    it('check subtract function with string num', () => {
        let calc = createCalculator();
        calc.subtract('3');
        expect(calc.get()).to.equal(-3);

    });
    it('check get function', () => {
        let calc = createCalculator();
        expect(calc.get()).to.equal(0);

    });
});