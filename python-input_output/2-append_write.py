#!/usr/bin/python3
"""Using with statement writing into the file"""


def write_file(filename="", text=""):
    """def write_file(filename="", text=""):"""
    with open(filename, 'a') as f:
        return f.write(text)
