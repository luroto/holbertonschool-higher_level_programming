#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    else:
        i = 0
        for z in my_list:
            if z > i:
                i = z
        return(i)
