from bs4 import BeautifulSoup
import re

print("Starting build_responsive_carousel.py...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Inspect and rebuild .angled-carousel to support true 3D/angled landscape cards
hero = soup.find('section', id='homepage-hero')
if hero:
    carousel = hero.find(class_='angled-carousel')
    if carousel:
        carousel.clear()
        
        # We define the 5 authentic cards with exact 16:10 landscape images
        card_data = [
            {
                "id": "creative",
                "title": "Creative Agency",
                "img": "https://media-www.sqspcdn.com/images/auto/c7c32ead/creative-500w.jpg"
            },
            {
                "id": "plants",
                "title": "Botanica",
                "img": "https://media-www.sqspcdn.com/images/auto/9e9d7f8d/plants-500w.jpg"
            },
            {
                "id": "barber",
                "title": "Borough Barber",
                "img": "https://media-www.sqspcdn.com/images/auto/f2051f0f/barber-500w.jpg"
            },
            {
                "id": "wellness",
                "title": "Balance",
                "img": "https://media-www.sqspcdn.com/images/auto/b37c49fb/wellness-500w.jpg"
            },
            {
                "id": "tutor",
                "title": "Academic Lessons",
                "img": "https://media-www.sqspcdn.com/images/auto/f1f95a06/tutor-500w.jpg"
            }
        ]
        
        # Track container
        track = soup.new_tag('div', **{'class': 'angled-carousel__track', 'id': 'angled-track'})
        for i, d in enumerate(card_data):
            c_div = soup.new_tag('div', **{'class': f'angled-carousel__card card-index-{i}', 'data-card-id': d['id']})
            img = soup.new_tag('img', src=d['img'], alt=d['title'], loading="eager")
            c_div.append(img)
            track.append(c_div)
        
        carousel.append(track)
        
        # Controls
        ctrl_left = soup.new_tag('button', **{'class': 'angled-carousel__control angled-carousel__control--left', 'id': 'hero-prev', 'aria-label': 'Slide anterior'})
        ctrl_left.append(BeautifulSoup('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>', 'html.parser'))
        
        ctrl_right = soup.new_tag('button', **{'class': 'angled-carousel__control angled-carousel__control--right', 'id': 'hero-next', 'aria-label': 'Próximo slide'})
        ctrl_right.append(BeautifulSoup('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>', 'html.parser'))
        
        carousel.append(ctrl_left)
        carousel.append(ctrl_right)
        print("Hero carousel rebuilt with 5 authentic 16:10 cards and controls.")

# 2. Add Hamburger Button to Header on Mobile
header = soup.find('header', id='global-navigation')
if header:
    # Check if hamburger exists
    if not header.find(class_='mobile-menu-btn'):
        hamb = soup.new_tag('button', **{'class': 'mobile-menu-btn', 'id': 'mobile-menu-toggle', 'aria-label': 'Abrir menu'})
        hamb.append(BeautifulSoup('<span class="bar"></span><span class="bar"></span>', 'html.parser'))
        header.append(hamb)

# 3. Replace Master Styles with accurate responsive rules
head = soup.find('head')
if head:
    # remove old master override style tag if present
    for s in head.find_all('style'):
        if 'MASTER SQUARESPACE 1:1' in (s.string or ''):
            s.decompose()
            
    new_style = soup.new_tag('style')
    new_style.string = '''
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

        /* 1. HERO CAROUSEL CONTAINER */
        .angled-carousel {
            position: relative !important;
            width: 100vw !important;
            max-width: 100% !important;
            height: auto !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            padding: 20px 0 60px !important;
            overflow: hidden !important;
            user-select: none !important;
        }

        .angled-carousel__track {
            position: relative !important;
            width: 100% !important;
            height: 480px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }

        /* 2. ANGLED CAROUSEL CARDS - EXACT 16:10 ASPECT RATIO (500x312) */
        .angled-carousel__card {
            position: absolute !important;
            width: min(740px, 54vw) !important;
            aspect-ratio: 16 / 10 !important;
            border-radius: 6px !important;
            overflow: hidden !important;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85) !important;
            transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.5s ease, z-index 0.5s ease !important;
            cursor: pointer !important;
            background-color: #111111 !important;
        }

        .angled-carousel__card img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
            display: block !important;
            border-radius: 6px !important;
        }

        /* CARD POSITIONS (DESKTOP) */
        /* Center Card: 100% size, prominent shadow, completely straight */
        .card-pos-center {
            transform: translate3d(0, 0, 0) scale(1) !important;
            z-index: 10 !important;
            opacity: 1 !important;
            box-shadow: 0 35px 90px rgba(0, 0, 0, 0.95) !important;
        }

        /* Left Card: shifted left, tilted -3deg, scaled 0.86 */
        .card-pos-left {
            transform: translate3d(calc(-50vw + 60px), 0, 0) scale(0.86) rotate(-3deg) !important;
            z-index: 5 !important;
            opacity: 0.85 !important;
        }

        /* Right Card: shifted right, tilted +3deg, scaled 0.86 */
        .card-pos-right {
            transform: translate3d(calc(50vw - 60px), 0, 0) scale(0.86) rotate(3deg) !important;
            z-index: 5 !important;
            opacity: 0.85 !important;
        }

        /* Hidden Cards */
        .card-pos-hidden-left {
            transform: translate3d(-120vw, 0, 0) scale(0.7) rotate(-6deg) !important;
            z-index: 1 !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }

        .card-pos-hidden-right {
            transform: translate3d(120vw, 0, 0) scale(0.7) rotate(6deg) !important;
            z-index: 1 !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }

        /* Hero Controls (Left & Right Arrows) */
        .angled-carousel__control {
            position: absolute !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            width: 52px !important;
            height: 52px !important;
            border-radius: 50% !important;
            background: rgba(255, 255, 255, 0.12) !important;
            backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: #FFFFFF !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
            z-index: 20 !important;
            transition: background 0.2s, transform 0.2s !important;
        }
        .angled-carousel__control:hover {
            background: rgba(255, 255, 255, 0.25) !important;
            transform: translateY(-50%) scale(1.08) !important;
        }
        .angled-carousel__control--left {
            left: calc(50% - min(740px, 54vw) / 2 - 70px) !important;
        }
        .angled-carousel__control--right {
            right: calc(50% - min(740px, 54vw) / 2 - 70px) !important;
        }

        /* 3. MOBILE MENU BUTTON */
        .mobile-menu-btn {
            display: none;
            width: 40px;
            height: 40px;
            background: transparent;
            border: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            z-index: 100;
        }
        .mobile-menu-btn .bar {
            width: 24px;
            height: 2px;
            background-color: #FFFFFF;
            transition: transform 0.3s, opacity 0.3s;
        }

        /* 4. MOBILE ADAPTATIONS (@media max-width: 992px) */
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
            
            /* HERO CAROUSEL ON MOBILE */
            .angled-carousel__track {
                height: 240px !important;
            }
            .angled-carousel__card {
                width: min(84vw, 360px) !important;
                aspect-ratio: 16 / 10 !important;
                border-radius: 4px !important;
            }
            .card-pos-left {
                transform: translate3d(calc(-50vw - 35%), 0, 0) scale(0.82) rotate(-4deg) !important;
                opacity: 0.8 !important;
            }
            .card-pos-right {
                transform: translate3d(calc(50vw + 35%), 0, 0) scale(0.82) rotate(4deg) !important;
                opacity: 0.8 !important;
            }
            .angled-carousel__control {
                display: none !important;
            }

            /* HERO STATS ON MOBILE (2 Cols) */
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

            /* ONE PLATFORM 4 CARDS ON MOBILE */
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

            /* GET STARTED 2 CARDS ON MOBILE */
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
    head.append(new_style)

# 4. Inject Vanilla JS Carousel Controller at bottom
script_carousel = soup.new_tag('script')
script_carousel.string = '''
    document.addEventListener('DOMContentLoaded', () => {
        const cards = document.querySelectorAll('.angled-carousel__card');
        const prevBtn = document.getElementById('hero-prev');
        const nextBtn = document.getElementById('hero-next');
        const total = cards.length;
        if (total === 0) return;

        // Default active index: 2 on desktop (Barber), 1 on mobile (Botanica)
        let activeIdx = window.innerWidth > 992 ? 2 : 1;

        function updatePositions() {
            cards.forEach((card, i) => {
                card.classList.remove(
                    'card-pos-center',
                    'card-pos-left',
                    'card-pos-right',
                    'card-pos-hidden-left',
                    'card-pos-hidden-right'
                );

                // calculate relative distance in circular array
                let diff = (i - activeIdx + total) % total;
                if (diff > total / 2) diff -= total;

                if (diff === 0) {
                    card.classList.add('card-pos-center');
                } else if (diff === -1 || (diff === total - 1 && total === 2)) {
                    card.classList.add('card-pos-left');
                } else if (diff === 1) {
                    card.classList.add('card-pos-right');
                } else if (diff < 0) {
                    card.classList.add('card-pos-hidden-left');
                } else {
                    card.classList.add('card-pos-hidden-right');
                }
            });
        }

        function nextSlide() {
            activeIdx = (activeIdx + 1) % total;
            updatePositions();
        }

        function prevSlide() {
            activeIdx = (activeIdx - 1 + total) % total;
            updatePositions();
        }

        if (nextBtn) nextBtn.addEventListener('click', nextSlide);
        if (prevBtn) prevBtn.addEventListener('click', prevSlide);

        // Click on side card moves it to center
        cards.forEach((card, idx) => {
            card.addEventListener('click', () => {
                if (idx !== activeIdx) {
                    activeIdx = idx;
                    updatePositions();
                }
            });
        });

        // Touch swipe for mobile
        let touchStartX = 0;
        let touchEndX = 0;
        const track = document.getElementById('angled-track');
        if (track) {
            track.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].screenX;
            }, { passive: true });
            track.addEventListener('touchend', e => {
                touchEndX = e.changedTouches[0].screenX;
                if (touchStartX - touchEndX > 40) {
                    nextSlide(); // swipe left -> next
                } else if (touchEndX - touchStartX > 40) {
                    prevSlide(); // swipe right -> prev
                }
            }, { passive: true });
        }

        updatePositions();
    });
'''
soup.body.append(script_carousel)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("build_responsive_carousel.py completed successfully!")
