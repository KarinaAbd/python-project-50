def walk_unchanged(nest, level):
    if not isinstance(nest, dict):
        return nest
    nested_level = {}

    for key in sorted(set(nest)):
        nested_level[key] = {
            'level': level,
            'status': 'remaining',
            'value': walk_unchanged(nest.get(key), level + 1)
        }
    return nested_level


def parse(file1, file2):

    def walk(nest1, nest2, level):
        if not isinstance(nest1, dict) and not isinstance(nest2, dict):
            return [nest1, nest2]
        elif not isinstance(nest1, dict) and isinstance(nest2, dict):
            return [nest1, walk_unchanged(nest2, level + 1)]
        elif isinstance(nest1, dict) and not isinstance(nest2, dict):
            return [walk_unchanged(nest1, level + 1), nest2]

        difference = {}

        keys1 = set(nest1)
        keys2 = set(nest2)

        all_keys = keys1 | keys2
        added = keys2 - keys1
        deleted = keys1 - keys2

        for key in sorted(all_keys):
            if key in added:
                difference[key] = {
                    'level': level,
                    'status': 'added',
                    'value': walk_unchanged(nest2.get(key), level + 1)
                }
            elif key in deleted:
                difference[key] = {
                    'level': level,
                    'status': 'deleted',
                    'value': walk_unchanged(nest1.get(key), level + 1)
                }
            else:
                if nest1.get(key) == nest2.get(key):
                    difference[key] = {
                        'level': level,
                        'status': 'remaining',
                        'value': walk_unchanged(nest1.get(key), level + 1)
                    }
                else:
                    difference[key] = {
                        'level': level,
                        'status': 'changed',
                        'value': walk(nest1.get(key), nest2.get(key), level + 1)
                    }
        return difference
    return walk(file1, file2, 0)
