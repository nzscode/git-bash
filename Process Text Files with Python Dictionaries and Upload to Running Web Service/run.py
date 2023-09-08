#! /usr/bin/env python3

import os
import requests
url = 'http://34.125.11.126/feedback/'
directory = '/data/feedback'
folder = os.listdir("feedback/")
files = [filename for filename in folder if filename.endswith('.txt')]
for filename in files:
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r') as file:
        contents = file.read()
        content = contents.split('\n')

        feedback_dict = {'title': content[0].strip(), 'name': content[1].strip(), 'date': content[2].strip(), 'feedback': content[3].strip()}
        # print(feedback_dict)

        response = requests.post(url, json=feedback_dict)

        if response.status_code == 201:
            print(f"feedback uploaded successfully from file: {filename}")

        else:
            print(f"Error uploading feedback from fileL {filename}")
            print("Response Status Code:", response_status_code)
            print("Response content:", response.text)


