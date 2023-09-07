#!/usr/bin/env python3
import os
from PIL import Image

directory = "images/"
folder = os.listdir("images")
SIZE = 128, 128

for item in folder:
    if item != ".DS_Store":
        f, e = os.path.splitext(item)
        outfile = f + ".jpeg"
        im = Image.open(os.path.join(directory, item))
        im.rotate(-90).resize(SIZE).convert("RGB").save("/opt/icons/"+outfile)



