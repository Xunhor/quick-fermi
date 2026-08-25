import re
import sys

def inline_css():
    html_path = 'index.html'
    
    # Read CSS files
    try:
        with open('css/base/global.css', 'r', encoding='utf-8') as f:
            global_css = f.read()
        with open('css/desktop/style.css', 'r', encoding='utf-8') as f:
            style_css = f.read()
    except FileNotFoundError as e:
        print(f"Error reading CSS: {e}")
        return
        
    combined_css = f"<style>\n{global_css}\n{style_css}\n</style>"
    
    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Remove old links
    html = re.sub(r'<link rel="preload" as="style" href="css/base/global.css">\n?\s*', '', html)
    html = re.sub(r'<link rel="preload" as="style" href="css/desktop/style.css\?v=3">\n?\s*', '', html)
    html = re.sub(r'<link rel="stylesheet" href="css/base/global.css">\n?\s*', '', html)
    html = re.sub(r'<link rel="stylesheet" href="css/desktop/style.css\?v=3">\n?\s*', '', html)
    
    # Inject before </head>
    html = html.replace('<!-- Fonts Preload & Load -->', combined_css + '\n    <!-- Fonts Preload & Load -->')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("CSS inlined successfully!")

if __name__ == '__main__':
    inline_css()
