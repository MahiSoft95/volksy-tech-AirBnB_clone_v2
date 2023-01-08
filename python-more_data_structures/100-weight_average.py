#!/usr/bin/python3
def weight_average(my_list=[]):
    summation = 0
    count = 0
    if my_list:
        for x, y in my_list:
            summmation += x * y
            count += y
        average = summation/count
        return average
    else:
        return 0
