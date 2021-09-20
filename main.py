from PIL import Image
import os


def main():
    walk_dir = '../wp-content/uploads'

    for root, subdir, files in os.walk(walk_dir):
        ext = ('jpg', 'jpeg', 'png')
        images = [file for file in files if file.lower().endswith(ext)]

        for image in images:
            image_path = os.path.join(root, image)
            print(f"Converting {image_path}")
            converter(image_path=image_path)


def converter(image_path):
    with Image.open(image_path) as image:
        image.convert('RGBA')
        new_path = ''.join(image_path.split('.')[:-1])
        new_path = f"..{new_path}.webp"
        image.save(new_path, 'webp')


if __name__ == '__main__':
    main()
