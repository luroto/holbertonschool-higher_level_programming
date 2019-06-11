#!/usr/bin/python3
"""This module creates a rectangle"""
from .base import Base


class Rectangle(Base):
    """ This is the class Rectangle, which inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for the Rectangle class"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter""" 
        return(self.__x)

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter"""
        return(self.__y)

    @y.setter
    def y(self, value):
        """y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This function returns the area of the polygone"""
        ancho = self.__width
        alto = self.__height
        return(ancho * alto)

    def display(self):
        """ This function prints the polygone"""
        ancho = self.__width
        alto = self.__height
        corre = self.__x
        prof = self.__y
        i = 0
        j = 0
        al = 0
        for al in range(prof):
            print()
        for i in range(alto):
            for j in range(ancho + corre):
                if j < corre:
                    print("{}".format("  "), end="")
                else:
                    print("{}".format('#'), end="")
            print()

    def __str__(self):
        """ Returns a string representation of the polygone"""
            return("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                   self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Updates all the info """
        if args and args != "":
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
                i += 1
        else:
            if kwargs and kwargs != "":
                i = 0
                for key, value in kwargs.items():
                    if key == "height":
                        self.__height = value
                    if key == "width":
                        self.__width = value
                    if key == "id":
                        self.id = value
                    if key == "x":
                        self.__x = value
                    if key == "y":
                        self.__y = value
