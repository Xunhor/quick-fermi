import re

def inline_google_fonts():
    with open('fonts.css', 'r', encoding='utf-8') as f:
        fonts_css = f.read()
        
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Remove the Google Fonts external links
    html = re.sub(r'<link rel="preload" as="style" href="https://fonts\.googleapis\.com/css2[^>]+>\n?', '', html)
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2[^>]+>\n?', '', html)
    
    # Inject fonts CSS into the existing style block
    html = html.replace('<style>', '<style>\n/* INLINED GOOGLE FONTS */\n' + fonts_css + '\n')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == '__main__':
    inline_google_fonts()
