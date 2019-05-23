#!/usr/bin/python3
"""This is the first project using Documentation for Python """


class Square:
    """On this task I'll set a size and dispose some exceptions"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if isinstance(position[0], int) is False or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[1], int) is False or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """This function returns the square area"""
        return(self.__size**2)

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if isinstance(position[0], int) is False or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(position[1], int) is False or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            lenght = self.position[0] + self.size
            spaces = self.position[0]
            deep = self.position[1]
            for i in range(deep):
                print()
            for x in range(self.size):
                for y in range(lenght):
                    if y < spaces:
                        print("{}".format(" "), end="")
                    else:
                        print("{}".format("#"), end="")
                print()
