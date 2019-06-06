#!/usr/bin/python3
""" This module checks if an object is a subclass of some class"""


def inherits_from(obj, a_class):
    """ This function do the check"""
    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return(True)
    return(False)
