from PIL import Image
import glob

def resize_images():
    for filepath in glob.glob('templates/*/assets/images/hero-*.webp'):
        img = Image.open(filepath)
        if img.size == (1024, 1024):
            img = img.resize((512, 512), Image.Resampling.LANCZOS)
            img.save(filepath, "WEBP", quality=85)
            print(f"Resized {filepath} to 512x512")

if __name__ == '__main__':
    resize_images()
