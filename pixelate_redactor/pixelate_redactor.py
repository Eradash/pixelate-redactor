from PIL import Image
import json


def pixelate_redactor(input_file_path, output_file_path, pixel_size, start_x, start_y, size_x, size_y):
    box = (start_x, start_y, start_x + size_x, start_y + size_y)
    original, pixelated = pixelate(input_file_path, pixel_size)
    original = pixelate_box(original, pixelated, box)
    original.save(output_file_path)


def pixelate_boxes_path(input_file_path, output_file_path, pixel_size, boxes_file_path):
    pixelate_boxes(input_file_path, output_file_path, pixel_size, generate_boxes(boxes_file_path))


def pixelate_boxes(input_file_path, output_file_path, pixel_size, boxes):
    original, pixelated = pixelate(input_file_path, pixel_size)

    for box_key in boxes.keys():
        pixelate_box(original, pixelated, generate_tuples(boxes[box_key]))

    original.save(output_file_path)


def generate_tuples(box):
    px = box["px"]
    py = box["py"]
    sx = box["sx"]
    sy = box["sy"]

    box = (px, py, px + sx, py + sy)
    return box


def pixelate_box(original, pixelated, box):
    original.paste(pixelated.crop(box), box)
    return original


def pixelate(input_file_path, pixel_size):
    original = Image.open(input_file_path)
    pixelated = original.resize(
        (original.size[0] // pixel_size, original.size[1] // pixel_size),
        Image.NEAREST
    )
    pixelated = pixelated.resize(
        (pixelated.size[0] * pixel_size, pixelated.size[1] * pixel_size),
        Image.NEAREST
    )
    return original, pixelated


def generate_boxes(box_file_path):
    with open(box_file_path) as f:
        return json.load(f)


if __name__ == '__main__':
    pixelate_boxes_path("../img/example_img_original.png", "../img/example_img_redacted.png", 20, "../img/boxes.json")
