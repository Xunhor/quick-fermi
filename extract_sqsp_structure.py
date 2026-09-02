from bs4 import BeautifulSoup

with open('sqsp_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')

sections = [
    'homepage-hero',
    'grow-your-business',
    'one-platform',
    'get-started',
    'your-domain',
    'customers-served',
    'homepage-faq',
    'conversion'
]

for sid in sections:
    sec = main.find('section', id=sid) or main.find('div', id=sid) or soup.find(id=sid)
    if sec:
        print(f"=== SECTION: {sid} ===")
        print(f"Classes: {sec.get('class')}")
        # Print first 300 chars of HTML
        snippet = str(sec)[:400].replace('\n', ' ')
        print(f"Snippet: {snippet}...\n")
    else:
        print(f"=== SECTION NOT FOUND: {sid} ===\n")
