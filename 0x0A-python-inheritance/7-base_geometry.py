#!/usr/bin/python3
""" On this module we'll write an empty class """


class BaseGeometry:
    """ This is the empty class"""
    pass

    def area(self):
        """ For the area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This verifyies value's value and type"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
