import json
import yaml
from gendiff.formaters import design
from gendiff.difference import get_dict_of_differences


__all__ = ['generate_diff']


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
