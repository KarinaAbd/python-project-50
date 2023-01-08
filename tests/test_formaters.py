import json

import pytest

from gendiff import generate_diff
from tests import get_full_path


@pytest.mark.parametrize('input1, input2, format, expected', [
    ('file1_nested.json', 'file2_nested.json', 'plain', 'plain_result.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'plain', 'plain_result.txt')
])
def test_generate_diff_in_plain_format(input1, input2, format, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    with open(f'{get_full_path(expected)}') as correct:
        assert result == correct.read()


@pytest.mark.parametrize('input1, input2, format', [
    ('file1_nested.json', 'file2_nested.json', 'json'),
    ('file1_nested.yml', 'file2_nested.yml', 'json')
])
def test_generate_diff_in_json_format(input1, input2, format):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2, format)
    assert json.loads(result)


@pytest.mark.parametrize('input1, input2, format', [
    ('file1_nested.yml', 'file2_nested.yml', 'style'),
    ('file1_nested.json', 'file2_nested.json', 'pain'),
    ('file1_nested.yml', 'file2_nested.yml', 'JSON')
])
def test_generate_diff_in_wrong_format(input1, input2, format):
    file1, file2 = map(get_full_path, (input1, input2))
    with pytest.raises(Exception) as e:
        generate_diff(file1, file2, format)
    assert str(e.value) == 'Invalid format, choose from stylish, plain, json'
