#!/usr/bin/env python3
import os
from PIL import Image
directory = "images/"
folder = os.listdir("images")

for item in folder:
    # print(item)
    if item != ".DS_Store" and item != "images.zip":
        f, e = os.path.splitext(item)
        outfile = f + ".jpeg"
        im = Image.open(os.path.join(directory, item))
        im.convert("RGB")
