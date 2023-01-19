#!/usr/bin/python3
"""Using with statement writing into the file"""


def write_file(filename="", text=""):
    """def write_file(filename="", text=""):"""
    with open(filename, 'w') as f:
        f.write(text)
