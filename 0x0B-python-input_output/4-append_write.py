#!/usr/bin/python3
"""This is the documentation for this module. On this file we have to append
a string into a given file"""


def append_write(filename="", text=""):
    with open(filename, 'a') as archivo:
            return(archivo.write(text))
