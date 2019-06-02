#!/usr/bin/python3
"""This module creates a rectangle"""


class Rectangle:
    """This is the class Rectangle. This time it's necessary to define some
    attributes. At this moment we have widht, height, perimeter and area"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Function that returns the area of a rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """ Function for returning the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return(2 * (self.__width + self.__height))

    def print(self):
        """Section for printing a rectangle """
        alto = self.__height
        ancho = self.__width
        if alto == 0 or ancho == 0:
            print()
        else:
            for i in range(alto):
                for j in range(ancho):
                    print("{}".format(self.print_symbol), end="")
                print()

    def __str__(self):
        """ Section which merely prints a copy of the instance/object?"""
        repre = ""
        if self.__width == 0 or self.__height == 0:
            return (repre)
        else:
            alto = self.__height
            ancho = self.__width
            for i in range(alto):
                for j in range(ancho):
                    repre += str(self.print_symbol)
                repre += '\n'
            return(repre[:-1])

    def __repr__(self):
        """section which returns the exact string to create a rectangle"""
        alto = self.__height
        ancho = self.__width
        clnm = "Rectangle"
        parentop = "("
        parentclose = ")"
        commo = ", "
        repre = clnm + parentop + str(ancho) + commo + str(alto) + parentclose
        return(repre)

    def __del__(self):
        """ section which disposes routine for del cases"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
