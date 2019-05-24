#!/usr/bin/python3
"""
Function cheatsheet:
add_integer(4, 5)
9
"""


def add_integer(a, b=98):
    """ This function works only with integer and float numbers, any other
    type of argument will be re rejected"""
    if (type(a) != int and type(a) != float and type(b) != int and
            type(b) != float):
        raise TypeError("a and b both must be integers.")
    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if isinstance(a, int) is True and isinstance(b, int) is True:
        c = a + b
        return(c)
