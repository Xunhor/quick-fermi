const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
  
  // Go to the live vercel site
  await page.goto('https://quick-fermi.vercel.app/', { waitUntil: 'networkidle0' });
  
  // Take screenshot
  await page.screenshot({ path: 'C:/Users/junio/Desktop/Boomo_Site_Real.png' });
  
  await browser.close();
})();
