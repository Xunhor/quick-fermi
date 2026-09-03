from bs4 import BeautifulSoup
import re

print("Starting fix_gyb_carousel.py...")

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Update the CSS in <head> for GYB
head = soup.find('head')
if head:
    style = head.find('style')
    if style and style.string:
        # Replace the old GYB section in CSS
        pattern = r'/\* 2\. AMPLIE SEUS NEGÓCIOS.*?\*/(.*?)(?=/\* 3\.|$)'
        replacement = '''/* 2. AMPLIE SEUS NEGÓCIOS (GROW YOUR BUSINESS) */
        #grow-your-business {
            width: 100% !important;
            overflow-x: clip !important;
            padding: 80px 0 60px 0 !important;
            background: #FFFFFF !important;
        }

        .king-carousel {
            position: relative !important;
            width: 100% !important;
            overflow: hidden !important;
        }

        .king-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 24px !important;
            overflow-x: auto !important;
            scroll-snap-type: x mandatory !important;
            padding: 24px calc(50vw - min(680px, 54vw) / 2) !important;
            margin: 0 !important;
            scrollbar-width: none !important;
            -ms-overflow-style: none !important;
            scroll-behavior: smooth !important;
        }
        .king-carousel__cards::-webkit-scrollbar {
            display: none !important;
        }

        .king-carousel__card {
            position: relative !important;
            left: auto !important;
            flex-shrink: 0 !important;
            width: min(680px, 54vw) !important;
            min-width: min(680px, 54vw) !important;
            height: 440px !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            scroll-snap-align: center !important;
            cursor: pointer !important;
            transition: transform 0.3s ease, opacity 0.3s ease !important;
        }

        .pills {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 6px !important;
            list-style: none !important;
            padding: 0 !important;
            margin: 0 auto 36px auto !important;
            flex-wrap: wrap !important;
            max-width: 900px !important;
        }
        .pills__pill-container {
            display: inline-block !important;
        }
        .pills__pill {
            background: transparent !important;
            border: none !important;
            color: #000000 !important;
            font-family: Clarkson, -apple-system, sans-serif !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            padding: 8px 16px !important;
            border-radius: 999px !important;
            cursor: pointer !important;
            transition: background 0.2s, color 0.2s !important;
            text-decoration: none !important;
        }
        .pills__pill:hover {
            background: rgba(0, 0, 0, 0.04) !important;
        }
        .pills__pill.is-active,
        .pills__pill--active {
            background: rgba(0, 0, 0, 0.08) !important;
            font-weight: 700 !important;
        }

        .king-carousel__toolbar {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 16px !important;
            margin-top: 32px !important;
        }
        '''
        style.string = re.sub(pattern, replacement, style.string, flags=re.S)
        print("Updated GYB CSS in style block!")

# 2. Inject JS controller for GYB carousel at bottom of body
body = soup.find('body')
if body:
    # Remove previous controller if exists
    for s in body.find_all('script'):
        if 'initGybCarousel' in (s.string or ''):
            s.decompose()
            
    js_script = soup.new_tag('script')
    js_script.string = '''
    function initGybCarousel() {
        const section = document.getElementById('grow-your-business');
        if (!section) return;

        const container = section.querySelector('.king-carousel__cards');
        const cards = Array.from(section.querySelectorAll('.king-carousel__card'));
        const pills = Array.from(section.querySelectorAll('.pills__pill'));
        const nextBtn = section.querySelector('.king-carousel__toolbar-button, .cursor-follow__area:nth-of-type(2)');

        if (!container || cards.length === 0) return;

        // Ensure first pill is active initially
        function setActivePill(index) {
            pills.forEach((p, i) => {
                if (i === index) {
                    p.classList.add('is-active', 'pills__pill--active');
                } else {
                    p.classList.remove('is-active', 'pills__pill--active');
                }
            });
        }
        setActivePill(0);

        // Click pill to center card
        pills.forEach((pill, i) => {
            pill.addEventListener('click', (e) => {
                e.preventDefault();
                if (cards[i]) {
                    const card = cards[i];
                    const targetLeft = card.offsetLeft - (container.clientWidth / 2 - card.clientWidth / 2);
                    container.scrollTo({ left: targetLeft, behavior: 'smooth' });
                    setActivePill(i);
                }
            });
        });

        // Click on peeking card to center it
        cards.forEach((card, i) => {
            card.addEventListener('click', () => {
                const targetLeft = card.offsetLeft - (container.clientWidth / 2 - card.clientWidth / 2);
                container.scrollTo({ left: targetLeft, behavior: 'smooth' });
                setActivePill(i);
            });
        });

        // Scroll listener to update active pill
        let scrollTimeout;
        container.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                const centerPoint = container.scrollLeft + container.clientWidth / 2;
                let closestIndex = 0;
                let minDistance = Infinity;

                cards.forEach((card, i) => {
                    const cardCenter = card.offsetLeft + card.clientWidth / 2;
                    const dist = Math.abs(cardCenter - centerPoint);
                    if (dist < minDistance) {
                        minDistance = dist;
                        closestIndex = i;
                    }
                });

                setActivePill(closestIndex);
            }, 50);
        }, { passive: true });

        // Next button click
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                const centerPoint = container.scrollLeft + container.clientWidth / 2;
                let currentIndex = 0;
                let minDistance = Infinity;

                cards.forEach((card, i) => {
                    const cardCenter = card.offsetLeft + card.clientWidth / 2;
                    const dist = Math.abs(cardCenter - centerPoint);
                    if (dist < minDistance) {
                        minDistance = dist;
                        closestIndex = i;
                    }
                });

                const nextIndex = (currentIndex + 1) % cards.length;
                const nextCard = cards[nextIndex];
                const targetLeft = nextCard.offsetLeft - (container.clientWidth / 2 - nextCard.clientWidth / 2);
                container.scrollTo({ left: targetLeft, behavior: 'smooth' });
                setActivePill(nextIndex);
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGybCarousel);
    } else {
        initGybCarousel();
    }
    '''
    body.append(js_script)
    print("Injected GYB carousel controller script!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("fix_gyb_carousel.py completed successfully!")
