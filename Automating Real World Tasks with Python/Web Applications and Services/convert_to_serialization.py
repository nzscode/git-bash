#!/usr/bin/env python3
people = [
    {'name': 'Sabrina Green',
     'username': 'sgreen',
     'phone': {'cell': '802-867-5309', 'office': '802-867-5309'},
     'department': 'IT Infrastructure',
     'role': 'System Administrator'},
    {'name': 'Eli Jones',
     'username': 'ejones',
     'phone': {'office': '684-3481127'},
     'department': 'IT Infrastructure',
     'role': 'IT specialist'}
]

def convert_to_csv(output_csv_file):
    import csv

    #Define the fields for the CSV
    fields = ['name', 'username', 'phone', 'department', 'role']

    with open(output_csv_file, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        #Write the Header Row
        writer.writeheader()

        #Write the data
        for row in people:
            writer.writerow(row)

# convert_to_csv('people.csv')


# to convert to a dictionary
def convert_to_Dict(csv_input):
    import csv

    with open(csv_input, 'r') as file:
        reader = csv.DictReader(file)
        for entry in reader:
            print(entry)

# convert_to_Dict("people.csv")



def convert_to_Json(output_json, input_dict):
    import json
    with open(output_json, 'w') as people_json:
        json.dump(input_dict, people_json, indent=2)

    print(people_json)

# convert_to_Json('people.json', people)

def convert_to_yaml(output_yaml, input_dict):
    import yaml

    with open(output_yaml, 'w') as people_yaml:
        yaml.safe_dump(input_dict, people_yaml)

# convert_to_yaml('people.yaml', people)

def convert_json_to_dict(input_json, output_dict):
    import json

    with open(input_json, 'r') as people_json:
        output_dict = json.load(people_json)
        print(output_dict)

# convert_json_to_dict('people.json', 'people_dict')

def convert_yaml_to_dict(input_yaml):
    import yaml

    with open(input_yaml, 'r') as people_yaml:
        output_dict = yaml.safe_load(people_yaml)
        print(output_dict)

convert_yaml_to_dict('people.yaml')

