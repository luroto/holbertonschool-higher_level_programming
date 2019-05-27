#!/usr/bin/python3
"""This module creates a rectangle"""


class Rectangle:
    """This is the class Rectangle. This time it's necessary to define some
    attributes. At this moment we have widht, height, perimeter and area"""
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return(2 * (self.__width + self.__height))

    def print(self):
        alto = self.__height
        ancho = self.__width
        if alto == 0 or ancho == 0:
            print()
        else:
            for i in range(alto):
                for j in range(ancho):
                    print("{}".format('#'), end="")
                print()

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            self.__height = self.__height - 1
            ancho = self.__width
            self.print()
            self.__height += 1
            return("{}".format("#")*ancho)

    def __repr__(self):
        alto = self.__height
        ancho = self.__width
        repre = ""
        if alto != 0 and ancho != 0:
            for i in range(alto):
                for j in range(ancho):
                    repre += "#"
                repre += ('\n')
        repre += '\n'
        return(repre)
