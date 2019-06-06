#!/usr/bin/python3
"""This is the documentation for this module. Just read a filename, and
write its content into the stdout"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        for i in f:
            print("{}".format(i), end="")
