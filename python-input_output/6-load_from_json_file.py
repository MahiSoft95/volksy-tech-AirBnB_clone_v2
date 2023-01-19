#!/usr/bin/python3
"""def load_from_json_file(filename):"""
import json


def save_to_json_file(my_obj, filename):
    """def load_from_json_file(filename):"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
