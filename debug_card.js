const http = require('http');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : req.url.split('?')[0]);
    if (!fs.existsSync(filePath)) {
        res.writeHead(404);
        return res.end('Not Found');
    }
    const ext = path.extname(filePath);
    const mimeMap = {
        '.html': 'text/html; charset=utf-8',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.webp': 'image/webp',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.svg': 'image/svg+xml'
    };
    res.writeHead(200, { 'Content-Type': mimeMap[ext] || 'text/plain' });
    fs.createReadStream(filePath).pipe(res);
});

server.listen(3041, async () => {
    try {
        console.log('Starting puppeteer on 3041...');
        const browser = await puppeteer.launch({
            headless: 'new',
            executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 900 });
        await page.goto('http://localhost:3041/', { waitUntil: 'load', timeout: 15000 });
        
        const info = await page.evaluate(() => {
            const card = document.querySelector('.card-carousel-card');
            const asset = card ? card.querySelector('.card-carousel-card__asset') : null;
            const img = card ? card.querySelector('img') : null;
            return {
                card: card ? { w: card.offsetWidth, h: card.offsetHeight } : null,
                asset: asset ? {
                    w: asset.offsetWidth,
                    h: asset.offsetHeight,
                    display: window.getComputedStyle(asset).display,
                    position: window.getComputedStyle(asset).position,
                    zIndex: window.getComputedStyle(asset).zIndex
                } : null,
                img: img ? {
                    w: img.offsetWidth,
                    h: img.offsetHeight,
                    src: img.currentSrc || img.src,
                    display: window.getComputedStyle(img).display,
                    visibility: window.getComputedStyle(img).visibility,
                    opacity: window.getComputedStyle(img).opacity,
                    complete: img.complete,
                    naturalWidth: img.naturalWidth
                } : null
            };
        });
        console.log('INFO:', JSON.stringify(info, null, 2));

        await browser.close();
        server.close();
    } catch(err) {
        console.error('Error:', err);
        server.close();
    }
});
