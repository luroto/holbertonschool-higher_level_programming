#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return(None)
    else:
        newlist = set(my_list)
        suma = 0
        for i in newlist:
            suma += i
        return(suma)
