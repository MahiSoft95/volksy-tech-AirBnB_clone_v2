#!/usr/bin/python3
def roman_to_int(s):
    if not s:
        return 0
    if type(s) != str:
        return 0
    translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    number = 0
    for char in s:
        number += translations[char]
    return number
