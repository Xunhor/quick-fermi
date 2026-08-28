import io

with io.open('index.html.backup', 'r', encoding='utf-8') as f:
    backup_lines = f.readlines()

carousel_lines = []
capturing = False
for line in backup_lines:
    if '<div class="carousel-viewport-container">' in line:
        capturing = True
    if '<!-- 4. COMO FUNCIONA' in line:
        capturing = False
        break
    if capturing:
        carousel_lines.append(line)

original_carousel_html = "".join(carousel_lines)
# Remove the last </div> and </section> if they are there, wait, the loop breaks at <!-- 4. COMO FUNCIONA.
# Let's check the last few lines of carousel_lines
print(original_carousel_html[-100:])

with io.open('index.html', 'r', encoding='utf-8') as f:
    new_lines = f.readlines()

new_html_start = []
new_html_end = []
state = 0 # 0: before, 1: inside, 2: after
for line in new_lines:
    if '<div class="carousel-viewport-container"' in line:
        state = 1
    
    if state == 0:
        new_html_start.append(line)
    elif state == 1:
        # We need to find the end of the carousel in the new html
        # It's right before <!-- 4. POSICIONAMENTO -->
        if '<!-- 4. POSICIONAMENTO -->' in line:
            # wait, <section id="modelos"> closes before <!-- 4.
            # let's just find </section> before <!-- 4.
            pass
    
    if '<!-- 4. POSICIONAMENTO -->' in line:
        state = 2
        # we need to append closing tags for section because our start stopped at viewport
        new_html_start.append("        </div>\n    </section>\n\n")
        new_html_end.append(line)
    elif state == 2:
        new_html_end.append(line)

final_html = "".join(new_html_start) + original_carousel_html + "".join(new_html_end)

with io.open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Replaced successfully!")
