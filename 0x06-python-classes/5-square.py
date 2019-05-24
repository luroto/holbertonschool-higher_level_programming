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

    def area(self):
        """This function returns the square area"""
        return(self.__size**2)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def my_print(self):
            for j in range(self.__size):
                print("{}".format('#'), end="")
            print()
            if self.__size == 0:
                print()