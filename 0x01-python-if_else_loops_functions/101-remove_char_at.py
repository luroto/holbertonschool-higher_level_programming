#!/usr/bin/python3


def remove_char_at(str, n):
    copystr = ""
    i = 0
    for i in range(len(str)):
        if i != n:
            copystr += str[i]
        i += 1
    return (copystr)
