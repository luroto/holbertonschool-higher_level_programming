#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        copylist = my_list.copy()
        for i in range(len(my_list)):
            copylist[i] = my_list[i]
            if idx < 0:
                return(copylist)
            if idx >= len(my_list):
                return(copylist)
            if i == idx:
                copylist[i] = element
                return(copylist)
