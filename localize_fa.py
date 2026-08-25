import urllib.request
import re
import os

def setup_local_fontawesome():
    base_dir = "assets/vendor/fontawesome"
    css_dir = f"{base_dir}/css"
    webfonts_dir = f"{base_dir}/webfonts"
    
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(webfonts_dir, exist_ok=True)
    
    css_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    print("Downloading FontAwesome CSS...")
    req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        css_content = response.read().decode('utf-8')
        
    # Find all url(../webfonts/...) links
    urls = re.findall(r'url\(([^)]+)\)', css_content)
    webfont_files = set()
    for url in urls:
        url = url.strip("'\"")
        if 'webfonts/' in url:
            filename = url.split('/')[-1].split('?')[0].split('#')[0]
            webfont_files.add(filename)
            
    print(f"Found {len(webfont_files)} webfonts to download.")
    
    for filename in webfont_files:
        font_url = f"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/{filename}"
        font_path = f"{webfonts_dir}/{filename}"
        if not os.path.exists(font_path):
            print(f"Downloading {filename}...")
            try:
                font_req = urllib.request.Request(font_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(font_req) as response:
                    with open(font_path, 'wb') as f:
                        f.write(response.read())
            except Exception as e:
                print(f"Failed to download {filename}: {e}")
                
    # Modify CSS: Add font-display: swap; to @font-face blocks
    print("Patching CSS with font-display: swap...")
    # Find all @font-face blocks and insert font-display: swap; before the closing brace
    patched_css = re.sub(r'(@font-face\s*\{[^}]+)(?=\})', r'\1;font-display:swap;', css_content)
    
    with open(f"{css_dir}/all.min.css", 'w', encoding='utf-8') as f:
        f.write(patched_css)
        
    print("FontAwesome localized successfully.")

if __name__ == '__main__':
    setup_local_fontawesome()
