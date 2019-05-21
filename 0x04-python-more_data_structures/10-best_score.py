#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return(None)
    else:
        newdict = a_dictionary.items()
        newdict = max(list(newdict))
        return (newdict[0])
