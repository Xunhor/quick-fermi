import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Models Section Header
html = re.sub(
    r'<h2>Veja como o seu novo site vai ficar.</h2>',
    '<h2>Sites demonstrativos</h2>',
    html
)

html = re.sub(
    r'<p>Navegue pelos modelos reais desenvolvidos.*?sua marca.</p>',
    '<p>Veja alguns exemplos do que podemos criar para o seu negócio.</p>',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
