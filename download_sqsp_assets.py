import urllib.request
import os

css_urls = [
    ("css/sqsp-defaults.css", "https://pt.assets.squarespace.com/www/versioned-assets/styles/defaults.3400d60b.css"),
    ("css/sqsp-homepage.css", "https://pt.assets.squarespace.com/www/versioned-assets/styles/pages/homepage/default/index.4dbd58af.css")
]

for dest, url in css_urls:
    print(f"Downloading {url} to {dest}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
        f.write(resp.read())
    print(f"Downloaded {dest}: {os.path.getsize(dest)} bytes")
