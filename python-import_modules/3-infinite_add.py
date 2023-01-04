#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = argv[1:]
    sum = 0
    for k in x:
        sum = sum + int(k)
    print("{}".format(sum))
