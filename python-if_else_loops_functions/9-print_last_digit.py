#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0:
        last = last - 10
    return last
