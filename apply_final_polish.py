from bs4 import BeautifulSoup
import re

print("Starting apply_final_polish.py...")
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Clean both logo links in header
header = soup.find('header', id='global-navigation')
if header:
    for a in header.find_all('a', class_=lambda x: x and 'global-navigation__logo-link' in ' '.join(x)):
        a.clear()
        a['style'] = "text-decoration: none; display: inline-flex; align-items: center;"
        boomo_html = '<span style="font-family: Clarkson, -apple-system, sans-serif; font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: #FFFFFF; display: inline-block;">BOOMO<span style="color: #10B981;">.</span></span>'
        a.append(BeautifulSoup(boomo_html, 'html.parser'))
    
    # Also clean any stray svg logo
    for s in header.find_all('svg', class_=lambda x: x and 'global-navigation__logo' in ' '.join(x)):
        s.decompose()
    print("Header logos completely cleaned.")

# 2. Hero CTA Button: Pure Solid White #FFFFFF, black bold text #000000
hero = soup.find('section', id='homepage-hero')
if hero:
    for a in hero.find_all('a'):
        if 'homepage-hero__cta' in ' '.join(a.get('class', [])):
            a['class'] = ['cta', 'cta--primary', 'cta--light', 'homepage-hero__cta']
            a['style'] = 'background-color: #FFFFFF !important; color: #000000 !important; font-family: Clarkson, -apple-system, sans-serif !important; font-weight: 700 !important; border-radius: 4px !important; padding: 16px 36px !important; font-size: 14px !important; letter-spacing: 0.06em !important; text-transform: uppercase !important; box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important; display: inline-flex !important; align-items: center !important; justify-content: center !important;'
            a.clear()
            a.append(BeautifulSoup('<span style="color: #000000 !important; font-weight: 700 !important;">COMECE JÁ</span>', 'html.parser'))
    print("Hero CTA button updated to solid white with bold black text.")

# 3. Save index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("apply_final_polish.py executed successfully!")
