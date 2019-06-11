#!/usr/bin/python3
""" This module contains all about the Square class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ This is the main definition of Square """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
