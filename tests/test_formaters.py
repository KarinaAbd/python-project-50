from gendiff import generate_diff
from gendiff.formaters.formater_json import format_to_json
from gendiff.formaters.formater_plain import plain
import json


def test_generate_diff_in_plain_format():
    file_path1 = './tests/fixtures/file1_nested.json'
    file_path2 = './tests/fixtures/file2_nested.json'
    result = generate_diff(file_path1, file_path2, format=plain)
    correct = open('./tests/fixtures/result_plain_format.txt')

    assert result == correct.read()


def test_generate_diff_in_json_format():
    file_path1 = './tests/fixtures/file1_nested.json'
    file_path2 = './tests/fixtures/file2_nested.json'
    result = generate_diff(file_path1, file_path2, format=format_to_json)

    assert json.loads(result)
