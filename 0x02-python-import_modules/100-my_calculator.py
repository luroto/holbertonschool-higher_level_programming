#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    total = len(argv)
    if total != 4:
        print("Usage: ./100-my_calculator <a> <operator> <b>")
        exit(1)
    opera = argv[2]
    if opera != "+" and opera != "-" and opera != "*" and opera != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if opera == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if opera == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if opera == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if opera == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
