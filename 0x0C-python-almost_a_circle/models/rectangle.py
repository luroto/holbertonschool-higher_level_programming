#!/usr/bin/python3
""" This is the rectangle module"""

from .base import Base


class Rectangle(Base):
    """ This is the class Rectangle, which inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for the Rectangle class"""
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        super().__init__(id)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, y):
        self.__y = value
