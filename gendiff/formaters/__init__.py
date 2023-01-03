import json

from gendiff.formaters.formater_plain import plain
from gendiff.formaters.formater_stylish import stylish


def design(intermediate_representation, style):
    # There are three available formats for presentation of files differences.
    if style == 'plain':
        return plain(intermediate_representation)
    elif style == 'json':
        return json.dumps(intermediate_representation, indent=4)
    else:
        # Use default format 'stylish'.
        return stylish(intermediate_representation)
