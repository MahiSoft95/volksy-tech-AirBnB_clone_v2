#!/usr/bin/python3
alphas = ''
for k in range(97, 123):
    if k % 2 != 0:
        k = k-32
    alphas = alphas + chr(k)
print('{}'.format(alphas[::-1]), end="")
