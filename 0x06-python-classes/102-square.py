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
            self.__size = value

    def __lt__(self,  other):
        return self.area() < other.area()

    def __le__(self, other):
        return(self.area() <= other.area())

    def __eq__(self, other):
        return(self.area() == other.area())

    def __ne__(self, other):
        return(self.area() != other.area())

    def __get__(self, other):
        return(self.area() >= other.area())

    def __gt__(self, other):
        return(self.area() > other.area())
