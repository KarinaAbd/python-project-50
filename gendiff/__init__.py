__all__ = ['generate_diff']

import json

import yaml

from gendiff.difference import get_dict_of_differences
from gendiff.formaters import design


def parse_file(file_path):
    with open(f'{file_path}') as input:
        if file_path.endswith('json'):
            return json.load(input)
        else:
            return yaml.safe_load(input)


def generate_diff(file_path1, file_path2, format='stylish'):
    file1, file2 = map(parse_file, (file_path1, file_path2))
    difference_dictionary = get_dict_of_differences(file1, file2)

    return design(difference_dictionary, format)
