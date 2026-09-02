from bs4 import BeautifulSoup

print("Refining CSS in index.html for pixel-perfect desktop and mobile...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

head = soup.find('head')
if head:
    for s in head.find_all('style'):
        if 'RESPONSIVE HERO CAROUSEL' in (s.string or ''):
            s.decompose()

    css_tag = soup.new_tag('style')
    css_tag.string = '''
        /* ==========================================================================
           RESPONSIVE HERO CAROUSEL & MOBILE ADAPTATIONS (100% IDENTICAL TO REFERENCE)
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
            overflow-x: hidden;
            width: 100%;
        }

        #truste-consent-track, .truste_overlay, .truste_box_overlay, .onetrust-pc-dark-filter {
            display: none !important;
        }

        /* HIDE SKIP LINK AND MOBILE CTA FROM DESKTOP HEADER */
        .global-navigation__skip-link {
            position: absolute !important;
            left: -9999px !important;
            top: -9999px !important;
            width: 1px !important;
            height: 1px !important;
            overflow: hidden !important;
        }
        .mobile-cta {
            display: none !important;
        }

        /* HEADER DESKTOP */
        @media (min-width: 993px) {
            .global-navigation {
                display: flex !important;
                justify-content: space-between !important;
                align-items: center !important;
                padding: 18px 40px !important;
                background: transparent !important;
            }
            .mobile-menu-btn {
                display: none !important;
            }
            .global-navigation__links-container, .global-navigation__ctas-container {
                display: flex !important;
            }
        }

        /* 1. HERO CTA BUTTON (DESKTOP: FROSTED GLASS / MOBILE: PURE SOLID WHITE) */
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

        /* 2. ANGLED CAROUSEL CONTAINER */
        .angled-carousel {
            position: relative !important;
            width: 100% !important;
            max-width: 100vw !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 20px 0 30px !important;
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

        /* 3. CARDS: EXACT 500/312 (1.60) LANDSCAPE RATIO WITH ZERO CROPPING */
        .angled-carousel__card {
            position: absolute !important;
            width: min(780px, 54vw) !important;
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

        /* DESKTOP CARD POSITIONS: CENTER (BARBER), LEFT (PLANTS), RIGHT (WELLNESS) */
        .card-pos-center {
            transform: translate3d(-50%, -50%, 0) scale(1) !important;
            z-index: 10 !important;
            opacity: 1 !important;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.95) !important;
        }

        .card-pos-left {
            transform: translate3d(calc(-50% - 46vw), -50%, 0) scale(0.85) rotate(-3deg) !important;
            z-index: 5 !important;
            opacity: 0.88 !important;
        }

        .card-pos-right {
            transform: translate3d(calc(-50% + 46vw), -50%, 0) scale(0.85) rotate(3deg) !important;
            z-index: 5 !important;
            opacity: 0.88 !important;
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

        /* CAROUSEL ARROWS */
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
            left: calc(50% - min(780px, 54vw) / 2 - 70px) !important;
        }
        .angled-carousel__control--right {
            right: calc(50% - min(780px, 54vw) / 2 - 70px) !important;
        }

        /* 4. MOBILE DRAWER & NAVIGATION */
        .boomo-mobile-drawer {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(10, 10, 10, 0.96);
            backdrop-filter: blur(20px);
            z-index: 9999;
            display: none;
            flex-direction: column;
            padding: 24px;
            transition: opacity 0.3s ease;
        }
        .boomo-mobile-drawer.is-open {
            display: flex;
        }
        .boomo-mobile-drawer-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
        }
        .boomo-drawer-close {
            background: transparent;
            border: none;
            color: #FFFFFF;
            font-size: 28px;
            cursor: pointer;
        }
        .boomo-mobile-nav {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }
        .boomo-mobile-nav a {
            font-family: Clarkson, -apple-system, sans-serif;
            font-size: 24px;
            font-weight: 700;
            color: #FFFFFF;
            text-decoration: none;
            letter-spacing: -0.02em;
        }
        .boomo-mobile-drawer-footer {
            margin-top: auto;
            padding-top: 24px;
        }
        .boomo-mobile-drawer-cta {
            display: block;
            text-align: center;
            background: #FFFFFF;
            color: #000000;
            font-family: Clarkson, -apple-system, sans-serif;
            font-weight: 700;
            font-size: 16px;
            padding: 16px;
            border-radius: 6px;
            text-decoration: none;
        }

        /* 5. MOBILE SPECIFICS (@media max-width: 992px) */
        @media (max-width: 992px) {
            .mobile-menu-btn {
                display: flex !important;
            }
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

            /* HERO STATS ON MOBILE (2 Columns + 1 Center) */
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

            /* CARD CAROUSEL (4 POSTERS) ON MOBILE */
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

            /* GROW YOUR BUSINESS ON MOBILE */
            .king-carousel__cards {
                padding: 20px !important;
                gap: 16px !important;
            }
            .king-carousel__card {
                width: 88vw !important;
                height: 380px !important;
            }

            /* GET STARTED ON MOBILE */
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
    head.append(css_tag)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("CSS refined successfully!")
