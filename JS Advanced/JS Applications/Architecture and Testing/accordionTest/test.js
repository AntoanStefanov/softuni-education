const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

let browser, page; // Declare reusable variables

describe('E2E tests', async function () {
    this.timeout(5000);

    before(async () => { browser = await chromium.launch(); });
    after(async () => { await browser.close(); });
    beforeEach(async () => { page = await browser.newPage(); });
    afterEach(async () => { await page.close(); });

    it('inital load', async () => {

        await page.goto('http://127.0.0.1:5502/');

        await page.waitForSelector('.accordion');

        const content = await page.textContent('#main');

        expect(content).to.contains('Scalable Vector Graphics');
        expect(content).to.contains('Open standard');
        expect(content).to.contains('Unix');
        expect(content).to.contains('ALGOL');

    });

    it('More button works', async () => {
        await page.goto('http://127.0.0.1:5502/');

        await page.waitForSelector('.accordion');

        const buttonTextContent = await page.textContent('.accordion .button');
        expect(buttonTextContent).to.equals('More');

        await page.click('text=More');

        await page.waitForResponse(/articles\/details/i); // // for throttling on

        const visible = await page.isVisible('.accordion p');

        expect(visible).to.be.true;
    });

    it('Less button works', async () => {
        await page.goto('http://127.0.0.1:5502/');

        await page.waitForSelector('.accordion');

        await page.click('text=More');

        await page.waitForResponse(/articles\/details/i);  // for throttling on

        const buttonTextContent = await page.textContent('.accordion .button');
        expect(buttonTextContent).to.equals('Less');

        await page.click('text=Less');

        const visible = await page.isVisible('.accordion p');

        expect(visible).to.be.false;

    });
});