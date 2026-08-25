import os
import glob

def replace_image_extensions(directory):
    patterns = ['**/*.html', '**/*.css']
    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(directory, pattern), recursive=True))
        
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We replace .jpg and .png with .webp
        # Except og-boomo.jpg which we skipped in the previous script (wait, in the previous script I skipped 'og-boomo' but I printed "Otimizado: boomo-og.jpg", that's because the filename was boomo-og.jpg from an old version, the new one is og-boomo.jpg which WAS skipped. Let's check.)
        
        new_content = content.replace('.jpg', '.webp').replace('.jpeg', '.webp').replace('.png', '.webp')
        
        # Restore og-boomo.jpg which was explicitly skipped in previous script and MUST remain .jpg for WhatsApp compatibility
        new_content = new_content.replace('og-boomo.webp', 'og-boomo.jpg')
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Atualizado: {filepath}")

if __name__ == "__main__":
    replace_image_extensions(".")
