from bs4 import BeautifulSoup
import re

print("Starting apply_gyb_compact_center.py...")

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

head = soup.find('head')
if head:
    style = head.find_all('style')[-1]
    if style and style.string:
        css = style.string
        
        # Define clean new rules for GYB
        old_pattern = r'/\* 2\. AMPLIE SEUS NEGÓCIOS.*?\*/(.*?)(?=/\* 3\.|$)'
        new_rules = '''/* 2. AMPLIE SEUS NEGÓCIOS (GROW YOUR BUSINESS - COMPACT & CENTERED) */
        #grow-your-business {
            width: 100% !important;
            max-width: 100vw !important;
            overflow-x: clip !important;
            padding: 80px 0 60px 0 !important;
            background: #FFFFFF !important;
            position: relative !important;
        }

        .king-carousel {
            position: relative !important;
            width: 100vw !important;
            max-width: 100vw !important;
            left: 50% !important;
            right: 50% !important;
            margin-left: -50vw !important;
            margin-right: -50vw !important;
            overflow: hidden !important;
        }

        .king-carousel__cards {
            width: 100vw !important;
            max-width: 100vw !important;
            display: flex !important;
            flex-direction: row !important;
            gap: 24px !important;
            overflow-x: auto !important;
            scroll-snap-type: x mandatory !important;
            box-sizing: border-box !important;
            padding: 24px calc(50vw - 320px) !important;
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
            width: 640px !important;
            min-width: 640px !important;
            max-width: 640px !important;
            height: 420px !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            scroll-snap-align: center !important;
            cursor: pointer !important;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08) !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        }
        .king-carousel__card:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12) !important;
        }

        /* Pills Styling */
        .pills {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            gap: 6px !important;
            list-style: none !important;
            padding: 0 20px !important;
            margin: 0 auto 36px auto !important;
            flex-wrap: wrap !important;
            max-width: 960px !important;
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
            padding: 8px 18px !important;
            border-radius: 999px !important;
            cursor: pointer !important;
            transition: background 0.2s, color 0.2s !important;
            text-decoration: none !important;
        }
        .pills__pill:hover {
            background: rgba(0, 0, 0, 0.05) !important;
        }
        .pills__pill.is-active,
        .pills__pill--active {
            background: rgba(0, 0, 0, 0.08) !important;
            font-weight: 700 !important;
        }

        /* Mobile */
        @media (max-width: 768px) {
            .king-carousel__cards {
                padding: 20px 24px !important;
                gap: 16px !important;
            }
            .king-carousel__card {
                width: calc(100vw - 48px) !important;
                min-width: calc(100vw - 48px) !important;
                max-width: calc(100vw - 48px) !important;
                height: 380px !important;
            }
            .pills {
                overflow-x: auto !important;
                justify-content: flex-start !important;
                flex-wrap: nowrap !important;
                scrollbar-width: none !important;
            }
            .pills::-webkit-scrollbar {
                display: none !important;
            }
        }
        '''
        
        css = re.sub(old_pattern, new_rules, css, flags=re.S)
        style.string = css
        print("Updated Style 4 successfully!")

# Ensure the JS controller is present and works
body = soup.find('body')
if body:
    # Remove any old initGybCarousel
    for s in body.find_all('script'):
        if 'initGybCarousel' in (s.string or ''):
            s.decompose()

    script_tag = soup.new_tag('script')
    script_tag.string = '''
    function initGybCarousel() {
        const section = document.getElementById('grow-your-business');
        if (!section) return;

        const container = section.querySelector('.king-carousel__cards');
        const cards = Array.from(section.querySelectorAll('.king-carousel__card'));
        const pills = Array.from(section.querySelectorAll('.pills__pill'));
        const nextBtn = section.querySelector('.king-carousel__toolbar-button, .cursor-follow__area:nth-of-type(2)');

        if (!container || cards.length === 0) return;

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

        // Click pill
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

        // Scroll listener with debounce to update active pill
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
            }, 60);
        }, { passive: true });

        // Next button
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
    body.append(script_tag)
    print("Injected updated initGybCarousel script!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("apply_gyb_compact_center.py completed!")
