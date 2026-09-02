from bs4 import BeautifulSoup

print("Adapting copy for Boomo in index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Hero Subtext
hero = soup.find('section', id='homepage-hero')
if hero:
    p = hero.find('p', class_='hero-cta-body')
    if p:
        p.string = "O site profissional da sua empresa no ar em 72h. Você aprova o design antes de pagar o setup."

# 2. Conversion Section (Sphere CTA)
conv = soup.find('section', id='conversion')
if conv:
    h2 = conv.find('h2')
    if h2:
        h2.string = "Coloque o seu site profissional no ar"
    p = conv.find('p')
    if p:
        p.string = "Design exclusivo, hospedagem de alta performance e suporte contínuo. Fale conosco pelo WhatsApp."
    btn = conv.find('a')
    if btn:
        btn.string = "COMECE AGORA →"
        btn['href'] = "https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20colocar%20meu%20site%20profissional%20no%20ar%20com%20a%20Boomo."
        btn['target'] = "_blank"

# 3. Footer Branding & Copyright
footer = soup.find('footer')
if footer:
    brand = footer.find(class_='footer__branding')
    if brand:
        # replace squarespace logo with Boomo
        svg = brand.find('svg')
        if svg:
            svg.decompose()
        txt = brand.find('p')
        if txt:
            txt.string = "BOOMO. Sites profissionais por assinatura para o seu negócio crescer."
    
    # Remove ICANN
    icann = footer.find(class_='footer__icann')
    if icann:
        icann.decompose()
    
    # Copyright
    cr = footer.find(class_='footer__copyright')
    if cr:
        cr.string = "© 2026 Boomo Tecnologia. Todos os direitos reservados."

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Boomo copy applied successfully!")
