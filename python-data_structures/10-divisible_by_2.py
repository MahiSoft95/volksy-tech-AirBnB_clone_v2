#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    newlist += my_list
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            newlist[k] = True
        else:
            newlist[k] = False
    return newlist
