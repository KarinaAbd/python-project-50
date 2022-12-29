DOT = '.'


def get_normal(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value == '':
        return "''"
    elif value == '[complex value]':
        return value
    return f"'{str(value)}'"


def check(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def walk(difference_dict, path):  # noqa: C901
    if not isinstance(difference_dict, dict):
        return get_normal(difference_dict)

    lines = []

    for key, diff_info in difference_dict.items():
        value = diff_info.get('value')
        status = diff_info.get('status')

        if status == 'added':
            value = walk(check(value), path + DOT)
            phrase = ' was added with value: '
            lines.append(
                f"Property '{path + key}'{phrase}{value}"
            )

        elif status == 'deleted':
            lines.append(
                f"Property '{path + key}' was removed"
            )

        elif status == 'updated':
            value1, value2 = value
            value1 = walk(check(value1), path + DOT)
            value2 = walk(check(value2), path + DOT)
            item = path + key

            lines.append(
                f"Property '{item}' was updated. From {value1} to {value2}"
            )
        elif isinstance(value, dict):
            lines.append(walk(value, path + key + DOT))

    return '\n'.join(lines)


def plain(difference_dictionary):
    return walk(difference_dictionary, '')
