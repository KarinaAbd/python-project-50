def walk_unchanged(nest):
    if not isinstance(nest, dict):
        return nest
    nested_level = {}

    for key in sorted(set(nest)):
        nested_level[key] = {
            'value': walk_unchanged(nest.get(key))
        }
    return nested_level


def check_type(item1, item2):
    if not isinstance(item1, dict) and not isinstance(item2, dict):
        return [item1, item2]
    elif not isinstance(item1, dict) and isinstance(item2, dict):
        return [item1, walk_unchanged(item2)]
    elif isinstance(item1, dict) and not isinstance(item2, dict):
        return [walk_unchanged(item1), item2]
    else:
        return item1, item2


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
                'value': walk_unchanged(file2.get(key))
            }
        elif key in deleted:
            differences[key] = {
                'status': 'deleted',
                'value': walk_unchanged(file1.get(key))
            }
        elif file1.get(key) == file2.get(key):
            differences[key] = {
                'value': walk_unchanged(file1.get(key))
            }
        elif isinstance(check_type(file1.get(key), file2.get(key)), tuple):
            dict1, dict2 = check_type(file1.get(key), file2.get(key))
            differences[key] = {
                'value': get_dict_of_differences(dict1, dict2)
            }
        else:
            differences[key] = {
                'status': 'updated',
                'value': check_type(file1.get(key), file2.get(key))
            }
    return differences
