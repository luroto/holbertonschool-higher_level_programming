#!/usr/bin/python3
"""This is the documentation for this module. Just read a filename, and
prints its content given a number of lines"""


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        i = 0
        for lines in f:
            if nb_lines > 0 and nb_lines <= i:
                break
            i += 1
            print("{}".format(lines), end="")
