#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    newlist = sorted(my_list[:])
    for i in newlist:
        if i == 0 or newlist[i] != newlist[i-1]:
            total += newlist[i]
    return total
