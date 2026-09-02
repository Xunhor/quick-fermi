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

server.listen(3045, async () => {
    try {
        console.log('Capturing responsive views on 3045...');
        const browser = await puppeteer.launch({
            headless: 'new',
            executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        
        // 1. DESKTOP (1440x900)
        const pageDesktop = await browser.newPage();
        await pageDesktop.setViewport({ width: 1440, height: 900 });
        await pageDesktop.goto('http://localhost:3045/', { waitUntil: 'networkidle2', timeout: 20000 });
        await new Promise(r => setTimeout(r, 1500));
        await pageDesktop.screenshot({ path: 'desktop_hero_1440.png', clip: { x: 0, y: 0, width: 1440, height: 950 } });
        console.log('Saved desktop_hero_1440.png');

        // 2. MOBILE (390x844 iPhone 14/15)
        const pageMobile = await browser.newPage();
        await pageMobile.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });
        await pageMobile.goto('http://localhost:3045/', { waitUntil: 'networkidle2', timeout: 20000 });
        await new Promise(r => setTimeout(r, 1500));
        await pageMobile.screenshot({ path: 'mobile_hero_390.png', clip: { x: 0, y: 0, width: 390, height: 844 } });
        console.log('Saved mobile_hero_390.png');

        await browser.close();
        server.close();
    } catch(err) {
        console.error('Error:', err);
        server.close();
    }
});
