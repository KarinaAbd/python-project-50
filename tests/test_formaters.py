import json

from gendiff import generate_diff


def test_generate_diff_in_plain_format():
    file_path1 = './tests/fixtures/file1_nested.json'
    file_path2 = './tests/fixtures/file2_nested.json'
    result = generate_diff(file_path1, file_path2, 'plain')
    correct = open('./tests/fixtures/result_plain_format.txt')

    assert result == correct.read()


def test_generate_diff_in_json_format():
    file_path1 = './tests/fixtures/file1_nested.json'
    file_path2 = './tests/fixtures/file2_nested.json'
    result = generate_diff(file_path1, file_path2, 'json')

    assert json.loads(result)