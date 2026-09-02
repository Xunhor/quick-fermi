from bs4 import BeautifulSoup
import re

print("Perfecting carousel and mobile responsive layout...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Clean the header logo so it's strictly BOOMO. without stray SVGs
header = soup.find('header', id='global-navigation')
if header:
    logo_link = header.find(class_='global-navigation__logo')
    if logo_link:
        logo_link.clear()
        logo_link.append(BeautifulSoup('<a href="/" style="text-decoration: none;"><span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF;">BOOMO<span style="color: #10B981;">.</span></span></a>', 'html.parser'))

# 2. Hero CTA Button: White background with black text (exact Squarespace look)
hero = soup.find('section', id='homepage-hero')
if hero:
    btn = hero.find('a', class_='homepage-hero__cta')
    if btn:
        btn['style'] = 'background: #FFFFFF !important; color: #000000 !important; font-weight: 700 !important; border-radius: 4px !important; padding: 14px 28px !important; text-transform: uppercase !important; font-size: 13px !important; letter-spacing: 0.05em !important; box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;'

# 3. Update CSS overrides for perfect proportions on desktop and mobile
head = soup.find('head')
if head:
    for s in head.find_all('style'):
        if 'RESPONSIVE HERO CAROUSEL' in (s.string or ''):
            s.decompose()

    new_css = soup.new_tag('style')
    new_css.string = '''
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

        /* 1. HERO CTA BUTTON (WHITE BACKGROUND LIKE ORIGINAL) */
        .homepage-hero__cta, .homepage-hero__cta-wrapper a, .hero-cta-button {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            font-family: Clarkson, -apple-system, sans-serif !important;
            font-weight: 700 !important;
            border-radius: 4px !important;
            padding: 14px 32px !important;
            font-size: 13px !important;
            letter-spacing: 0.06em !important;
            text-transform: uppercase !important;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            text-decoration: none !important;
            transition: transform 0.2s, background 0.2s !important;
        }
        .homepage-hero__cta:hover {
            background-color: #F0F0F0 !important;
            transform: scale(1.02) !important;
        }

        /* 2. ANGLED CAROUSEL CONTAINER */
        .angled-carousel {
            position: relative !important;
            width: 100% !important;
            max-width: 100vw !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 20px 0 40px !important;
            overflow: visible !important;
            user-select: none !important;
        }

        .angled-carousel__track {
            position: relative !important;
            width: 100% !important;
            height: 500px !important;
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

        /* 4. MOBILE SPECIFICS (@media max-width: 992px) */
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
                margin: 20px 0 30px !important;
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

            /* KING CAROUSEL ON MOBILE */
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
    head.append(new_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Perfected carousel and mobile CSS written!")
