from gendiff.formaters.formater_json import format_to_json
from gendiff.formaters.formater_plain import plain
from gendiff.formaters.formater_stylish import stylish


def design(intermediate_representation, style):
    if style == 'plain':
        return plain(intermediate_representation)
    elif style == 'json':
        return format_to_json(intermediate_representation)
    else:
        return stylish(intermediate_representation)
