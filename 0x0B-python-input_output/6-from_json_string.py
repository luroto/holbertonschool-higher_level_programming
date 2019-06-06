#!/usr/bin/python3
"""This is the documentation for this module. On this file we get a
object representation of a JSON rep"""


def from_json_string(my_str):
    import json
    x = json.loads(my_str)
    return(x)
