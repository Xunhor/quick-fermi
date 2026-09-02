from bs4 import BeautifulSoup

print("Stripping external JS bundles from index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Remove all external script tags
for s in soup.find_all('script'):
    src = s.get('src', '')
    if src:
        s.decompose()
    else:
        # If it's not our FAQ script, check if it's webpack/react code
        text = s.string or ''
        if 'webpack' in text or 'window.__' in text or 'Squarespace' in text or 'JSON.parse' in text:
            s.decompose()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("All external React bundles removed. Only pure HTML & CSS remaining.")
