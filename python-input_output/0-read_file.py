#!/usr/bin/python3
"""Using with statement read and print data in stdout"""


def read_file(filename=""):
    """def read_file(filename=""):"""
    with open(filename, 'r') as f:
        print(f.read(), end="")
