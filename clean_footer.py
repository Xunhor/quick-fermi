from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

footer = soup.find('footer')
if footer:
    logo_svg = footer.find(class_='footer-auxiliary__sqsp-logo')
    if logo_svg:
        logo_svg.replace_with(BeautifulSoup('<span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF; display: block; margin-bottom: 8px;">BOOMO<span style="color: #10B981;">.</span></span>', 'html.parser'))

    title_p = footer.find(class_='footer-auxiliary__title')
    if title_p:
        title_p.string = "Sites profissionais por assinatura."

    # Remove icann container
    icann_p = footer.find(class_='footer-auxiliary__icann-text')
    if icann_p:
        parent = icann_p.find_parent('div')
        if parent:
            parent.decompose()

# Clean footer copyright text across entire file
c = str(soup)
c = re.sub(r'©\s*2003[–-]2026\s*Squarespace,\s*Inc\.', '© 2026 Boomo Tecnologia. Todos os direitos reservados.', c)
c = re.sub(r'\*Da revista\s*TIME[^\n<]+', '', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Footer cleaned and updated with Boomo branding!")
