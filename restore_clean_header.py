from bs4 import BeautifulSoup

print("Restoring clean header from sqsp_raw.html...")
with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    raw_soup = BeautifulSoup(f.read(), 'html.parser')

with open('index.html', 'r', encoding='utf-8') as f:
    index_soup = BeautifulSoup(f.read(), 'html.parser')

raw_header = raw_soup.find('header', id='global-navigation')

# 1. Clean up tracking links or logins
for a in raw_header.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True).upper()
    if 'COMECE' in text or 'CRIE' in text or 'START' in text:
        a['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20um%20site%20profissional%20para%20minha%20empresa.'
        a['target'] = '_blank'
    elif 'LOGIN' in text or 'ENTRAR' in text:
        a['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20saber%20mais%20sobre%20a%20Boomo.'
        a['target'] = '_blank'
        a.string = 'WHATSAPP'

# 2. Replace the SVG logos inside a.global-navigation__logo-link with clean BOOMO.
logo_a = raw_header.find('a', class_='global-navigation__logo-link')
if logo_a:
    logo_a.clear()
    logo_a['style'] = "text-decoration: none; display: inline-flex; align-items: center;"
    logo_span = BeautifulSoup('<span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF; display: inline-block;">BOOMO<span style="color: #10B981;">.</span></span>', 'html.parser')
    logo_a.append(logo_span)

# 3. Add mobile menu button to header
mobile_btn = BeautifulSoup('<button class="mobile-menu-btn" id="mobile-menu-toggle" aria-label="Abrir menu"><span class="bar"></span><span class="bar"></span></button>', 'html.parser')
hdr_div = raw_header.find('div', class_='global-navigation__header')
if hdr_div:
    hdr_div.append(mobile_btn)

# 4. Replace header in index.html
current_header = index_soup.find('header', id='global-navigation')
if current_header:
    current_header.replace_with(raw_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(index_soup))

print("Header restored cleanly with BOOMO. logo and hamburger button!")
