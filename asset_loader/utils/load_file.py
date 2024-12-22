import json


def load_json_file_path(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
