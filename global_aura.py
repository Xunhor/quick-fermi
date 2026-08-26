import io
import re

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific hero tracking JS with a global body tracking JS
js_old = r"""        // 7. Hero Aurora Follow Mouse
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
        }"""

js_new = r"""        // 7. Global Cursor Aura
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX;
            const y = e.clientY;
            document.documentElement.style.setProperty('--global-mouse-x', x + 'px');
            document.documentElement.style.setProperty('--global-mouse-y', y + 'px');
        });"""

html = html.replace(js_old, js_new)

# Add CSS for global aura
css_global_aura = """
  /* GLOBAL CURSOR AURA */
  html.dark-theme::before {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: radial-gradient(800px circle at var(--global-mouse-x, 50%) var(--global-mouse-y, 50%), rgba(34, 211, 238, 0.06), transparent 40%);
      pointer-events: none;
      z-index: 9997; /* Below the noise layer */
      will-change: background;
  }
"""
html = html.replace('</style>', css_global_aura + '\n</style>')

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done global aura")
