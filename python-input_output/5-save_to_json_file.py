#!/usr/bin/python3
"""def save_to_json_file(my_obj, filename):"""
import json


def save_to_json_file(my_obj, filename):
    """def from_json_string(my_str):"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
