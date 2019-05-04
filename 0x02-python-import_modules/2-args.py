#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    if total == 1:
        print("0 arguments.")
    elif total == 2:
        print("1 argument:")
        print("{:d}: {:s}".format((1), sys.argv[1]))
    else:
        print("{:d} arguments".format(total - 1))
        for i in range(0, total-1):
            print("{:d}: {:s}".format(i+1, sys.argv[i+1]))
