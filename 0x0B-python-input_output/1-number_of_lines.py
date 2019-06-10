    #!/usr/bin/python3
"""This is the documentation for this module. Just read a filename, and
return the number of lines"""


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        i = 0
        for lines in f:
            i += 1
    return(i)
