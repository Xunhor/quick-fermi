import os
import re

files_to_check = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'assets' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            files_to_check.append(os.path.join(root, file))

for filepath in files_to_check:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace exact matches
    content = re.sub(r'href="index\.html(#.*?|)"', r'href="/\1"', content)
    content = re.sub(r'href="sobre\.html(#.*?|)"', r'href="/sobre\1"', content)
    content = re.sub(r'href="sucesso\.html(#.*?|)"', r'href="/sucesso\1"', content)
    content = re.sub(r'href="termos-privacidade\.html(#.*?|)"', r'href="/termos-privacidade\1"', content)
    content = re.sub(r'href="onboarding\.html(#.*?|)"', r'href="/onboarding\1"', content)
    
    # Also action attributes in forms if any
    content = re.sub(r'action="sucesso\.html(#.*?|)"', r'action="/sucesso\1"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
