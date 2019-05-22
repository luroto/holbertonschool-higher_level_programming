#!/usr/bin/python3
"""This is the first project using Documentation for Python """


class Square:
    """On this task I'll set a size and dispose some exceptions"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
