import json


def read_json(input_file):
    with open(input_file) as json_file:
        return json.load(json_file)
