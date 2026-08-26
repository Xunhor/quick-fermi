import io
import re

with io.open('css/desktop/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_transform = "transform: translateX(-50%);"
new_transform = "transform: translate(calc(-50% + var(--mouse-x, 0px)), var(--mouse-y, 0px));\n    will-change: transform;"
css = re.sub(r'(\.hero-aurora-glow\s*{[^}]*)transform:\s*translateX\(-50%\);', r'\1' + new_transform, css)

with io.open('css/desktop/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
