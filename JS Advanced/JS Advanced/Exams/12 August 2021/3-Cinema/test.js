// START 20:02:27 
// END 20:22:39 
let { expect } = require('chai');

const cinema = {
    showMovies: function (movieArr) {

        if (movieArr.length == 0) {
            return 'There are currently no movies to show.';
        } else {
            let result = movieArr.join(', ');
            return result;
        }

    },
    ticketPrice: function (projectionType) {

        const schedule = {
            "Premiere": 12.00,
            "Normal": 7.50,
            "Discount": 5.50
        }
        if (schedule.hasOwnProperty(projectionType)) {
            let price = schedule[projectionType];
            return price;
        } else {
            throw new Error('Invalid projection type.')
        }

    },
    swapSeatsInHall: function (firstPlace, secondPlace) {
        if (!Number.isInteger(firstPlace) || firstPlace <= 0 || firstPlace > 20 ||
            !Number.isInteger(secondPlace) || secondPlace <= 0 || secondPlace > 20 ||
            firstPlace === secondPlace) {
            return "Unsuccessful change of seats in the hall.";
        } else {
            return "Successful change of seats in the hall.";
        }

    }
};

describe("Tests …", function () {
    describe("showMovies FUNC", function () {
        it("ARR LENGTH 0", function () {
            expect(cinema.showMovies([])).to.equal('There are currently no movies to show.');
        });
        it("ARR LENGTH 2 ", function () {
            expect(cinema.showMovies(['Titanic', 'Musala'])).to.equal('Titanic, Musala');
        });
    });

    describe("ticketPrice FUNC", function () {
        it("CHECK PREMIERE", function () {
            expect(cinema.ticketPrice('Premiere')).to.equal(12.00);
        });
        it("CHECK Normal", function () {
            expect(cinema.ticketPrice('Normal')).to.equal(7.50);

        });
        it("CHECK Discount", function () {
            expect(cinema.ticketPrice('Discount')).to.equal(5.50);
        });
        it('NO SUCH SCHEDULE', function () {
            expect(() => cinema.ticketPrice('INVALID')).to.throw("Invalid projection type.");
        })
        it('NO SUCH SCHEDULE', function () {
            expect(() => cinema.ticketPrice(2)).to.throw("Invalid projection type.");
        })
    });

    describe("swapSeatsInHall FUNC", function () {
        it("UNSUCCESSFUL CHANGE, NOT PASSED first arg ", function () {
            expect(cinema.swapSeatsInHall(undefined, 2)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, NOT  PASSED second arg ", function () {
            expect(cinema.swapSeatsInHall(2, undefined)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, NOT INTEGER PASSED as first arg ", function () {
            expect(cinema.swapSeatsInHall(5.2, 2)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, NOT INTEGER PASSED as second arg ", function () {
            expect(cinema.swapSeatsInHall(2, 2.5)).to.equal('Unsuccessful change of seats in the hall.');
        });

        it("UNSUCCESSFUL CHANGE, NOT INTEGER PASSED as first arg ", function () {
            expect(cinema.swapSeatsInHall('a', 2)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, NOT INTEGER PASSED as second arg ", function () {
            expect(cinema.swapSeatsInHall(2, 'b')).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, FIRST ARG INVALID LESS THAN ZERO", function () {
            expect(cinema.swapSeatsInHall(0, 2)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, SECOND ARG INVALID LESS THAN ZERO", function () {
            expect(cinema.swapSeatsInHall(2, 0)).to.equal('Unsuccessful change of seats in the hall.');
        });

        it("UNSUCCESSFUL CHANGE, FIRST ARG INVALID Greater THAN 20", function () {
            expect(cinema.swapSeatsInHall(21, 2)).to.equal('Unsuccessful change of seats in the hall.');
        });
        it("UNSUCCESSFUL CHANGE, SECOND ARG INVALID Greater THAN 20", function () {
            expect(cinema.swapSeatsInHall(2, 21)).to.equal('Unsuccessful change of seats in the hall.');
        });

        it("UNSUCCESSFUL CHANGE, SAME SEAT NUMBER", function () {
            expect(cinema.swapSeatsInHall(2, 2)).to.equal('Unsuccessful change of seats in the hall.');
        });

        it("SUCCESSFUL CHANGE", function () {
            expect(cinema.swapSeatsInHall(2, 5)).to.equal("Successful change of seats in the hall.");
        });
        it("SUCCESSFUL CHANGE", function () {
            expect(cinema.swapSeatsInHall(1, 20)).to.equal("Successful change of seats in the hall.");
        });
    });
});