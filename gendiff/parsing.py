def get_normal_value(file, key):
    value = file.get(key)
    if isinstance(value, bool):
        return str(value).lower()
    return value


def parse(file1, file2):
    keys1 = set(file1)
    keys2 = set(file2)
    all_keys = keys1 | keys2

    lines = []

    for key in sorted(all_keys):
        value1 = get_normal_value(file1, key)
        value2 = get_normal_value(file2, key)

        if key in (keys1 - keys2):
            lines.append(f'  - {key}: {value1}')
        elif key in (keys1 & keys2):
            if value1 == value2:
                lines.append(f'    {key}: {value1}')
            else:
                lines.append(f'  - {key}: {value1}')
                lines.append(f'  + {key}: {value2}')
        elif key in (keys2 - keys1):
            lines.append(f'  + {key}: {value2}')

    return lines
