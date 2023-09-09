import os, sys
import json
import requests

path = "supplier-data/descriptions/"
descriptions = os.listdir(path)
url = "http://localhost/fruits/"



for file in descriptions:
    if file.endswith("txt"):
        with open(path + file, 'r') as text_file:
            fruit_name = os.path.splitext(file)[0]
            # print(fruit_name)
            data = text_file.read()
            data = data.split("\n")
            test_dict = {"name": data[0], "weight": int(data[1].strip( "lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
            # print(test_dict)

            response = requests.post(url, json=test_dict)



