#!/usr/bin/python3
""" This is the base module for this project Almost a circle"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This function returns the JSON string rep of an object"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return(json.dumps(list_dictionaries))
