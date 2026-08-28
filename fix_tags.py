import io
with io.open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_string = "        </div>\n    </section>\n\n        <div class=\"carousel-viewport-container\">"
good_string = "        <div class=\"carousel-viewport-container\">"
html = html.replace(bad_string, good_string)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
