DOT = '.'


def to_str(value):
    if isinstance(value, bool):
        result = str(value).lower()
    elif value is None:
        result = 'null'
    elif isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, int):
        result = value
    else:
        result = f"'{str(value)}'"
    return result


def plain(difference_dict, path=''):
    lines = []

    for key, diff_info in difference_dict.items():
        value = diff_info.get('value')
        status = diff_info.get('status')

        if status == 'added':
            value = to_str(value)
            phrase = ' was added with value: '
            lines.append(
                f"Property '{path + key}'{phrase}{value}"
            )

        elif status == 'deleted':
            lines.append(
                f"Property '{path + key}' was removed"
            )

        elif status == 'updated':
            value1, value2 = map(to_str, value)
            item = path + key

            lines.append(
                f"Property '{item}' was updated. From {value1} to {value2}"
            )
        elif isinstance(value, dict):
            lines.append(plain(value, path + key + DOT))

    return '\n'.join(lines)
