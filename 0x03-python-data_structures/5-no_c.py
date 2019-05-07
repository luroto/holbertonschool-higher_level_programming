#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new = my_string.replace('C', "")
        new = new.replace('c', "")
    return (new)
