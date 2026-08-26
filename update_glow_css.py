import re

with open('css/desktop/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_old = r'''\.hero-aurora-glow \{
    position: absolute;
    top: -120px;
    left: 50%;
    transform: translateX\(-50%\);
    width: 1000px;
    height: 600px;'''

css_new = r'''.hero-aurora-glow {
    position: absolute;
    top: -120px;
    left: 50%;
    transform: translate(calc(-50% + var(--mouse-x, 0px)), var(--mouse-y, 0px));
    width: 1000px;
    height: 600px;
    transition: transform 0.6s cubic-bezier(0.2, 1, 0.2, 1);
    will-change: transform;'''

css = re.sub(css_old, css_new, css, flags=re.DOTALL)

with open('css/desktop/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done CSS")
