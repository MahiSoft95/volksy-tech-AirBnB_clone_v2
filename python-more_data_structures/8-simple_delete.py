#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    temp = False
    for k in a_dictionary:
        if k == key:
            temp = True
    if temp:
        del a_dictionary[key]
    return a_dictionary
