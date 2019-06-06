#!/usr/bin/python3
"""This is the documentation for this task. Here we're inheriting
from a class"""


class MyList(list):

    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        print(sorted(self))
