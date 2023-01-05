__all__ = ['generate_diff']

import json

import yaml

from gendiff.difference import get_dict_of_differences
from gendiff.formaters import design


def parse(content, format_name):
    if format_name == 'json':
        return json.load(content)
    if format_name == 'yaml':
        return yaml.safe_load(content)


def generate_diff(file_path1, file_path2, format='stylish'):
    dicts = []

    for file_path in file_path1, file_path2:
        if file_path.endswith('.json'):
            with open(f'{file_path}') as input:
                file = parse(input, 'json')
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            with open(f'{file_path}') as input:
                file = parse(input, 'yaml')
        dicts.append(file)

    file1, file2 = dicts
    difference_dictionary = get_dict_of_differences(file1, file2)

    return design(difference_dictionary, format)
