from bs4 import BeautifulSoup

print("Fixing GYB card inline styles and CSS...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Clear inline style on every GYB card
gyb = soup.find('section', id='grow-your-business')
if gyb:
    for c in gyb.find_all(class_='king-carousel__card'):
        if c.has_attr('style'):
            del c['style']

# 2. Update CSS rule for GYB carousel in head
head = soup.find('head')
if head:
    style = head.find('style')
    if style and style.string:
        old_gyb_css = '''.king-carousel__cards {
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
        }'''
        
        new_gyb_css = '''.king-carousel__cards {
            display: flex !important;
            flex-direction: row !important;
            gap: 24px !important;
            overflow-x: auto !important;
            scroll-snap-type: x mandatory !important;
            padding: 20px calc(50vw - min(880px, 70vw) / 2) !important;
            transform: none !important;
            justify-content: flex-start !important;
        }
        .king-carousel__card {
            position: relative !important;
            left: 0 !important;
            min-width: min(880px, 70vw) !important;
            width: min(880px, 70vw) !important;
            height: 520px !important;
            scroll-snap-align: center !important;
            flex-shrink: 0 !important;
            border-radius: 6px !important;
            overflow: hidden !important;
        }'''
        style.string = style.string.replace(old_gyb_css, new_gyb_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("GYB cards fixed and centered on Ofereça serviços!")
