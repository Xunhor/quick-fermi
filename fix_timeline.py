import re
import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the inline style from timeline-connected-grid
html = html.replace(
    '<div class="timeline-connected-grid" style="grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px;">',
    '<div class="timeline-connected-grid">'
)
# Actually, I should just make it a clean CSS override
html = html.replace(
    '.timeline-connected-grid {\n    display: grid;\n    grid-template-columns: repeat(3, 1fr);\n    gap: 24px;\n  }',
    '.timeline-connected-grid {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));\n    gap: 24px;\n  }'
)
# Wait, I might have messed up the CSS exact match.
# Let's just use regex for the inline style
html = re.sub(
    r'<div class="timeline-connected-grid".*?>',
    '<div class="timeline-connected-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">',
    html
)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
