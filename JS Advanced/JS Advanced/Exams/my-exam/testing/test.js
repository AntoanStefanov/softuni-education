let { expect } = require('chai');


const library = {
    calcPriceOfBook(nameOfBook, year) {
        let price = 20;
        if (typeof nameOfBook != "string" || !Number.isInteger(year)) {
            throw new Error("Invalid input");
        } else if (year <= 1980) {
            let total = price - (price * 0.5);
            return `Price of ${nameOfBook} is ${total.toFixed(2)}`;
        }
        return `Price of ${nameOfBook} is ${price.toFixed(2)}`;
    },

    findBook: function (booksArr, desiredBook) {
        if (booksArr.length == 0) {
            throw new Error("No books currently available");
        } else if (booksArr.find(e => e == desiredBook)) {
            return "We found the book you want.";
        } else {
            return "The book you are looking for is not here!";
        }

    },
    arrangeTheBooks(countBooks) {
        const countShelves = 5;
        const availableSpace = countShelves * 8; // 40 mesta

        if (!Number.isInteger(countBooks) || countBooks < 0) {
            throw new Error("Invalid input");
        } else if (availableSpace >= countBooks) {
            return "Great job, the books are arranged.";
        } else {
            return "Insufficient space, more shelves need to be purchased.";
        }
    }

};

describe('Tests...', function () {
    describe('calcPriceOfBook func', function () {
        it('invalid book input', function () {
            expect(() => library.calcPriceOfBook(['invalid'], 1980)).to.throw('Invalid input');
        });
        it('invalid book input', function () {
            expect(() => library.calcPriceOfBook(2, 1980)).to.throw('Invalid input');
        });
        it('invalid year input', function () {
            expect(() => library.calcPriceOfBook('valid', 4.2)).to.throw('Invalid input');
        });
        it('invalid year input', function () {
            expect(() => library.calcPriceOfBook('valid', 'invalid')).to.throw('Invalid input');
        });
        it('invalid year input', function () {
            expect(() => library.calcPriceOfBook('valid', '4.2')).to.throw('Invalid input');
        });

        it('invalid year input', function () {
            expect(() => library.calcPriceOfBook(['invalid'], '4.2')).to.throw('Invalid input');
        });

        it('valid inputs discount', function () {
            expect(library.calcPriceOfBook('book', 1980)).to.equal('Price of book is 10.00');
        });
        it('valid inputs discount', function () {
            expect(library.calcPriceOfBook('book', 1979)).to.equal('Price of book is 10.00');
        });
        it('valid inputs NO discount', function () {
            expect(library.calcPriceOfBook('book', 1981)).to.equal('Price of book is 20.00');
        });


    });

    describe('findBook func', function () {
        it('invalid input', function () {
            expect(() => library.findBook([])).to.throw('No books currently available');
        });

        it('valid inputs', function () {
            expect(library.findBook(['book', 'bookTwo'], 'bookTwo')).to.equal("We found the book you want.");
        });
        it('valid inputs', function () {
            expect(library.findBook(['book', 'bookTwo'], 'book')).to.equal("We found the book you want.");
        });

        it('valid inputs', function () {
            expect(library.findBook(['book', 'bookTwo'], 'NotThere')).to.equal("The book you are looking for is not here!");
        });
    });

    describe('arrangeTheBooks func', function () {

        it('invalid input', function () {
            expect(() => library.arrangeTheBooks(-1)).to.throw("Invalid input");
        });

        it('invalid input', function () {
            expect(() => library.arrangeTheBooks(4.2)).to.throw("Invalid input");
        });
        it('invalid input', function () {
            expect(() => library.arrangeTheBooks('4.2')).to.throw("Invalid input");
        });

        it('invalid input', function () {
            expect(() => library.arrangeTheBooks(-4.2)).to.throw("Invalid input");
        });

        it('enough space', function () {
            expect(library.arrangeTheBooks(40)).to.equal("Great job, the books are arranged.")
        })
        it('enough space', function () {
            expect(library.arrangeTheBooks(39)).to.equal("Great job, the books are arranged.")
        })

        it('NOT enough space', function () {
            expect(library.arrangeTheBooks(41)).to.equal("Insufficient space, more shelves need to be purchased.");
        })
    });
});

