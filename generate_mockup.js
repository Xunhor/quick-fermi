const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
  
  // Go to local file
  await page.goto('file:///' + __dirname.replace(/\\/g, '/') + '/ig_mockup.html', { waitUntil: 'networkidle0' });
  
  // Take screenshot
  await page.screenshot({ path: 'C:/Users/junio/Desktop/Boomo_Mockup_3D_Instagram.png' });
  
  await browser.close();
})();
