#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    newlist = [x if x != search else replace for x in newlist]
    return newlist
