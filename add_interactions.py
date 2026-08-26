import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add reveal to price cards
html = re.sub(r'<div class="price-card">', '<div class="price-card reveal delay-1">', html)
html = re.sub(r'<div class="price-card featured">', '<div class="price-card featured reveal delay-2">', html)
# Note: Since there are multiple price cards, delay-1, 2, 3 makes sense but delay-1 is enough for standard ones

# Add reveal to timeline steps
html = re.sub(r'<div class="timeline-step-card">', '<div class="timeline-step-card reveal">', html)

# Add reveal to FAQ items
html = re.sub(r'<div class="faq-item">', '<div class="faq-item reveal">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done interactions")
