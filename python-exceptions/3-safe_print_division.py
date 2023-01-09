#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
    except(TypeError, ValueError):
        return "something went wrong"
    finally:
        print("{}".format(div))
