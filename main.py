from PIL import Image
import os
import sys
import zipfile


def main():
    walk_dir = sys.argv[1]
    zip_path = f"{walk_dir}.zip"
    zip = zipfile.ZipFile(zip_path, 'w')

    for root, subdir, files in os.walk(walk_dir):
        ext = ('jpg', 'jpeg', 'png')
        images = [file for file in files if file.lower().endswith(ext)]

        for image in images:
            image_path = os.path.join(root, image)
            print(f"Converting {image_path} to WebP")
            webp_path = converter(image_path=image_path)
            print(f"Image converted: {webp_path}")
            zip.write(webp_path)
            os.remove(webp_path)

    zip.close()

    print(f"Zip file generated in {zip_path}")


def converter(image_path):
    with Image.open(image_path) as image:
        image.convert('RGB')
        new_path = ''.join(image_path.split('.')[:-1])
        new_path = os.path.join(new_path + '.webp')
        image.save(new_path, 'webp')
        return new_path


if __name__ == '__main__':
    main()
