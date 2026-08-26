import io

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace CSS
old_transform = "transform: translateX(-50%);"
new_transform = "transform: translate(calc(-50% + var(--mouse-x, 0px)), var(--mouse-y, 0px));\n    will-change: transform;"

# Only replace the one inside .hero-aurora-glow
import re
html = re.sub(r'(\.hero-aurora-glow\s*{[^}]*)transform:\s*translateX\(-50%\);', r'\1' + new_transform, html)

# Inject JS before the closing script tag (the main one)
js_to_add = """
        // 7. Hero Aurora Follow Mouse
        const heroSection = document.querySelector('.hero');
        const heroAurora = document.querySelector('.hero-aurora-glow');
        if (heroSection && heroAurora) {
            heroSection.addEventListener('mousemove', (e) => {
                const rect = heroSection.getBoundingClientRect();
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const moveX = (e.clientX - rect.left - centerX) / 2;
                const moveY = (e.clientY - rect.top - centerY) / 2;
                
                heroAurora.style.setProperty('--mouse-x', moveX + 'px');
                heroAurora.style.setProperty('--mouse-y', moveY + 'px');
            });
            heroSection.addEventListener('mouseleave', () => {
                heroAurora.style.setProperty('--mouse-x', '0px');
                heroAurora.style.setProperty('--mouse-y', '0px');
            });
        }
"""

# Find the end of the script before the <script src="assets/js/menu.js"></script>
html = html.replace('        }\n    </script>\n    <script src="assets/js/menu.js"></script>', js_to_add + '        }\n    </script>\n    <script src="assets/js/menu.js"></script>')


with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done python fix")
