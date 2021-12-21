let { PaymentPackage } = require('./paymentPackage');
let { expect } = require('chai');


describe('Test PaymentPackage Class', function () {
    // let paymentPackage;
    // beforeEach(() => {
    //     paymentPackage = new PaymentPackage();
    // })

    it('Constructor - can be initialized with two parameters - string name, number value.', function () {
        let paymentPackage = new PaymentPackage('HR Services', 800);

        expect(paymentPackage).to.be.an.instanceof(PaymentPackage);

        expect(paymentPackage).to.have.own.property('_name');
        expect(paymentPackage._name).to.equal('HR Services');

        expect(paymentPackage).to.have.own.property('_value');
        expect(paymentPackage._value).to.equal(800);

        expect(paymentPackage).to.have.own.property('_VAT');
        expect(paymentPackage._VAT).to.equal(20);

        expect(paymentPackage).to.have.own.property('_active');
        expect(paymentPackage._active).to.equal(true);



    });
    describe('TESTS FOR NAME INPUTS', function () {
        it('should throw error Name must be a non-empty string, int', function () {
            expect(() => new PaymentPackage(1, 800)).to.throw('Name must be a non-empty string');
        });

        it('should throw error Name must be a non-empty string, empty string', function () {
            expect(() => new PaymentPackage('', 800)).to.throw('Name must be a non-empty string');
        });

        it('should throw error Name must be a non-empty string, arr with string', function () {
            expect(() => new PaymentPackage(['abc'], 800)).to.throw('Name must be a non-empty string');
        });

        it('Should return the new Name if the input is good', () => {
            expect(() => new PaymentPackage('abc', 800)).not.to.throw('Name must be a non-empty string');
        });

        it('VALID INPUT FOR NAME, CHECK DOES IT HAVE IT AND DOES IT EQUAL TO.', () => {
            let paymentPackage = new PaymentPackage('HR Services', 800);
            expect(paymentPackage).to.have.own.property('_name');
            expect(paymentPackage._name).to.equal('HR Services');
        });
    });

    describe('TESTS FOR VALUE INPUTS', function () {
        it('should throw error Value must be a non-negative number, string', function () {
            expect(() => new PaymentPackage('valid', 'invalid')).to.throw('Value must be a non-negative number');
        });

        it('should throw error Value must be a non-negative number, negative number', function () {
            expect(() => new PaymentPackage('valid', -1)).to.throw('Value must be a non-negative number');
        });

        it('should throw error Value must be a non-negative number, arr', function () {
            expect(() => new PaymentPackage('valid', [-1])).to.throw('Value must be a non-negative number');
        });

        it('Should return the new value if the input is good', () => {
            expect(() => new PaymentPackage('abc', 800)).not.to.throw('Value must be a non-negative number');
        });

        it('VALID INPUT FOR VALUE, CHECK DOES IT HAVE IT AND DOES IT EQUAL TO ZERO', () => {
            let paymentPackage = new PaymentPackage('HR Services', 0);
            expect(paymentPackage).to.have.own.property('_value');
            expect(paymentPackage._value).to.equal(0);
            expect(paymentPackage.value).to.equal(0);
        });

    });

    describe('TESTS FOR VAT INPUTS', function () {
        it('should throw error VAT must be a non-negative number, string', function () {
            expect(() => new PaymentPackage('valid', 1800).VAT = 'invalid').to.throw('VAT must be a non-negative number');
        });

        it('should throw error VAT must be a non-negative number, negative number', function () {
            expect(() => new PaymentPackage('valid', 1800).VAT = -1).to.throw('VAT must be a non-negative number');
        });

        it('should throw error VAT must be a non-negative number, arr', function () {
            expect(() => new PaymentPackage('valid', 1800).VAT = [-1]).to.throw('VAT must be a non-negative number');
        });

        it('Should NOT throw error, the input is valid', function () {
            expect(() => new PaymentPackage('valid', 1800).VAT = 30).not.to.throw('VAT must be a non-negative number');
        });


        it('VALID INPUT FOR VAT, CHECK DOES IT HAVE IT AND DOES IT EQUAL TO ZERO', () => {
            let paymentPackage = new PaymentPackage('HR Services', 800);
            paymentPackage.VAT = 0;
            expect(paymentPackage).to.have.own.property('_VAT');
            expect(paymentPackage._VAT).to.equal(0);
            expect(paymentPackage.VAT).to.equal(0);
        });

    });

    describe('TESTS FOR ACTIVE INPUTS', function () {
        it('should throw error Active status must be a boolean, string', function () {
            expect(() => new PaymentPackage('valid', 1800).active = 'invalid').to.throw('Active status must be a boolean');
        });

        it('should throw error Active status must be a boolean, negative number', function () {
            expect(() => new PaymentPackage('valid', 1800).active = -1).to.throw('Active status must be a boolean');
        });

        it('should throw error Active status must be a boolean, arr', function () {
            expect(() => new PaymentPackage('valid', 1800).active = [-1]).to.throw('Active status must be a boolean');
        });

        it('Should NOT throw error, the input is valid', function () {
            expect(() => new PaymentPackage('valid', 1800).active = false).not.to.throw('Active status must be a boolean');
        });


        it('VALID INPUT FOR ACTIVE, CHECK DOES IT IF HAVE IT AND DOES IT EQUAL TO FALSE', () => {
            let paymentPackage = new PaymentPackage('HR Services', 800);
            paymentPackage.active = false;
            expect(paymentPackage).to.have.own.property('_active');
            expect(paymentPackage._active).to.equal(false);
            expect(paymentPackage.active).to.equal(false);
        });

    });

    describe('tests for toString', function () {

        it('test when active prop is true', function () {
            let paymentPackage = new PaymentPackage('name', 800);

            expect(paymentPackage.toString()).to.equal('Package: name\n- Value (excl. VAT): 800\n- Value (VAT 20%): 960');
        });

        it('test when active prop is true, vat = 30', function () {
            let paymentPackage = new PaymentPackage('name', 800);
            paymentPackage.VAT = 30;
            expect(paymentPackage.toString()).to.equal('Package: name\n- Value (excl. VAT): 800\n- Value (VAT 30%): 1040');
        });

        it('test when active prop is false', function () {
            let paymentPackage = new PaymentPackage('name', 800);
            paymentPackage.active = false;

            expect(paymentPackage.toString()).to.equal('Package: name (inactive)\n- Value (excl. VAT): 800\n- Value (VAT 20%): 960');
        });

        it('test when active prop is false, vat = 30', function () {
            let paymentPackage = new PaymentPackage('name', 800);
            paymentPackage.active = false;
            paymentPackage.VAT = 30;

            expect(paymentPackage.toString()).to.equal('Package: name (inactive)\n- Value (excl. VAT): 800\n- Value (VAT 30%): 1040');
        });
    });

});