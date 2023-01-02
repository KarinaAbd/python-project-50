from gendiff.converter import convert_file_to_python
from gendiff.formaters import design
from gendiff.parsing import parse


def generate_diff(file_path1, file_path2, format='stylish'):
    file1, file2 = map(convert_file_to_python, (file_path1, file_path2))
    difference_dictionary = parse(file1, file2)

    return design(difference_dictionary, format)
