from gendiff import generate_diff


def test_generate_diff_json():
    file_path1 = './tests/fixtures/file1.json'
    file_path2 = './tests/fixtures/file2.json'
    result = generate_diff(file_path1, file_path2)
    correct = open('./tests/fixtures/result.txt')

    assert result == correct.read()


def test_generate_diff_yaml():
    file_path1 = './tests/fixtures/file1.yml'
    file_path2 = './tests/fixtures/file2.yml'
    result = generate_diff(file_path1, file_path2)
    correct = open('./tests/fixtures/result.txt')

    assert result == correct.read()


def test_generate_diff_nested_json():
    file_path1 = './tests/fixtures/file1_nested.json'
    file_path2 = './tests/fixtures/file2_nested.json'
    result = generate_diff(file_path1, file_path2)
    correct = open('./tests/fixtures/result_nested.txt')

    assert result == correct.read()


def test_generate_diff_nested_yaml():
    file_path1 = './tests/fixtures/file1_nested.yml'
    file_path2 = './tests/fixtures/file2_nested.yml'
    result = generate_diff(file_path1, file_path2)
    correct = open('./tests/fixtures/result_nested.txt')

    assert result == correct.read()
