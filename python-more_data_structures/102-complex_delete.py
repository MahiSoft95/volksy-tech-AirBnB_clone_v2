#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = False
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == value:
                temp = k
        if temp:
            del a_dictionary[k]
            return (complex_delete(a_dictionary, value))
    return a_dictionary
