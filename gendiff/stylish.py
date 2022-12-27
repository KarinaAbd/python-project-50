import itertools


ADD = '  + '
DEL = '  - '
SP = '    '


def get_normal_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def format(difference_dictionary):
    def walk(diff_dict, level):
        current_indent = SP * level
        lines = []
        if not isinstance(diff_dict, dict):
            return get_normal_value(diff_dict)

        for key, diff_info in diff_dict.items():
            value = diff_info['value']
            if not isinstance(value, list):
                if diff_info['status'] == 'added':
                    lines.append(
                        f'{current_indent}{ADD}{key}: {walk(value, level + 1)}'
                    )
                elif diff_info['status'] == 'deleted':
                    lines.append(
                        f'{current_indent}{DEL}{key}: {walk(value, level + 1)}'
                    )
                elif diff_info['status'] == 'remaining':
                    lines.append(
                        f'{current_indent}{SP}{key}: {walk(value, level + 1)}'
                    )
                elif diff_info['status'] == 'changed':
                    lines.append(
                        f'{current_indent}{SP}{key}: {walk(value, level + 1)}'
                    )
            else:
                value1 = value[0]
                value2 = value[1]
                lines.append(
                    f'{current_indent}{DEL}{key}: {walk(value1, level + 1)}'
                )
                lines.append(
                    f'{current_indent}{ADD}{key}: {walk(value2, level + 1)}'
                )

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return walk(difference_dictionary, 0)
