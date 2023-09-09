import os
import sys
from PIL import Image

# for item in os.listdir("supplier-data/images/"):
#     if ".tiff" in item:
#         f, e = os.path.splitext(item)
#         Image.open("supplier-data/images/" + item).convert("RGB").save("supplier-data/images/" + f + ".jpeg")

path = "supplier-data/images/"
pictures = os.listdir(path)
for pic in pictures:
    if ".tiff" in pic:
        file_name = os.path.splitext(pic)[0]
        outfile = "supplier-data/images/" + file_name + ".jpeg"
        try:
            Image.open(path + pic).resize((600, 400)).convert("RGB").save(outfile, "JPEG")
        except IOError:
            print("cannot convert", pic)
