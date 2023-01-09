def build_diff_tree(content1, content2):
    differences = {}

    keys1 = set(content1)
    keys2 = set(content2)

    all_keys = keys1 | keys2
    added = keys2 - keys1
    deleted = keys1 - keys2

    for key in sorted(all_keys):
        if key in added:
            differences[key] = {
                'status': 'added',
                'value': content2.get(key)
            }
        elif key in deleted:
            differences[key] = {
                'status': 'deleted',
                'value': content1.get(key)
            }
        elif content1.get(key) == content2.get(key):
            differences[key] = {
                'status': 'unchanged',
                'value': content1.get(key)
            }
        elif isinstance(content1.get(key), dict) \
                and isinstance(content2.get(key), dict):
            differences[key] = {
                'status': 'nested',
                'value': build_diff_tree(content1.get(key), content2.get(key))
            }
        else:
            differences[key] = {
                'status': 'updated',
                'value': [content1.get(key), content2.get(key)]
            }
    return differences
