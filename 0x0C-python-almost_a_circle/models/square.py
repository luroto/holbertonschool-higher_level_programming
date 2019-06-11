#!/usr/bin/python3
""" This module contains all about the Square class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ This is the main definition of Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor"""
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """ Size getter"""
        return(self.width)

    @size.setter
    def size(self, size):
        """ Size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """ This function returns a string representation of the polygone"""
        return("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
               self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ This function updates values in the instance attributes"""
        if args and args != "":
            i = 0
            for argu in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
                i += 1
        else:
            i = 0
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
