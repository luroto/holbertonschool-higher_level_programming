#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 != 0:
        temp = i - 32
    else:
        temp = i
    print("{:s}".format(chr(temp)), end="")
