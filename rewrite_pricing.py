import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<p class="price-desc">Ideal para profissionais aut.*?</p>',
    '<p class="price-desc">Para quem precisa colocar seu negócio no ar.</p>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p class="price-desc">Perfeito para cl.*?</p>',
    '<p class="price-desc">Para empresas que querem uma presença digital mais completa.</p>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p class="price-desc">Para empresas com m.*?</p>',
    '<p class="price-desc">Para negócios que precisam de mais personalização e recursos.</p>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<h3>Pro Negcios Locais</h3>',
    '<h3>Profissional</h3>',
    html
)
html = re.sub(
    r'<h3>Pro Negócios Locais</h3>',
    '<h3>Profissional</h3>',
    html
)

html = re.sub(
    r'<li><i class="fa-solid fa-check"></i> Altera.*?</p>',
    '<li><i class="fa-solid fa-check"></i> Alterações ilimitadas dentro do escopo</li>',
    html, flags=re.DOTALL
)

# Update CTAs for Pricing
html = re.sub(
    r'<a href="https://wa.me/559192432044.*?" class="btn btn-secondary btn-full">Assinar Essencial</a>',
    '<a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Essencial%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Começar Essencial</a>',
    html
)
html = re.sub(
    r'<a href="https://wa.me/559192432044.*?" class="btn btn-primary btn-full">Assinar Pro</a>',
    '<a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Profissional%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-full">Começar Profissional</a>',
    html
)
html = re.sub(
    r'<a href="https://wa.me/559192432044.*?" class="btn btn-secondary btn-full">Solicitar Or.*</a>',
    '<a href="https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20conhecer%20o%20plano%20Premium%20da%20Boomo." target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-full">Falar com Consultor</a>',
    html
)

# Remove the COMPARISON TABLE completely as it violates simplicity
html = re.sub(
    r'<div class="compare-table-wrapper.*?(?=<!-- 7\. FAQ -->)',
    '',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
