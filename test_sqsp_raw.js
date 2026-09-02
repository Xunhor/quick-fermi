const http = require('http');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const server = http.createServer((req, res) => {
    let filePath = path.join(__dirname, req.url === '/' ? 'sqsp_raw.html' : req.url.split('?')[0]);
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

server.listen(3037, async () => {
    try {
        console.log('Capturing sqsp_raw.html...');
        const browser = await puppeteer.launch({
            headless: 'new',
            executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        
        const page = await browser.newPage();
        await page.setViewport({ width: 1440, height: 900 });
        await page.goto('http://localhost:3037/', { waitUntil: 'networkidle2', timeout: 60000 });
        
        // Remove opacity: 0 and hidden styles
        await page.evaluate(() => {
            const els = document.querySelectorAll('*');
            els.forEach(el => {
                if (el.style.opacity === '0') el.style.opacity = '1';
                if (el.style.transform && el.style.transform.includes('translateY')) el.style.transform = 'none';
            });
        });
        
        await new Promise(r => setTimeout(r, 2000));
        await page.screenshot({ path: 'test_raw_full.png', fullPage: true });
        console.log('Saved test_raw_full.png');

        await browser.close();
        server.close();
        console.log('Done.');
    } catch(err) {
        console.error('Error:', err);
        server.close();
    }
});
