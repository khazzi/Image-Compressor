from PIL import Image

def compress_png(input_path, output_path):
    with Image.open(input_path) as image:
        image.save(output_path, optimize=True)

img1 = input("Enter Image path to compress:")
output_paths = input("Enter path for compressed img:")
compress_png(img1, output_paths)
