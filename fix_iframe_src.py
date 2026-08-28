import re
import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace data-src="/xyz" src="about:blank" with src="/xyz"
html = re.sub(r'data-src="([^"]+)" src="about:blank"', r'src="\1"', html)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
