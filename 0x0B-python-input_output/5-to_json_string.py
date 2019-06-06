#!/usr/bin/python3
"""This is the documentation for this module. On this file we get a
JSON representation of an objectdef to_json_string(my_obj)"""


def to_json_string(my_obj):
    import json
    x = json.dumps(my_obj)
    return(x)
