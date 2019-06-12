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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This function returns the JSON rep of an object"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This function saves a json string to a file """
        nombre = cls.__name__ + ".json"
        nuevo = []
        if list_objs:
            for argu in list_objs:
                nuevo.append(argu.to_dictionary())
        with open(nombre, 'w') as archi:
            guarda = cls.to_json_string(nuevo)
            archi.write(guarda)
