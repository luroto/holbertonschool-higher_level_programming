#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        i = 0
        for z in my_list:
            if z > i:
                i = z
        return(i)
    else:
        return(None)
