import pytest

from gendiff import generate_diff
from tests import get_full_path


@pytest.mark.parametrize('input1, input2, expected', [
    ('file1.json', 'file2.json', 'result.txt'),
    ('file1.yml', 'file2.yml', 'result.txt'),
    ('file1_nested.json', 'file2_nested.json', 'result_nested.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'result_nested.txt')
])
def test_generate_diff(input1, input2, expected):
    file1, file2 = map(get_full_path, (input1, input2))
    result = generate_diff(file1, file2)
    with open(f'{get_full_path(expected)}') as expected_file:
        assert result == expected_file.read()


@pytest.mark.parametrize('input1, input2', [
    ('result.txt', 'result_nested.txt'),
])
def test_exception_in_generate_diff(input1, input2):
    file1, file2 = map(get_full_path, (input1, input2))
    with pytest.raises(Exception) as e:
        generate_diff(file1, file2)
    assert str(e.value) == \
        'Comparison is available only for json and yaml files'
