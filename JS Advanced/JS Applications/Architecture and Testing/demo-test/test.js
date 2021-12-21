const { chromium } = require('playwright-chromium');
(async () => {
    // headless == visible
    // slowMo , wait 2 sec per action
    const browser = await chromium.launch({ headless: false, slowMo: 2000 });
    const page = await browser.newPage();
    await page.goto('https://google.com/');
    await page.screenshot({ path: `example.png` });
    await browser.close();
    
})();