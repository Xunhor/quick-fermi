from bs4 import BeautifulSoup
import re

print("Starting finalize_identical_boomo.py...")
with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Clean up third party scripts and cookie banners
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

# Remove all inline opacity: 0 and transform styles
for tag in soup.find_all(style=True):
    style = tag['style']
    if 'opacity' in style or 'transform' in style:
        # Keep background images if any
        bg = re.search(r'background[^;]+;', style)
        bg_str = bg.group(0) if bg else ''
        tag['style'] = bg_str

# 2. Header: Logo -> BOOMO.
logo = soup.find(class_='global-navigation__logo')
if logo:
    logo.clear()
    logo.append(BeautifulSoup('<a href="/" style="text-decoration: none;"><span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF;">BOOMO<span style="color: #10B981;">.</span></span></a>', 'html.parser'))

# Header links
for a in soup.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True).upper()
    if any(k in text for k in ['COMECE', 'CRIE', 'START', 'LOGIN', 'ENTRAR']):
        a['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Gostaria%20de%20um%20site%20profissional%20para%20minha%20empresa.'
        a['target'] = '_blank'
        if 'LOGIN' in text or 'ENTRAR' in text:
            a.string = 'WHATSAPP'

# 3. Hero Carousel (Angled Carousel)
# We want 3 cards in order: Creative (left), Tutor / Academic Lessons (center), Plants (right)
hero = soup.find('section', id='homepage-hero')
if hero:
    track = hero.find(class_='angled-carousel__track')
    if track:
        cards = track.find_all(class_='angled-carousel__card')
        # Find tutor, creative, plants cards
        card_tutor = None
        card_creative = None
        card_plants = None
        for c in cards:
            html_c = str(c)
            if 'tutor' in html_c:
                card_tutor = c
            elif 'creative' in html_c:
                card_creative = c
            elif 'plants' in html_c:
                card_plants = c
        
        # Clear track and append only these 3
        if card_tutor and card_creative and card_plants:
            track.clear()
            card_creative['class'] = ['angled-carousel__card', 'hero_card_side']
            card_tutor['class'] = ['angled-carousel__card', 'hero_card_center']
            card_plants['class'] = ['angled-carousel__card', 'hero_card_side']
            track.append(card_creative)
            track.append(card_tutor)
            track.append(card_plants)
            print("Hero track re-ordered: Creative, Tutor, Plants.")

# 4. King Carousel ("Amplie seus negócios")
# We want 3 panoramic cards: services, online-store, portfolio
grow = soup.find('section', id='grow-your-business')
if grow:
    king_cards_container = grow.find(class_='king-carousel__cards')
    if king_cards_container:
        all_king_cards = king_cards_container.find_all(class_='king-carousel__card')
        chosen_cards = []
        seen_types = set()
        for kc in all_king_cards:
            html_kc = str(kc)
            for t in ['services-desktop', 'online-store-desktop', 'portfolio-desktop']:
                if t in html_kc and t not in seen_types:
                    seen_types.add(t)
                    chosen_cards.append(kc)
                    break
        if len(chosen_cards) >= 3:
            king_cards_container.clear()
            for c in chosen_cards[:3]:
                c['style'] = ''
                king_cards_container.append(c)
            print("King carousel re-ordered: 3 desktop cards.")

# 5. Card Carousel ("Tudo o que você precisa em uma só plataforma")
# We want 4 cards: website-editing, design-intelligence, business-email, domains
one_plat = soup.find('section', id='one-platform')
if one_plat:
    cards_container = one_plat.find(class_='card-carousel__cards')
    if cards_container:
        all_cards = cards_container.find_all(class_='card-carousel-card')
        chosen_plat_cards = []
        seen_keys = set()
        for c in all_cards:
            html_c = str(c)
            for key in ['website-editing', 'design-intelligence', 'business-email', 'domains']:
                if key in html_c and key not in seen_keys:
                    seen_keys.add(key)
                    chosen_plat_cards.append(c)
                    break
        if len(chosen_plat_cards) == 4:
            cards_container.clear()
            for c in chosen_plat_cards:
                c['style'] = ''
                cards_container.append(c)
            print("One platform re-ordered: 4 featured cards.")

# 6. Customers Served: ensure 5 faces are visible
cust = soup.find('section', id='customers-served')
if cust:
    faces = cust.find(class_='customers-served__faces')
    if faces:
        for tag in faces.find_all(True):
            tag['style'] = ''

# 7. Conversion: ensure video autoplays and CTA is wired
conv = soup.find('section', id='conversion')
if conv:
    for v in conv.find_all('video'):
        v['autoplay'] = 'true'
        v['loop'] = 'true'
        v['muted'] = 'true'
        v['playsinline'] = 'true'
    btn = conv.find('a')
    if btn:
        btn['href'] = 'https://wa.me/559192432044?text=Ol%C3%A1%21%20Quero%20colocar%20meu%20site%20no%20ar%20com%20a%20Boomo.'
        btn['target'] = '_blank'

# 8. Inject Master CSS Overrides in Head
head = soup.find('head')
if head:
    title = head.find('title')
    if title:
        title.string = "Boomo | Estúdio Digital de Sites por Assinatura"
    
    master_css = soup.new_tag('style')
    master_css.string = '''
        /* MASTER OVERRIDES FOR IDENTICAL RENDERING WITHOUT REACT HYDRATION */
        :root {
            --grid-gutter-width: 24px;
            --grid-column-width: 88px;
            --grid-margin: 60px;
            --card-width: 312px;
            --card-height: 480px;
        }

        * {
            opacity: 1 !important;
        }

        #truste-consent-track, .truste_overlay, .truste_box_overlay, .onetrust-pc-dark-filter {
            display: none !important;
        }

        /* 1. HERO CAROUSEL: Creative, Tutor (Center Star), Plants */
        .angled-carousel__track {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 28px !important;
            overflow: visible !important;
            width: 100% !important;
            padding: 40px 0 !important;
            transform: none !important;
        }
        .angled-carousel__card {
            display: block !important;
            position: relative !important;
            width: 440px !important;
            height: 580px !important;
            border-radius: 6px !important;
            overflow: hidden !important;
            box-shadow: 0 30px 80px rgba(0,0,0,0.9) !important;
            flex-shrink: 0 !important;
            transition: transform 0.3s ease !important;
        }
        .hero_card_center {
            transform: scale(1.08) !important;
            z-index: 3 !important;
            box-shadow: 0 40px 100px rgba(0,0,0,0.95) !important;
        }
        .hero_card_side {
            opacity: 0.82 !important;
            transform: scale(0.92) !important;
            z-index: 1 !important;
        }
        .angled-carousel__card img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
            display: block !important;
        }

        /* 2. AMPLIE SEUS NEGÓCIOS (KING CAROUSEL): 3 Banners Panorâmicos de Estúdio */
        .king-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 32px !important;
            overflow-x: auto !important;
            padding: 30px 48px !important;
            scrollbar-width: none !important;
            width: 100% !important;
        }
        .king-carousel__cards::-webkit-scrollbar { display: none; }
        .king-carousel__card {
            display: block !important;
            position: relative !important;
            left: auto !important;
            top: auto !important;
            width: 860px !important;
            height: 520px !important;
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
            position: absolute !important;
            inset: 0 !important;
        }
        .king-carousel__card-cta {
            display: block !important;
            width: 100% !important;
            height: 100% !important;
            position: relative !important;
            z-index: 2 !important;
        }

        /* 3. TUDO O QUE VOCÊ PRECISA (CARD CAROUSEL): 4 Pôsteres Ricos Lado a Lado */
        .card-carousel__cards, .card-carousel__cards--is-carousel {
            display: grid !important;
            grid-template-columns: repeat(4, 1fr) !important;
            gap: 20px !important;
            width: 100% !important;
            max-width: 1360px !important;
            margin: 0 auto !important;
            padding: 30px 0 !important;
        }
        .card-carousel-card, .card-carousel-card--is-carousel {
            display: flex !important;
            position: relative !important;
            left: auto !important;
            top: auto !important;
            transform: none !important;
            width: 100% !important;
            height: 480px !important;
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
            padding: 24px !important;
            position: relative !important;
            z-index: 2 !important;
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

        /* 4. ROSTOS / CLIENTES ATENDIDOS */
        .customers-served__faces {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin-bottom: 24px !important;
        }
        .faces__face {
            width: 56px !important;
            height: 56px !important;
            border-radius: 50% !important;
            object-fit: cover !important;
            border: 3px solid #000000 !important;
            margin-left: -14px !important;
            display: inline-block !important;
        }
        .faces__face:first-child {
            margin-left: 0 !important;
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
            padding: 160px 0 140px !important;
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
    head.append(master_css)

# Add simple vanilla JS at bottom for FAQ clicks
faq_script = soup.new_tag('script')
faq_script.string = '''
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.accordion-headline__title').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.getAttribute('aria-controls');
                const target = document.getElementById(targetId);
                if (target) {
                    const isHidden = target.style.display === 'none';
                    target.style.display = isHidden ? 'block' : 'none';
                    btn.setAttribute('aria-expanded', isHidden);
                }
            });
        });
    });
'''
soup.body.append(faq_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("SUCCESS: index.html written with full fidelity!")
