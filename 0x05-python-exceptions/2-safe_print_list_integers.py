#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    suma = 0
    for i in my_list:
        try:
            if i <= x:
                print("{:d}". format(i))
                suma += 1
        except ValueError:
            pass
    return(suma)
