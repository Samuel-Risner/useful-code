import os
import subprocess

from PIL import Image

SUPPORTED_EXTENSIONS = [".img", ".png"]
# PATH = "convert pixel art to svg"
PATH = ""


def convert(file_name: str):
    img = Image.open(os.path.join(PATH, "images_to_convert", file_name))
    better_filename = file_name.split(".")[0]

    pixels = img.load()

    data = f'<svg xmlns="http://www.w3.org/2000/svg" width="{img.width}" height="{img.height}">\n'

    for x in range(0, img.width, 1):
        for y in range(0, img.height, 1):
            px = pixels[x, y]

            # Skip pixels with alpha value 0
            if len(px) == 4:
                if px[3] == 0:
                    continue

            data += f'<rect width="1" height="1" x="{x}" y="{y}" style="fill:rgba{px}"/>\n'

    data += "</svg>\n"

    normal_svg_file = os.path.join(PATH, "svgs", f"{file_name}.svg")
    minified_svg_file = os.path.join(PATH, "svgs", f"{file_name}.min.svg")

    with open(normal_svg_file, "w") as d:
        d.write(data)

    subprocess.run(["npx", "svgo", normal_svg_file, "-o", minified_svg_file])


def main():
    print("Getting files...\n")

    files: list[str] = os.listdir(os.path.join(PATH, "images_to_convert"))
    to_convert: list[str] = list()

    for img in files:
        for file_extension in SUPPORTED_EXTENSIONS:
            if img.endswith(file_extension):
                to_convert.append(img)
                continue

    print(
        f"Going to convert these files: {to_convert}. {len(files)} files were found and {len(to_convert)} "
        f"of them are going to be converted. Meaning that {len(files) - len(to_convert)} file(s) will not be "
        f"converted.\n"
    )

    print("Converting images...")

    for img in to_convert:
        convert(img)

    print("\nFinished converting!")


if __name__ == "__main__":
    main()
