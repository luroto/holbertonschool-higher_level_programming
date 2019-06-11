#!/usr/bin/python3
""" This is the base module for this project Almost a circle"""


class Base:
    """ This is the base superclass"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
