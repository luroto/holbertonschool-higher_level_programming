#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = len(argv)
    if total == 1:
        print("0 arguments.")
    elif total == 2:
        print("1 argument:")
        print("{:d}: {:s}".format((1), argv[1]))
    else:
        print("{:d} arguments".format(total - 1))
        for i in range(1, total):
            print("{:d}: {:s}".format(i, argv[i]))
