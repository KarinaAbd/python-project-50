import json

import yaml


def parse(content, format_name):
    if format_name == 'json':
        return json.load(content)
    if format_name == 'yaml':
        return yaml.safe_load(content)
