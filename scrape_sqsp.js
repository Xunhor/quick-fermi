const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    try {
        console.log('Launching browser...');
        const browser = await puppeteer.launch({
            headless: 'new',
            executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 900 });
        console.log('Navigating to https://pt.squarespace.com/ ...');
        await page.goto('https://pt.squarespace.com/', { waitUntil: 'networkidle2', timeout: 60000 });
        
        // Save full rendered HTML
        const html = await page.content();
        fs.writeFileSync('sqsp_raw.html', html, 'utf-8');
        console.log('Saved sqsp_raw.html (' + html.length + ' bytes)');
        
        // Extract CSS links
        const styles = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(l => l.href);
        });
        console.log('CSS Links found:', styles.length);
        fs.writeFileSync('sqsp_css_links.json', JSON.stringify(styles, null, 2), 'utf-8');

        // Extract media
        const media = await page.evaluate(() => {
            const imgs = Array.from(document.querySelectorAll('main img, header img, footer img')).map(i => ({
                src: i.src,
                currentSrc: i.currentSrc,
                srcset: i.srcset,
                alt: i.alt,
                className: i.className
            }));
            const videos = Array.from(document.querySelectorAll('video, source')).map(v => v.src);
            return { imgs, videos };
        });
        fs.writeFileSync('sqsp_media.json', JSON.stringify(media, null, 2), 'utf-8');
        console.log('Media extracted. Images count:', media.imgs.length, 'Videos:', media.videos.length);

        await browser.close();
        console.log('Scrape complete.');
    } catch (err) {
        console.error('Error:', err);
    }
})();
