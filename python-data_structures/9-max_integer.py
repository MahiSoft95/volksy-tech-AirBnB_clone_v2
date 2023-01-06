#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        newlist = [my_list[0]]
        for i in my_list:
            if i > newlist[0]:
                newlist[0] = i
        return newlist[0]

    else:
        return None
