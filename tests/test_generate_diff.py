import pytest
from gendiff import generate_diff


JSON1 = './tests/fixtures/file1.json'
JSON2 = './tests/fixtures/file2.json'
YAML1 = './tests/fixtures/file1.yml'
YAML2 = './tests/fixtures/file2.yml'
RESULT = './tests/fixtures/result.txt'


JSON1_N = './tests/fixtures/file1_nested.json'
JSON2_N = './tests/fixtures/file2_nested.json'
YAML1_N = './tests/fixtures/file1_nested.yml'
YAML2_N = './tests/fixtures/file2_nested.yml'
RESULT_N = './tests/fixtures/result_nested.txt'


@pytest.mark.parametrize('input1, input2, expected', [
    (JSON1, JSON2, RESULT),
    (YAML1, YAML2, RESULT),
    (JSON1_N, JSON2_N, RESULT_N),
    (YAML1_N, YAML2_N, RESULT_N)
])
def test_generate_diff(input1, input2, expected):
    result = generate_diff(input1, input2)
    correct = open(expected)
    assert result == correct.read()
