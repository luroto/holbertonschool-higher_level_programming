#!/usr/bin/python3
"""This is the documentation for this module. On this file we have to
create an Object from a JSON file"""


def load_from_json_file(filename):
    import json
    with open(filename, 'r') as filej:
        x = json.load(filej)
    return(x)
