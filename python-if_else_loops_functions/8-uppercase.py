#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) >= 97 and ord(k) <= 122:
            k = ord(k)-32
        print('{}'.format(chr(k)), end="")
    print()
