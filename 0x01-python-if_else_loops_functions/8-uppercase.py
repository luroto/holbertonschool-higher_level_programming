#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            pri = ord(i) - 32
        else:
            pri = ord(i)
        print("{}".format(chr(pri)), end="")
    print("")
