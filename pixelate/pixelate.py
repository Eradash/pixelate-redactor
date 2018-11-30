from PIL import Image


def pixelate(input_file_path, output_file_path, pixel_size, start_x, start_y, size_x, size_y):
    original = Image.open(input_file_path)
    pixelated = original.resize(
        (original.size[0] // pixel_size, original.size[1] // pixel_size),
        Image.NEAREST
    )
    pixelated = pixelated.resize(
        (pixelated.size[0] * pixel_size, pixelated.size[1] * pixel_size),
        Image.NEAREST
    )
    box = (start_x, start_y, start_x + size_x, start_y + size_y)
    original.paste(pixelated.crop(box), box)
    original.save(output_file_path)
