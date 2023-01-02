import json
import yaml


def convert_json(file_path):
    with open(f'{file_path}') as input:
        file = json.load(input)
    return file


def convert_yaml(file_path):
    with open(f'{file_path}') as input:
        file = yaml.load(input, Loader=yaml.FullLoader)
    return file


def convert_file_to_python(file):
    if file.endswith('json'):
        file_py = convert_json(file)
    else:
        file_py = convert_yaml(file)
    return file_py
