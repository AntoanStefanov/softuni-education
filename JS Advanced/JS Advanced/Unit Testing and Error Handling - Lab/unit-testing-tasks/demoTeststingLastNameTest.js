// za da moje da testva funckiqta sum, trq da q importnem
let { sum } = require('./myModule');
// importirane na neshta ot chai
const { expect, } = require('chai'); // za assertite // chai e biblioteka

describe('Demo Test', () => { // packet s testove suite
    it('passing test', () => {
        'do nothing'; // tuk ne se hvurlq greshka (exception ?) suotvetno testa minava
    }); // 1 arg = ime na test // 2 arg = funkciqta koqto shte se izpylni
    it('failing test', () => {
        throw Error('Failed'); // funkciqta na edinichniq test hvurlq greshka suotvetno NE MINAVA FAIL
    });
});

describe('My Module Test', () => {
    it('works with 5 and 4', () => {
        // vmesto if-a dolu , pishem s chai importnatata funckiq expect
        // if (sum(5,4) != 9) {
        //     throw Error('Did not work as expected');
        // }
        expect(sum(5, 4)).to.equal(9); // hvurlq exception s nujnata informaciq pri greshka
    });
    it('works with 5 and 5', () => {
        // if (sum(5, 5) != 10) {
        //     throw Error('INCORRECT ANSWER')
        // };
        expect(sum(5, 5)).to.equal(10);
    });
});