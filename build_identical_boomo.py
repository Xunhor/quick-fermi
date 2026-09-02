from bs4 import BeautifulSoup
import re

print("Building identical Boomo page from Squarespace DOM...")
with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Remove third-party trackers & cookie banners
for s in soup.find_all('script'):
    src = s.get('src', '')
    if any(k in src for k in ['datadog', 'google', 'gtm', 'analytics', 'segment', 'facebook', 'optimizely', 'trustarc', 'truste']):
        s.decompose()
    elif not src:
        text = s.string or ''
        if any(k in text for k in ['dataLayer', 'datadog', 'analytics', 'trustarc', 'truste']):
            s.decompose()

for el in soup.find_all(id=lambda x: x and ('consent' in x or 'trustarc' in x or 'truste' in x)):
    el.decompose()
for el in soup.find_all(class_=lambda x: x and ('consent' in ' '.join(x) or 'trustarc' in ' '.join(x) or 'truste' in ' '.join(x))):
    el.decompose()

# 2. Reset inline opacity: 0 and translateY
for tag in soup.find_all(style=True):
    style = tag['style']
    style = re.sub(r'opacity\s*:\s*0(\.0*)?\s*;?', 'opacity: 1;', style)
    style = re.sub(r'transform\s*:\s*translateY\([^)]+\)\s*;?', 'transform: none;', style)
    tag['style'] = style

# 3. Replace brand logo with BOOMO.
logo = soup.find(class_='global-navigation__logo')
if logo:
    logo.clear()
    logo.append(BeautifulSoup('<a href="/" style="text-decoration: none;"><span style="font-family: Clarkson, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF;">BOOMO<span style="color: #10B981;">.</span></span></a>', 'html.parser'))

# Update Header CTAs to WhatsApp
for a in soup.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True).upper()
    if 'COMECE' in text or 'CRIE' in text or 'START' in text or 'LOGIN' in text or 'ENTRAR' in text:
        a['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20um%20site%20profissional%20para%20minha%20empresa.'
        a['target'] = '_blank'
        if 'LOGIN' in text or 'ENTRAR' in text:
            a.string = 'WHATSAPP'

# 4. In conversion section, link button to WhatsApp
conversion = soup.find('section', id='conversion')
if conversion:
    btn = conversion.find('a')
    if btn:
        btn['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20colocar%20meu%20site%20no%20ar%20com%20a%20Boomo.'
        btn['target'] = '_blank'
    # Make sure video autoplays
    for v in conversion.find_all('video'):
        v['autoplay'] = 'true'
        v['loop'] = 'true'
        v['muted'] = 'true'
        v['playsinline'] = 'true'

# 5. In hero, ensure video autoplays
hero = soup.find('section', id='homepage-hero')
if hero:
    for v in hero.find_all('video'):
        v['autoplay'] = 'true'
        v['loop'] = 'true'
        v['muted'] = 'true'
        v['playsinline'] = 'true'

# 6. Inject CSS variables and layout fixes in head
head = soup.find('head')
if head:
    title = head.find('title')
    if title:
        title.string = "Boomo | Estúdio Digital de Sites por Assinatura"
    
    custom_style = soup.new_tag('style')
    custom_style.string = '''
        /* CSS VARIABLES ESSENCIAIS DO GRID DO SQUARESPACE */
        :root {
            --grid-gutter-width: 24px;
            --grid-column-width: 88px;
            --grid-margin: 60px;
            --card-width: 320px;
            --card-height: 520px;
        }

        * {
            opacity: 1 !important;
            transform: none !important;
        }

        #truste-consent-track, .truste_overlay, .truste_box_overlay, .onetrust-pc-dark-filter {
            display: none !important;
        }

        /* 1. HERO CAROUSEL: Mostrar o card Tutor / Academic Lessons no centro com Creative e Plants nos lados */
        .angled-carousel__track {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 24px !important;
            overflow: visible !important;
            width: 100% !important;
            padding: 40px 0 !important;
        }
        .angled-carousel__card {
            display: block !important;
            position: relative !important;
            width: 440px !important;
            height: 580px !important;
            border-radius: 4px !important;
            overflow: hidden !important;
            box-shadow: 0 30px 80px rgba(0,0,0,0.85) !important;
            flex-shrink: 0 !important;
        }
        .angled-carousel__card img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
        }

        /* 2. KING CAROUSEL ("AMPLIE SEUS NEGÓCIOS"): 3 Banners Panorâmicos lado a lado */
        .king-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 32px !important;
            overflow-x: auto !important;
            padding: 30px 60px !important;
            scrollbar-width: none !important;
        }
        .king-carousel__cards::-webkit-scrollbar { display: none; }
        .king-carousel__card {
            display: block !important;
            position: relative !important;
            width: 880px !important;
            height: 540px !important;
            border-radius: 12px !important;
            overflow: hidden !important;
            flex-shrink: 0 !important;
            box-shadow: 0 20px 60px rgba(0,0,0,0.12) !important;
        }
        .king-carousel__card-background-image {
            object-fit: cover !important;
            width: 100% !important;
            height: 100% !important;
            display: block !important;
        }

        /* 3. CARD CAROUSEL ("TUDO O QUE VOCÊ PRECISA EM UMA SÓ PLATAFORMA"): 4 Pôsteres */
        .card-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 20px !important;
            overflow-x: auto !important;
            padding: 30px 60px !important;
            scrollbar-width: none !important;
            max-width: 1440px !important;
            margin: 0 auto !important;
        }
        .card-carousel__cards::-webkit-scrollbar { display: none; }
        .card-carousel-card {
            display: flex !important;
            flex-direction: column !important;
            position: relative !important;
            width: 320px !important;
            height: 520px !important;
            flex-shrink: 0 !important;
            background-color: #1A1C20 !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.18) !important;
        }
        .card-carousel-card__cta {
            width: 100% !important;
            height: 100% !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            padding: 28px !important;
        }
        .card-carousel-card__asset {
            position: absolute !important;
            inset: 0 !important;
            width: 100% !important;
            height: 100% !important;
            z-index: 0 !important;
        }
        .card-carousel-card__asset img, .card-carousel-card__asset video {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
        }
        .card-carousel-card__content {
            position: relative !important;
            z-index: 2 !important;
        }

        /* 4. ROSTOS / CLIENTES ATENDIDOS */
        .customers-served__faces {
            display: flex !important;
            justify-content: center !important;
            gap: 12px !important;
            margin-top: 24px !important;
        }
        .customers-served__faces picture, .customers-served__faces img {
            width: 56px !important;
            height: 56px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            display: inline-block !important;
        }

        /* 5. VÍDEO DA ESFERA DE LUZ NO CTA */
        .conversion__centered-video, .video-base__video {
            position: absolute !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) !important;
            width: 600px !important;
            height: 600px !important;
            object-fit: contain !important;
            pointer-events: none !important;
            opacity: 0.8 !important;
        }
        .conversion {
            position: relative !important;
            overflow: hidden !important;
            background: #000000 !important;
        }
        .conversion__title, .conversion__body, .conversion__cta {
            position: relative !important;
            z-index: 2 !important;
        }

        /* 6. ACCORDION / FAQ */
        .accordion-headline__content-wrapper, .faq__accordion-body-wrapper {
            display: block !important;
        }
    '''
    head.append(custom_style)

# Add minimal vanilla JS at end of body to handle FAQ accordion clicks
script_faq = soup.new_tag('script')
script_faq.string = '''
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.accordion-headline__title').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.getAttribute('aria-controls');
                const target = document.getElementById(targetId);
                if (target) {
                    const isOpen = target.style.display !== 'none';
                    target.style.display = isOpen ? 'none' : 'block';
                    btn.setAttribute('aria-expanded', !isOpen);
                }
            });
        });
    });
'''
soup.body.append(script_faq)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("index.html written with full authentic Squarespace styles and variables!")
