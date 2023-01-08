def get_dict_of_differences(file1, file2):
    differences = {}

    keys1 = set(file1)
    keys2 = set(file2)

    all_keys = keys1 | keys2
    added = keys2 - keys1
    deleted = keys1 - keys2

    for key in sorted(all_keys):
        if key in added:
            differences[key] = {
                'status': 'added',
                'value': file2.get(key)
            }
        elif key in deleted:
            differences[key] = {
                'status': 'deleted',
                'value': file1.get(key)
            }
        elif file1.get(key) == file2.get(key):
            differences[key] = {
                'value': file1.get(key)
            }
        elif isinstance(file1.get(key), dict) \
                and isinstance(file2.get(key), dict):
            differences[key] = {
                'status': 'nested',
                'value': get_dict_of_differences(file1.get(key), file2.get(key))
            }
        else:
            differences[key] = {
                'status': 'updated',
                'value': [file1.get(key), file2.get(key)]
            }
    return differences
