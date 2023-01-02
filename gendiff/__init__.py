from gendiff.converter_json import convert_json
from gendiff.converter_yaml import convert_yaml
from gendiff.formaters import design
from gendiff.parsing import parse


def generate_diff(file_path1, file_path2, format='stylish'):
    if file_path1.endswith('json') and file_path2.endswith('json'):
        file1, file2 = convert_json(file_path1, file_path2)
    else:
        file1, file2 = convert_yaml(file_path1, file_path2)

    difference_dictionary = parse(file1, file2)

    return design(difference_dictionary, format)
