import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
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

html = re.sub(css_old, css_new, html, flags=re.DOTALL)

# 2. Update JS
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

html = html.replace('});\\n    </script>', '});\\n' + js_to_add + '    </script>')
html = html.replace('});\n    </script>', '});\n' + js_to_add + '    </script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done Mouse Follow")
