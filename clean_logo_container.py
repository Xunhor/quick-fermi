import re

print("Cleaning logo container in index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire global-navigation__logo-container
logo_replacement = '''<div class="global-navigation__logo-container">
  <a href="/" class="global-navigation__logo-link" style="text-decoration: none; display: inline-flex; align-items: center; padding: 4px 0;">
    <span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF; display: inline-block;">BOOMO<span style="color: #10B981;">.</span></span>
  </a>
</div>'''

html = re.sub(r'<div class="global-navigation__logo-container">.*?</div>\s*</div>\s*</div>', logo_replacement + '\n</div></div>', html, flags=re.DOTALL, count=1)

# Also ensure any other svg with global-navigation__logo is removed
html = re.sub(r'<svg[^>]*class="[^"]*global-navigation__logo[^"]*"[^>]*>.*?</svg>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Logo container cleaned completely!")
