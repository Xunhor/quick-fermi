import os
from PIL import Image
import glob

def optimize_images(directory):
    total_saved = 0
    
    # Find all jpg and png files
    patterns = ['**/*.jpg', '**/*.jpeg', '**/*.png']
    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(directory, pattern), recursive=True))
        
    print(f"Encontradas {len(files)} imagens para otimizar.")
    
    for filepath in files:
        if 'og-boomo' in filepath:
            continue # Skip OG image as some platforms prefer jpg
            
        try:
            with Image.open(filepath) as img:
                original_size = os.path.getsize(filepath)
                
                # Convert to RGB if PNG with alpha for WEBP saving (WebP supports alpha but just to be safe if we want JPEG fallback, but we use WEBP)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                    
                # Resize if too large (max 1400px width)
                max_width = 1400
                if img.width > max_width:
                    ratio = max_width / img.width
                    new_size = (max_width, int(img.height * ratio))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Save as webp
                new_filepath = os.path.splitext(filepath)[0] + '.webp'
                img.save(new_filepath, 'WEBP', quality=75, method=6)
                
                new_size = os.path.getsize(new_filepath)
                total_saved += (original_size - new_size)
                
                print(f"Otimizado: {os.path.basename(filepath)} -> .webp (Redução: {(original_size-new_size)/1024:.1f}KB)")
                
                # Remove original file to force us to use the new one
                os.remove(filepath)
                
        except Exception as e:
            print(f"Erro ao processar {filepath}: {e}")
            
    print(f"Otimização concluída! Espaço economizado: {total_saved/1024/1024:.2f}MB")

if __name__ == "__main__":
    optimize_images(".")
