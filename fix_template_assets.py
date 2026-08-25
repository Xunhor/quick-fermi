import os
import re

for template in ['estetica', 'advocacia', 'odontologia', 'contabilidade']:
    index_path = f"templates/{template}/index.html"
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace css paths
        content = re.sub(r'href="css/', f'href="/templates/{template}/css/', content)
        # Replace image paths
        content = re.sub(r'src="assets/images/', f'src="/templates/{template}/assets/images/', content)
        content = re.sub(r'srcset="assets/images/', f'srcset="/templates/{template}/assets/images/', content)

        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done")
