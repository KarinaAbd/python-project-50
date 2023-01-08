import json

from gendiff.formaters.formater_plain import plain
from gendiff.formaters.formater_stylish import stylish


def reformat(intermediate_representation, formatter_name):
    # There are three available formats for presentation of files differences.
    if formatter_name == 'stylish':
        return stylish(intermediate_representation)
    if formatter_name == 'plain':
        return plain(intermediate_representation)
    if formatter_name == 'json':
        return json.dumps(intermediate_representation, indent=4)
    else:
        raise Exception('Invalid format, choose from stylish, plain, json')
