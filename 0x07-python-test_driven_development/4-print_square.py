#!/usr/bin/python3
"""
Function handbook:
    print_square(6)
    ######
    ######
    ######
    ######
    ######
    ######
"""


def print_square(size):
    """ This function allows to print a square given a size"""
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("{}". format('#'), end="")
        print()
