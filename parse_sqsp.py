from bs4 import BeautifulSoup

with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')
print('Main found:', bool(main))

sections = main.find_all('section')
print(f'Total sections inside main: {len(sections)}')
for i, s in enumerate(sections):
    sec_id = s.get('id', '')
    sec_cls = ' '.join(s.get('class', []))
    title = s.find(['h1', 'h2', 'h3'])
    title_text = title.get_text(strip=True) if title else ''
    print(f"[{i}] id='{sec_id}' class='{sec_cls}' title='{title_text}'")
