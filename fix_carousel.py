import re
import io

with io.open('index.html.backup', 'r', encoding='utf-8') as f:
    backup_html = f.read()

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the carousel track wrapper from backup
# Starts at <div class="carousel-viewport-container"> and ends at the closing div before </div>\n        </div>\n    </section>
match_backup = re.search(r'(<div class="carousel-viewport-container".*?<!-- Dots Pagination Indicator -->\s*</div>)', backup_html, flags=re.DOTALL)
if match_backup:
    original_carousel = match_backup.group(1)
    
    # In my new HTML, I have:
    # <div class="carousel-viewport-container">
    #     <button class="carousel-nav-btn prev-btn" id="carousel-prev" ...
    # ...
    #     </div>
    # </div>
    match_new = re.search(r'(<div class="carousel-viewport-container.*?>.*?</button>\s*<div class="carousel-track-wrapper" id="carousel-track-wrap">.*?</div>\s*</div>\s*</div>)', html, flags=re.DOTALL)
    
    if match_new:
        html = html.replace(match_new.group(1), original_carousel)
        with io.open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Restored original carousel HTML!")
    else:
        print("Could not find the new carousel to replace.")
else:
    print("Could not find original carousel.")

