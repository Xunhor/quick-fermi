import io
import re

with io.open('css/desktop/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_global_aura = """
  /* GLOBAL CURSOR AURA */
  html.dark-theme::before {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: radial-gradient(800px circle at var(--global-mouse-x, 50vw) var(--global-mouse-y, -200px), rgba(34, 211, 238, 0.08), transparent 50%);
      pointer-events: none;
      z-index: 9997;
      will-change: background;
  }
"""

css = css + "\n" + css_global_aura

with io.open('css/desktop/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done style css")
