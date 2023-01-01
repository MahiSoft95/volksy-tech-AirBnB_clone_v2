#!/usr/bin/python3
def print_last_digit(number):
    l = number % 10
    if number < 0:
        l = l - 10
    return l
