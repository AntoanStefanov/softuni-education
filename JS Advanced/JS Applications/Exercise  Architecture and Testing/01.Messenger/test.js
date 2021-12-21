const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

const mockData = {
    "-LxHVtajG3N1sU714pVj":
        { "author": "Spami", "content": "Hello, are you there?" },
    "-LxIDxC-GotWtf4eHwV8":
        { "author": "Garry", "content": "Yep, whats up :?" },
    "-LxIDxPfhsNipDrOQ5g_":
        { "author": "Spami", "content": "How are you? Long time no see? :)" },
    "-LxIE-dM_msaz1O9MouM":
        { "author": "George", "content": "Hello, guys! :))" },
    "-LxLgX_nOIiuvbwmxt8w":
        { "author": "Spami", "content": "Hello, George nice to see you! :)))" }
};

function json(data) {
    return {
        status: 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };
}

describe('Tests', async function () {
    // this.timeout(60000);

    let page, browser;

    before(async () => {
        // browser = await chromium.launch({ headless: false, slowMo: 2000 });
        browser = await chromium.launch();
    });

    after(async () => {
        await browser.close();
    });

    beforeEach(async () => {
        page = await browser.newPage();
    });

    afterEach(async () => {
        await page.close();

    });

    it('loads and displays messages', async () => {
        await page.route('**/jsonstore/messenger', route => {
            route.fulfill(json(mockData));
        });

        await page.goto('http://localhost:5503'); // your port is 5500 , change here

        await page.click('[value="Refresh"]');

        await page.waitForFunction(() => document.querySelector('#messages').textLength > 0);

        const text = await page.inputValue('#messages');

        expect(text).to.contains('Hello');
        expect(text).to.contains('Spami');
        expect(text).to.contains('George');


    });

    it('sends message', async () => {
        await page.route('**/jsonstore/messenger', route => {
            route.fulfill(json(mockData));
        });

        await page.goto('http://localhost:5503'); // your port is 5500 , change here

        await page.fill('#author', 'Author');
        await page.fill('#content', 'Content');

        const [request] = await Promise.all([
            page.waitForRequest(request => request.method() == 'POST'),
            page.click('#submit')
        ]);

        const data = JSON.parse(request.postData());

        expect(data.author).to.equal('Author');
        expect(data.content).to.equal('Content');
    });
});