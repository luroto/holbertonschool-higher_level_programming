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

    @staticmethod
    def from_json_string(json_string):
        nuevo = []
        if json_string:
            nuevo = json.loads(json_string)
        return nuevo

    @classmethod
    def create(cls, **dictionary):
        """This method creates an instance"""
        nombrecito = cls.__name__
        if nombrecito == "Square":
            muneco = cls(10)
        if nombrecito == "Rectangle":
            muneco = cls(10, 42)
        muneco.update(**dictionary)
        return muneco

    @classmethod
    def load_from_file(cls):
        """ Load info from file"""
        nombrecito = cls.__name__ + ".json"
        listica = []
        try:
            with open(nombrecito, 'r') as archivo:
                cuy = cls.json.load(archivo)
                sabor = cls.from_json_string(cuy)
                hambre = cls.create(sabor)
            return hambre
        except:
            return listica


