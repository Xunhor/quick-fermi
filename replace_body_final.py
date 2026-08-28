import io
import re

with io.open('body_p1.txt', 'r', encoding='utf-8') as f:
    p1 = f.read()
with io.open('body_p2.txt', 'r', encoding='utf-8') as f:
    p2 = f.read()
with io.open('body_p3.txt', 'r', encoding='utf-8') as f:
    p3 = f.read()
with io.open('body_p4.txt', 'r', encoding='utf-8') as f:
    p4 = f.read()

new_body = p1 + p2 + p3 + p4

with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<body.*?>.*?</body>', new_body, html, flags=re.DOTALL)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Body completely replaced!")
