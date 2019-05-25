#!/usr/bin/python3
"""
Function handbook:

text_identation("Testing this. Do you see the newlines? It's rare if you don't: all are in the code."
Testing this.

Do you see the newlines?

It's rare if you dont:

all are in the code.


"""
def text_indentation(text):
    """ This function splits texts adding newlines when some separators are found"""
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    total = len(text)
    while i < total:
        if text[0] == ' ':
            pass
        if text[i] == '.' or text[i] == ':' or text[i] == "?":
            print("{}{}".format(text[i],'\n'))
            i += 2
        print("{}".format(text[i]), end="")
        i += 1
        if text[total -1] == ' ':
            pass
