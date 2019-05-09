#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return(my_list)
    else:
        newlist = my_list.copy()
        for i in range(len(my_list)):
            if my_list[i] == search:
                newlist[i] = replace
            else:
                newlist[i] = my_list[i]
        return(newlist)
