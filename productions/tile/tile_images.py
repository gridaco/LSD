import click
from PIL import Image, ImageDraw
from tqdm import tqdm
import os


def get_image_files_from_directory(image_folder):
    """Fetch all PNG and JPG images from the directory."""
    return [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg'))]


def create_blank_canvas(columns, rows, resolution_x, resolution_y, background_color, border_width):
    """Create a blank canvas for the tiled image."""
    total_width = columns * resolution_x + (columns - 1) * border_width
    total_height = rows * resolution_y + (rows - 1) * border_width
    return Image.new("RGB", (total_width, total_height), background_color)


def process_image(img_path, x, y, resolution_x, resolution_y, draw, border_width, border_color):
    """Open, resize, and draw the border for each image."""
    with Image.open(img_path) as img:
        img = img.resize((resolution_x, resolution_y), Image.LANCZOS)

        # Draw the border (by drawing a larger rect behind the image)
        if border_width > 0:
            rect_x1 = x - border_width
            rect_y1 = y - border_width
            rect_x2 = x + resolution_x + border_width
            rect_y2 = y + resolution_y + border_width
            draw.rectangle([rect_x1, rect_y1, rect_x2,
                           rect_y2], fill=border_color)

        return img


def save_canvas(canvas):
    """Save the final tiled image to a file."""
    output_path = "tiled_image.jpg"
    canvas.save(output_path)
    print(f"Image saved to {output_path}")


@click.command()
@click.argument("image_folder", type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option("--columns", default=5, help="Number of columns in the tiled image.", type=int)
@click.option("--rows", default=5, help="Number of rows in the tiled image.", type=int)
@click.option("--resolution-x", default=200, help="Width of each image cell.", type=int)
@click.option("--resolution-y", default=200, help="Height of each image cell.", type=int)
@click.option("--background-color", default="white", help="Background color of the tiled image.")
@click.option("--border-width", default=2, help="Width of the border around each image cell.", type=int)
@click.option("--border-color", default="black", help="Color of the border around each image cell.")
def make_tile_image(image_folder, columns, rows, resolution_x, resolution_y, background_color, border_width, border_color):
    """Create a tiled image from a list of image files in the specified folder."""

    image_files = get_image_files_from_directory(image_folder)
    canvas = create_blank_canvas(
        columns, rows, resolution_x, resolution_y, background_color, border_width)
    draw = ImageDraw.Draw(canvas)

    for i, img_path in enumerate(tqdm(image_files, desc="Processing images", total=min(len(image_files), columns*rows))):
        if i >= columns * rows:
            break

        row = i // columns
        col = i % columns

        # Calculate position
        x = col * (resolution_x + border_width)
        y = row * (resolution_y + border_width)

        img = process_image(img_path, x, y, resolution_x,
                            resolution_y, draw, border_width, border_color)
        canvas.paste(img, (x, y))

    save_canvas(canvas)


if __name__ == "__main__":
    make_tile_image()