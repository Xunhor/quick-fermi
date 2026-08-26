import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero texts
html = re.sub(
    r'<h1 class="hero-headline">.*?</h1>',
    '<h1 class="hero-headline">A infraestrutura digital<br>da sua empresa.</h1>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<p class="hero-subtext">.*?</p>',
    '<p class="hero-subtext">Engenharia de ponta para empresas locais. Sites com carregamento em milissegundos, arquitetura SEO nativa e uptime de 99.9%.</p>',
    html, flags=re.DOTALL
)

# Replace comparative texts to be more professional
html = html.replace('<span class="loss-badge"><i class="fa-solid fa-xmark"></i> R$ 3.000 a R$ 8.000</span>', '<span class="loss-badge"><i class="fa-solid fa-xmark"></i> R$ 4.000 a R$ 12.000</span>')
html = html.replace('<span class="neutral-badge">R$ 0 aparente</span>', '<span class="neutral-badge">Faça Você Mesmo</span>')
html = html.replace('<span>Requer plugins e otimização manual</span>', '<span>Requer cache, minificação e CDN de terceiros</span>')
html = html.replace('<span>Código solto, dependente da hospedagem</span>', '<span>Nativo. 100/100 LCP via Edge Network</span>')
html = html.replace('Lento, depende de plugins pesados', 'Lento (LCP > 3.0s)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done index")
