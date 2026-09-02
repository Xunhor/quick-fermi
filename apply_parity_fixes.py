from bs4 import BeautifulSoup
import re

print("Starting apply_parity_fixes.py...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Update Hero Background Video to Barber video (matching Borough Barber template)
bg = soup.find(class_='homepage-hero__background')
if bg:
    item0 = bg.find(class_='dynamic-background__item')
    if item0:
        # Update poster image
        poster = item0.find('img', class_='dynamic-background__poster')
        if poster:
            poster['src'] = 'https://media-www.sqspcdn.com/images/pages/homepage-2025/hero/videos/july-2026/barber-desktop-poster-500w.jpg'
        
        # Update video source
        vid = item0.find('video')
        if vid:
            vid.clear()
            vid['autoplay'] = ''
            vid['loop'] = ''
            vid['muted'] = ''
            vid['playsinline'] = ''
            vid['poster'] = 'https://media-www.sqspcdn.com/images/pages/homepage-2025/hero/videos/july-2026/barber-desktop-poster-500w.jpg'
            src1 = soup.new_tag('source', src='https://media-www.sqspcdn.com/images/pages/homepage-2025/hero/videos/july-2026/barber-desktop.mp4', type='video/mp4')
            vid.append(src1)
        print("Hero background video set to barber-desktop.mp4")

# 2. Fix Grow Your Business to show unique cards with 'Ofereça serviços' first
gyb = soup.find('section', id='grow-your-business')
if gyb:
    cards_container = gyb.find(class_='king-carousel__cards')
    if cards_container:
        # Keep only the first 7 unique cards
        cards = cards_container.find_all(class_='king-carousel__card')
        for c in cards[7:]:
            c.decompose()
        # Remove any hardcoded inline transform
        cards_container['style'] = ''
        print(f"Grow your business cleaned to 7 unique cards.")

# 3. Clean One-Platform cards to ensure exactly 4 featured cards
op = soup.find('section', id='one-platform')
if op:
    cards_div = op.find(class_='card-carousel__cards')
    if cards_div:
        cards_div['style'] = ''
        for card in cards_div.find_all(class_='card-carousel-card'):
            card['style'] = ''
        toolbar = op.find(class_='card-carousel__toolbar')
        if toolbar:
            toolbar['style'] = 'display: none !important;'
        print("One-platform cleaned.")

# 4. Inject Updated Master CSS
head = soup.find('head')
if head:
    for s in head.find_all('style'):
        if 'RESPONSIVE HERO CAROUSEL' in (s.string or ''):
            s.decompose()

    new_css = soup.new_tag('style')
    new_css.string = '''
        /* ==========================================================================
           RESPONSIVE HERO CAROUSEL & VISUAL PARITY OVERRIDES
           ========================================================================== */

        :root {
            --grid-gutter-width: 24px;
            --grid-column-width: 88px;
            --grid-margin: 60px;
            --card-width: 312px;
            --card-height: 480px;
        }

        * {
            box-sizing: border-box;
            opacity: 1 !important;
        }

        body {
            background-color: #000000 !important;
            overflow-x: hidden;
            width: 100%;
            margin: 0;
            padding: 0;
        }

        #truste-consent-track, .truste_overlay, .truste_box_overlay, .onetrust-pc-dark-filter {
            display: none !important;
        }

        /* HEADER NAVIGATION */
        #global-navigation {
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            background: transparent !important;
            z-index: 1000 !important;
        }
        main#content, #homepage-hero {
            margin-top: 0 !important;
            padding-top: 0 !important;
            position: relative !important;
        }

        .global-navigation__skip-link, .mobile-cta, .global-navigation__account-children {
            display: none !important;
        }

        @media (min-width: 993px) {
            .global-navigation {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                padding: 18px 40px !important;
            }
            .global-navigation__links-container, .global-navigation__ctas-container {
                display: flex !important;
            }
        }

        /* HERO CTA BUTTON */
        @media (min-width: 993px) {
            .homepage-hero__cta {
                background: rgba(255, 255, 255, 0.22) !important;
                backdrop-filter: blur(16px) !important;
                color: #FFFFFF !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                font-family: Clarkson, -apple-system, sans-serif !important;
                font-weight: 600 !important;
                font-size: 13px !important;
                letter-spacing: 0.05em !important;
                border-radius: 4px !important;
                padding: 14px 30px !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                text-decoration: none !important;
                transition: background 0.2s, transform 0.2s !important;
            }
            .homepage-hero__cta:hover {
                background: rgba(255, 255, 255, 0.35) !important;
                transform: scale(1.02) !important;
            }
            .homepage-hero__cta * {
                color: #FFFFFF !important;
            }
        }

        @media (max-width: 992px) {
            .homepage-hero__cta {
                background-color: #FFFFFF !important;
                color: #000000 !important;
                font-family: Clarkson, -apple-system, sans-serif !important;
                font-weight: 700 !important;
                font-size: 14px !important;
                letter-spacing: 0.06em !important;
                border-radius: 4px !important;
                padding: 16px 36px !important;
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4) !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                text-decoration: none !important;
            }
            .homepage-hero__cta * {
                color: #000000 !important;
            }
        }

        /* 1. HERO CAROUSEL: EXACT POSITIONING & SPACING */
        .angled-carousel {
            position: relative !important;
            width: 100% !important;
            max-width: 100vw !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 10px 0 20px !important;
            overflow: visible !important;
            user-select: none !important;
        }

        .angled-carousel__track {
            position: relative !important;
            width: 100% !important;
            height: 520px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }

        .angled-carousel__card {
            position: absolute !important;
            width: min(800px, 56vw) !important;
            aspect-ratio: 500 / 312 !important;
            border-radius: 6px !important;
            overflow: hidden !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.9) !important;
            transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.5s ease, z-index 0.5s ease !important;
            cursor: pointer !important;
            top: 50% !important;
            left: 50% !important;
        }

        .angled-carousel__card img {
            width: 100% !important;
            height: 100% !important;
            object-fit: fill !important;
            display: block !important;
            border-radius: 6px !important;
        }

        /* DESKTOP CARD POSITIONS (CLOSER SPACING TO MATCH REFERENCE) */
        .card-pos-center {
            transform: translate3d(-50%, -50%, 0) scale(1) !important;
            z-index: 10 !important;
            opacity: 1 !important;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.95) !important;
        }

        .card-pos-left {
            transform: translate3d(calc(-50% - 37vw), -50%, 0) scale(0.86) rotate(-3deg) !important;
            z-index: 5 !important;
            opacity: 0.9 !important;
        }

        .card-pos-right {
            transform: translate3d(calc(-50% + 37vw), -50%, 0) scale(0.86) rotate(3deg) !important;
            z-index: 5 !important;
            opacity: 0.9 !important;
        }

        .card-pos-hidden-left {
            transform: translate3d(calc(-50% - 100vw), -50%, 0) scale(0.7) rotate(-6deg) !important;
            z-index: 1 !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }

        .card-pos-hidden-right {
            transform: translate3d(calc(-50% + 100vw), -50%, 0) scale(0.7) rotate(6deg) !important;
            z-index: 1 !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }

        .angled-carousel__control {
            position: absolute !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            width: 52px !important;
            height: 52px !important;
            border-radius: 50% !important;
            background: rgba(255, 255, 255, 0.15) !important;
            backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.25) !important;
            color: #FFFFFF !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
            z-index: 20 !important;
            transition: background 0.2s, transform 0.2s !important;
        }
        .angled-carousel__control:hover {
            background: rgba(255, 255, 255, 0.3) !important;
            transform: translateY(-50%) scale(1.08) !important;
        }
        .angled-carousel__control--left {
            left: calc(50% - min(800px, 56vw) / 2 - 60px) !important;
        }
        .angled-carousel__control--right {
            right: calc(50% - min(800px, 56vw) / 2 - 60px) !important;
        }

        /* 2. AMPLIE SEUS NEGÓCIOS (GROW YOUR BUSINESS) */
        .king-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 24px !important;
            overflow-x: auto !important;
            scroll-snap-type: x mandatory !important;
            padding: 20px 40px !important;
            transform: none !important;
            justify-content: flex-start !important;
        }
        .king-carousel__card {
            position: relative !important;
            min-width: min(880px, 70vw) !important;
            width: min(880px, 70vw) !important;
            height: 520px !important;
            scroll-snap-align: center !important;
            flex-shrink: 0 !important;
            border-radius: 6px !important;
            overflow: hidden !important;
        }

        /* 3. TUDO O QUE VOCÊ PRECISA EM UMA SÓ PLATAFORMA (ONE PLATFORM - 4 CARDS) */
        @media (min-width: 993px) {
            .card-carousel__cards {
                display: grid !important;
                grid-template-columns: repeat(4, 1fr) !important;
                gap: 20px !important;
                width: 100% !important;
                max-width: 1360px !important;
                margin: 0 auto !important;
                padding: 0 40px !important;
                transform: none !important;
                position: relative !important;
            }
            .card-carousel-card {
                position: relative !important;
                top: auto !important;
                left: auto !important;
                width: 100% !important;
                height: 480px !important;
                border-radius: 4px !important;
                overflow: hidden !important;
                display: flex !important;
                flex-direction: column !important;
                justify-content: flex-end !important;
            }
            .card-carousel-card__asset {
                position: absolute !important;
                top: 0 !important;
                left: 0 !important;
                width: 100% !important;
                height: 100% !important;
                z-index: 1 !important;
            }
            .card-carousel-card__asset-image,
            .card-carousel-card__background-video,
            .card-carousel-card__background-video-poster {
                width: 100% !important;
                height: 100% !important;
                object-fit: cover !important;
                display: block !important;
            }
            .card-carousel-card__content {
                position: relative !important;
                z-index: 2 !important;
                padding: 24px 20px !important;
                background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 100%) !important;
            }
            .card-carousel__toolbar {
                display: none !important;
            }
        }

        /* 4. MOBILE ADAPTATIONS (@media max-width: 992px) */
        @media (max-width: 992px) {
            .global-navigation__links-container, .global-navigation__ctas-container {
                display: none !important;
            }
            .global-navigation {
                padding: 16px 20px !important;
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
            }

            .angled-carousel {
                margin: 20px 0 20px !important;
            }
            .angled-carousel__track {
                height: 250px !important;
            }
            .angled-carousel__card {
                width: min(84vw, 360px) !important;
                aspect-ratio: 500 / 312 !important;
                border-radius: 4px !important;
            }
            .card-pos-center {
                transform: translate3d(-50%, -50%, 0) scale(1) !important;
            }
            .card-pos-left {
                transform: translate3d(calc(-50% - 68vw), -50%, 0) scale(0.82) rotate(-4deg) !important;
                opacity: 0.8 !important;
            }
            .card-pos-right {
                transform: translate3d(calc(-50% + 68vw), -50%, 0) scale(0.82) rotate(4deg) !important;
                opacity: 0.8 !important;
            }
            .angled-carousel__control {
                display: none !important;
            }

            .homepage-hero__stats-container {
                display: grid !important;
                grid-template-columns: 1fr 1fr !important;
                gap: 24px 16px !important;
                padding: 0 20px !important;
                text-align: center !important;
            }
            .homepage-hero__stat:nth-child(3) {
                grid-column: 1 / -1 !important;
                margin-top: 8px !important;
            }

            .card-carousel__cards {
                display: flex !important;
                flex-direction: row !important;
                overflow-x: auto !important;
                scroll-snap-type: x mandatory !important;
                padding: 20px !important;
                gap: 16px !important;
            }
            .card-carousel-card {
                scroll-snap-align: start !important;
                width: 280px !important;
                min-width: 280px !important;
                height: 440px !important;
            }

            .king-carousel__cards {
                padding: 20px !important;
                gap: 16px !important;
            }
            .king-carousel__card {
                width: 88vw !important;
                min-width: 88vw !important;
                height: 380px !important;
            }

            .get-started__cards {
                flex-direction: column !important;
                padding: 0 20px !important;
            }
            .ai-entrypoints__card {
                width: 100% !important;
                height: 360px !important;
                margin-bottom: 20px !important;
            }
        }
    '''
    head.append(new_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("apply_parity_fixes.py completed successfully!")
