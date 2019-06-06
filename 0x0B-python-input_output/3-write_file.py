#!/usr/bin/python3
"""This is the documentation for this module. This time we have to add
a string into a given file, no matter if file previously existed or not"""


def write_file(filename="", text=""):
    with open(filename, 'w') as archivo:
        return(archivo.write(text))
