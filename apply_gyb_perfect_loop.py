from bs4 import BeautifulSoup
import re

print("Starting apply_gyb_perfect_loop.py...")

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

gyb = soup.find('section', id='grow-your-business')
if not gyb:
    print("Error: #grow-your-business not found!")
    exit(1)

container = gyb.find(class_='king-carousel__cards')
if not container:
    print("Error: .king-carousel__cards not found!")
    exit(1)

# Remove any existing clones first
for c in container.find_all(class_='king-carousel__card--clone'):
    c.decompose()

# Get the 8 original cards
original_cards = container.find_all(class_='king-carousel__card')
print(f"Found {len(original_cards)} original cards.")

if len(original_cards) == 8:
    # Clone card 7 to put at the beginning so card 0 has a left neighbor
    import copy
    card7_clone = copy.copy(original_cards[7])
    card7_clone['class'] = card7_clone.get('class', []) + ['king-carousel__card--clone']
    card7_clone['data-clone-of'] = '7'
    container.insert(0, card7_clone)

    # Clone card 0 to put at the end so card 7 has a right neighbor
    card0_clone = copy.copy(original_cards[0])
    card0_clone['class'] = card0_clone.get('class', []) + ['king-carousel__card--clone']
    card0_clone['data-clone-of'] = '0'
    container.append(card0_clone)
    
    print("Added clones at start and end for seamless flanking on all slides!")

# Now update CSS in <head>
head = soup.find('head')
if head:
    style = head.find_all('style')[-1]
    if style and style.string:
        css = style.string
        
        pattern = r'/\* 2\. AMPLIE SEUS NEGÓCIOS.*?\*/(.*?)(?=/\* 3\.|$)'
        new_css = '''/* 2. AMPLIE SEUS NEGÓCIOS (GROW YOUR BUSINESS - EXACT PARITY & COMPACT) */
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
            padding: 24px 0 !important;
            margin: 0 !important;
            scrollbar-width: none !important;
            -ms-overflow-style: none !important;
            transform: none !important;
        }
        .king-carousel__cards::-webkit-scrollbar {
            display: none !important;
        }

        .king-carousel__card {
            position: relative !important;
            left: auto !important;
            flex-shrink: 0 !important;
            width: 680px !important;
            min-width: 680px !important;
            max-width: 680px !important;
            height: 440px !important;
            border-radius: 8px !important;
            overflow: hidden !important;
            scroll-snap-align: center !important;
            cursor: pointer !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.07) !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease !important;
        }
        .king-carousel__card:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 14px 36px rgba(0, 0, 0, 0.1) !important;
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

        /* Mobile & Tablet */
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
        css = re.sub(pattern, new_css, css, flags=re.S)
        style.string = css
        print("Updated CSS with perfect padding and card sizes!")

# Replace the JS controller script
body = soup.find('body')
if body:
    for s in body.find_all('script'):
        if 'initGybCarousel' in (s.string or ''):
            s.decompose()
            
    js = soup.new_tag('script')
    js.string = '''
    function initGybCarousel() {
        const section = document.getElementById('grow-your-business');
        if (!section) return;

        const container = section.querySelector('.king-carousel__cards');
        const cards = Array.from(section.querySelectorAll('.king-carousel__card'));
        const pills = Array.from(section.querySelectorAll('.pills__pill'));
        const nextBtn = section.querySelector('.king-carousel__toolbar-button, .cursor-follow__area:nth-of-type(2)');

        if (!container || cards.length === 0) return;

        // Map each pill index 0..7 to its real card in the container (index 1 is card 0 because of the clone at index 0)
        // If clones exist: index 0 is clone of 7, index 1 is card 0, ..., index 8 is card 7, index 9 is clone of 0
        const hasStartClone = cards[0].classList.contains('king-carousel__card--clone');
        const cardOffset = hasStartClone ? 1 : 0;

        function scrollToCard(cardIndex, smooth = true) {
            const targetCard = cards[cardIndex];
            if (!targetCard) return;
            const targetLeft = targetCard.offsetLeft - (container.clientWidth / 2 - targetCard.clientWidth / 2);
            container.scrollTo({
                left: targetLeft,
                behavior: smooth ? 'smooth' : 'instant'
            });
        }

        function setActivePill(realIndex) {
            pills.forEach((p, i) => {
                if (i === realIndex) {
                    p.classList.add('is-active', 'pills__pill--active');
                } else {
                    p.classList.remove('is-active', 'pills__pill--active');
                }
            });
        }

        // Center card 0 immediately on load (without smooth animation for instant crisp render)
        scrollToCard(cardOffset, false);
        setActivePill(0);

        // Click pill
        pills.forEach((pill, i) => {
            pill.addEventListener('click', (e) => {
                e.preventDefault();
                scrollToCard(i + cardOffset, true);
                setActivePill(i);
            });
        });

        // Click on peeking card
        cards.forEach((card, i) => {
            card.addEventListener('click', () => {
                scrollToCard(i, true);
            });
        });

        // Scroll listener to update active pill
        let scrollTimeout;
        container.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                const centerPoint = container.scrollLeft + container.clientWidth / 2;
                let closestIndex = cardOffset;
                let minDistance = Infinity;

                cards.forEach((card, i) => {
                    const cardCenter = card.offsetLeft + card.clientWidth / 2;
                    const dist = Math.abs(cardCenter - centerPoint);
                    if (dist < minDistance) {
                        minDistance = dist;
                        closestIndex = i;
                    }
                });

                // Convert card index to pill index
                let pillIdx = closestIndex - cardOffset;
                if (pillIdx < 0) pillIdx = 7;
                if (pillIdx > 7) pillIdx = 0;
                setActivePill(pillIdx);
            }, 60);
        }, { passive: true });

        // Next button
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                const centerPoint = container.scrollLeft + container.clientWidth / 2;
                let currentIndex = cardOffset;
                let minDistance = Infinity;

                cards.forEach((card, i) => {
                    const cardCenter = card.offsetLeft + card.clientWidth / 2;
                    const dist = Math.abs(cardCenter - centerPoint);
                    if (dist < minDistance) {
                        minDistance = dist;
                        closestIndex = i;
                    }
                });

                const nextCardIndex = (closestIndex + 1) % cards.length;
                scrollToCard(nextCardIndex, true);
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGybCarousel);
    } else {
        initGybCarousel();
    }
    '''
    body.append(js)
    print("Injected updated initGybCarousel script!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("apply_gyb_perfect_loop.py finished!")
