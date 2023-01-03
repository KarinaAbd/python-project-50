import json
import yaml
from gendiff.formaters import design
from gendiff.parsing import parse


__all__ = ['generate_diff']


def convert_file_to_python(file):
    with open(f'{file}') as input:
        if file.endswith('json'):
            return json.load(input)
        else:
            return yaml.safe_load(input)


def generate_diff(file_path1, file_path2, format='stylish'):
    file1, file2 = map(convert_file_to_python, (file_path1, file_path2))
    difference_dictionary = parse(file1, file2)

    return design(difference_dictionary, format)
