let { expect } = require('chai');

let dealership = {
    newCarCost: function (oldCarModel, newCarPrice) {

        let discountForOldCar = {
            'Audi A4 B8': 15000,
            'Audi A6 4K': 20000,
            'Audi A8 D5': 25000,
            'Audi TT 8J': 14000,
        }

        if (discountForOldCar.hasOwnProperty(oldCarModel)) {
            let discount = discountForOldCar[oldCarModel];
            let finalPrice = newCarPrice - discount;
            return finalPrice;
        } else {
            return newCarPrice;
        }
    },

    carEquipment: function (extrasArr, indexArr) {
        let selectedExtras = [];
        indexArr.forEach(i => {
            selectedExtras.push(extrasArr[i])
        });

        return selectedExtras;
    },

    euroCategory: function (category) {
        if (category >= 4) {
            let price = this.newCarCost('Audi A4 B8', 30000);
            let total = price - (price * 0.05)
            return `We have added 5% discount to the final price: ${total}.`;
        } else {
            return 'Your euro category is low, so there is no discount from the final price!';
        }
    }
}
// dealership.newCarCost('Audi TT 8J', 30000);

describe('tests', function () {
    describe('newCarCost func tests', function () {
        it('test discount Audi A4 B8', function () {
            expect(dealership.newCarCost('Audi A4 B8', 30000)).to.equal(15000);
        });
        it('test discount Audi A6 4K', function () {
            expect(dealership.newCarCost('Audi A6 4K', 30000)).to.equal(10000);
        });
        it('test discount Audi A8 D5', function () {
            expect(dealership.newCarCost('Audi A8 D5', 30000)).to.equal(5000);
        });
        it('test discount Audi TT 8J', function () {
            expect(dealership.newCarCost('Audi TT 8J', 30000)).to.equal(16000);
        });
        it('test car NO DISCOUNT Audi Q7', function () {
            expect(dealership.newCarCost('Audi Q7', 30000)).to.equal(30000);
        });
    });
    describe('carEquipment func tests', function () {
        it('test 2 extras - 2 taken', function () {
            expect(dealership.carEquipment(['heated seats', 'navigation'], [0, 1])).to.eql(['heated seats', 'navigation']);
        })
        it('test 2 extras - 1 taken', function () {
            expect(dealership.carEquipment(['heated seats', 'navigation'], [0])).to.eql(['heated seats']);
        })
        it('test 2 extras - 0 taken', function () {
            expect(dealership.carEquipment(['heated seats', 'navigation'], [])).to.eql([]);
        })
        it('test 0 extras - 0 taken', function () {
            expect(dealership.carEquipment([], [])).to.eql([]);
        })
        it('test 0 extras - 1 taken', function () {
            expect(dealership.carEquipment([], [0])).to.eql([undefined]);
        })
    });
    describe('euroCategory func tests', function () {
        it('test good euro category', function () {
            expect(dealership.euroCategory(4)).to.equal('We have added 5% discount to the final price: 14250.');
        });
        it('test bad euro category', function () {
            expect(dealership.euroCategory(3)).to.equal('Your euro category is low, so there is no discount from the final price!');
        });
    });
})