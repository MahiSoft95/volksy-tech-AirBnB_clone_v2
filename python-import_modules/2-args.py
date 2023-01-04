#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = argv[1:]
    if len(x) == 0:
        print("{} arguments.".format(len(x)))
    else:
        print("{} arguments.".format(len(x)))
        n = 1
        for k in x:
            print("{}: {}".format(n, k))
            n = n + 1
