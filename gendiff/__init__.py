__all__ = ['generate_diff']

from gendiff.difference import get_dict_of_differences
from gendiff.formaters import reformat
from gendiff.parser import parse


def get_content(file_path):
    if file_path.endswith('.json'):
        with open(f'{file_path}') as input:
            return parse(input, 'json')
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(f'{file_path}') as input:
            return parse(input, 'yaml')
    raise Exception('Comparison is available only for json and yaml files')


def generate_diff(file_path1, file_path2, format='stylish'):
    '''Function compares two configuration files and returns a difference.

    Keyword argument:
    format -- formatter name for presentation of files differences.
              There are 3 available formats: stylish (default), plain, json.
    '''
    file1, file2 = map(get_content, (file_path1, file_path2))
    difference_dictionary = get_dict_of_differences(file1, file2)

    return reformat(difference_dictionary, format)
