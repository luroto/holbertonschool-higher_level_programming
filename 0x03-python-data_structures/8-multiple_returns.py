#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        firchar = None
    else:
        firchar = sentence[0]
    longi = len(sentence)
    newtupla = longi, firchar
    return(newtupla)
