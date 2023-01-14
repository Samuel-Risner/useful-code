import os

from PIL import Image

SUPPORTED_EXTENSIONS = [".img", ".png"]
PATH = "convert pixel art to svg/"

def convert(file_name: str):
    img = Image.open(f"{PATH}images_to_convert/{file_name}")
    better_filename = file_name.split(".")[0]

    pixels = img.load()

    data = f'<svg xmlns="http://www.w3.org/2000/svg" width="{img.width}" height="{img.height}">\n'

    for x in range(0, img.width, 1):
        for y in range(0, img.height, 1):
            px = pixels[x, y]
            
            if len(px) == 4:
                if px[3] == 0:
                    continue

            data += f'<rect width="1" height="1" x="{x}" y="{y}" style="fill:rgba{px}"/>\n'
    
    data += "</svg>\n"
    
    with open(f"{PATH}svgs/{better_filename}.svg", "w") as d:
        d.write(data)
    
    os.system(f"svgo '{PATH}svgs/{better_filename}.svg' -o '{PATH}svgs/{better_filename}.min.svg'")

print("Getting files...")
files: list[str] = os.listdir(f"{PATH}images_to_convert")
to_convert: list[str] = list()
for img in files:
    for file_extension in SUPPORTED_EXTENSIONS:
        if img.endswith(file_extension):
            to_convert.append(img)
            continue
print(f"Going to convert these files: {to_convert}. {len(files)} amount of files were found and {len(to_convert)} of \
them are going to be converted. Meaning that {len(files) - len(to_convert)} files will not be converted.")

print("Converting images...")
for img in to_convert:
    convert(img)

print("Finished converting!")