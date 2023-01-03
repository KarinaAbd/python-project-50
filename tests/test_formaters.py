import json

import pytest

from gendiff import generate_diff


def get_full_path(file_name):
    return f'./tests/fixtures/{file_name}'


@pytest.mark.parametrize('input1, input2, format, expected', [
    ('file1_nested.json', 'file2_nested.json', 'plain', 'plain_result.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'plain', 'plain_result.txt')
])
def test_generate_diff_in_plain_format(input1, input2, format, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    correct = open(get_full_path(expected))
    assert result == correct.read()


@pytest.mark.parametrize('input1, input2, format', [
    ('file1_nested.json', 'file2_nested.json', 'json'),
    ('file1_nested.yml', 'file2_nested.yml', 'json')
])
def test_generate_diff_in_json_format(input1, input2, format):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    assert json.loads(result)
