#!/usr/bin/env python3
import os
import requests

url = "http://localhost//upload"
path = "/supplier-data/images/"

pictures = os.listdir(path)

for pic in pictures:
    if ".jpeg" in pic:
        with open(path + pic, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
