#!/usr/bin/python3
""" This module checks if an object is an instance of some
class"""


def is_same_class(obj, a_class):
    if type(obj) != a_class:
        return(False)
    return(True)
