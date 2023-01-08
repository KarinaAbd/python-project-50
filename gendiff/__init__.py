__all__ = ['generate_diff']

from gendiff.difference import get_dict_of_differences
from gendiff.formaters import design
from gendiff.parser import parse


def get_content(file_path):
    if file_path.endswith('.json'):
        with open(f'{file_path}') as input:
            return parse(input, 'json')
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(f'{file_path}') as input:
            return parse(input, 'yaml')
    else:
        raise Exception('Comparison is available only for json and yaml files')


def generate_diff(file_path1, file_path2, format='stylish'):
    file1, file2 = map(get_content, (file_path1, file_path2))
    difference_dictionary = get_dict_of_differences(file1, file2)

    return design(difference_dictionary, format)
