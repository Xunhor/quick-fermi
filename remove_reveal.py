import re
import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove reveal and delay classes
html = re.sub(r'\s+reveal', '', html)
html = re.sub(r'\s+delay-\d+', '', html)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
