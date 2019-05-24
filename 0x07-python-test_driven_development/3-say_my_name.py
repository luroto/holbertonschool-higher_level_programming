#!/usr/bin/python3
"""
Function handbook

say_my_name("Lucia", "Rodriguez")
My name is Lucia Rodriguez

"""


def say_my_name(first_name, last_name=""):
    """ This function will print your name. If arguments are different\
        strings, it'll show an error message and the program will be closed"""
    if type(first_name) != str and type(last_name) != str:
        raise TypeError("both first_name and last_name must be strings")
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
