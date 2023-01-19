#!/usr/bin/python3
"""From json string to python datastructure"""
import json


def from_json_string(my_str):
    """def from_json_string(my_str):"""
    return json.loads(my_str)
