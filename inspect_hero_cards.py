from bs4 import BeautifulSoup

with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

sec = soup.find('section', id='homepage-hero')
if sec:
    cards = sec.find_all(class_=lambda x: x and 'angled-carousel__card' in x)
    print(f'Angled carousel cards count: {len(cards)}')
    for i, c in enumerate(cards):
        imgs = [img.get('src') for img in c.find_all('img')]
        cls = ' '.join(c.get('class', []))
        print(f'Card {i}: {cls} | imgs: {imgs}')
