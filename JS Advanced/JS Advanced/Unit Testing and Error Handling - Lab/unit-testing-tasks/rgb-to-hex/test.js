let { rgbToHexColor } = require('./rgb-to-hex');
let { expect } = require('chai');

describe('RGB to Hex', function () {
    it('valid input should return #42F5D8', function () {
        expect(rgbToHexColor(66, 245, 216)).to.equal('#42F5D8');
    });
    it('valid input check edge case 0,0,0 should return #000000', function () {
        expect(rgbToHexColor(0, 0, 0)).to.equal('#000000');
    });
    it('valid input check edge case 255,255,255 should return #FFFFFF', function () {
        expect(rgbToHexColor(255, 255, 255)).to.equal('#FFFFFF');
    });
    it('invalid red arg should return undefined', function () {
        expect(rgbToHexColor(4.2, 245, 216)).to.be.undefined;
    });
    it('invalid green arg should return undefined', function () {
        expect(rgbToHexColor(123, 'a', 216)).to.be.undefined;
    });
    it('invalid blue arg should return undefined', function () {
        expect(rgbToHexColor(123, 55, { a: 1 })).to.be.undefined;
    });
    it('invalid input red arg below range should return undefined', function () {
        expect(rgbToHexColor(-11, 245, 216)).to.be.undefined;
    });
    it('invalid input green arg below range should return undefined', function () {
        expect(rgbToHexColor(123, -102, 216)).to.be.undefined;
    });
    it('invalid input blue arg below range should return undefined', function () {
        expect(rgbToHexColor(123, 55, -1)).to.be.undefined;
    });
    it('invalid input red arg above range should return undefined', function () {
        expect(rgbToHexColor(1000, 245, 216)).to.be.undefined;
    });
    it('invalid input green arg above range should return undefined', function () {
        expect(rgbToHexColor(123, 500, 216)).to.be.undefined;
    });
    it('invalid input blue arg above range should return undefined', function () {
        expect(rgbToHexColor(123, 55, 320)).to.be.undefined;
    });
});