const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

const mockData = {
    "d953e5fb-a585-4d6b-92d3-ee90697398a0": {
        "author": "J.K.Rowling",
        "title": "Harry Potter and the Philosopher's Stone"
    },
    "d953e5fb-a585-4d6b-92d3-ee90697398a1": {
        "author": "Svetlin Nakov",
        "title": "C# Fundamentals"
    }
};

const mockBook = {
    "author": "J.K.Rowling",
    "title": "Harry Potter and the Philosopher's Stone"
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

    it('loads and displays books', async () => {
        await page.route('**/jsonstore/collections/books*', route => {
            route.fulfill(json(mockData));
        });

        await page.goto('http://localhost:5502'); // your port is 5500 , change here

        await page.click('text=LOAD ALL BOOKS');

        await page.waitForSelector('text=Harry Potter');

        const rows = await page.$$eval('tr', rows => rows.map(row => row.textContent.trim()));

        expect(rows[1]).to.contains('Harry Potter');
        expect(rows[1]).to.contains('Rowling');
        expect(rows[2]).to.contains('C# Fundamentals');
        expect(rows[2]).to.contains('Nakov');
    });

    it('can create book', async () => {
        await page.goto('http://localhost:5502'); // your port is 5500 , change here

        await page.fill('form#createForm >> input[name="title"]', 'Title');
        await page.fill('form#createForm >> input[name="author"]', 'Author');

        const [request] = await Promise.all([
            page.waitForRequest(request => request.method() == 'POST'),
            page.click('form#createForm >> text=Submit')
        ]);

        const data = JSON.parse(request.postData());

        expect(data.title).to.equal('Title');
        expect(data.author).to.equal('Author');
    });

    it('edit book', async () => {
        await page.route('**/jsonstore/collections/books', route => {
            route.fulfill(json(mockData));
        });

        await page.goto('http://localhost:5502'); // your port is 5500 , change here

        await page.click('text=LOAD ALL BOOKS');

        await page.waitForSelector('text=Harry Potter');

        await page.route('**/jsonstore/collections/books/d953e5fb-a585-4d6b-92d3-ee90697398a0', route => {
            route.fulfill(json(mockBook));
        });

        await page.click('text=Edit');

        const isEditFromVisible = await page.isVisible('form#editForm');

        expect(isEditFromVisible).to.be.true;

        let title = await page.inputValue('#editForm >> input[name="title"]');
        let author = await page.inputValue('#editForm >> input[name="author"]');

        expect(title).to.equal("Harry Potter and the Philosopher's Stone");
        expect(author).to.equal("J.K.Rowling");

        await page.fill('#editForm >> input[name="title"]', 'Title');
        await page.fill('#editForm >> input[name="author"]', 'Author');

        const [request] = await Promise.all([
            page.waitForRequest(request => request.method() == 'PUT'),
            page.click('form#editForm >> text=Save')
        ]);

        const data = JSON.parse(request.postData());

        expect(data.title).to.equal('Title');
        expect(data.author).to.equal('Author');
        // await page.waitForTimeout(60000);
    });

    it('delete book', async () => {
        await page.route('**/jsonstore/collections/books', route => {
            route.fulfill(json(mockData));
        });

        await page.goto('http://localhost:5502'); // your port is 5500 , change here

        await page.click('text=LOAD ALL BOOKS');

        await page.waitForSelector('text=Harry Potter');

        await page.route('**/jsonstore/collections/books/d953e5fb-a585-4d6b-92d3-ee90697398a0', route => {
            route.fulfill(json(mockBook));
        });

        const [request] = await Promise.all([
            page.waitForRequest(request => request.method() == 'DELETE'),
            page.click('text=Delete'),
            page.on('dialog', dialog => dialog.accept())
        ]);

        const data = JSON.parse(request.postData());
        expect(data).to.equal(null);

        // await page.waitForTimeout(60000);

    });
});