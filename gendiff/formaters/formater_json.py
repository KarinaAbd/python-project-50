import json


def format_to_json(difference_dict):
    return json.dumps(difference_dict, indent=4)
